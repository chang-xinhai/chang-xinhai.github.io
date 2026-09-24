"""No network access: ensure bad responses cannot masquerade as fresh statistics."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import requests
from main import ScholarError, fetch_profile, main, parse_profile, write_results


def profile(values=(62, 62, 5, 5, 1, 1)):
    rows = ''.join(
        f'<tr><td>{label}</td><td class="gsc_rsb_std">{values[i*2]}</td>'
        f'<td class="gsc_rsb_std">{values[i*2+1]}</td></tr>'
        for i, label in enumerate(('Citations', 'h-index', 'i10-index')))
    return f'<div id="gsc_prf_in">Xinhai Chang</div><table id="gsc_rsb_st">{rows}</table>'


def response(html=None, status=200, url='https://scholar.google.com/citations?user=test&hl=en'):
    return Mock(content=(html if html is not None else profile()).encode(), status_code=status, url=url)


class ProfileTests(unittest.TestCase):
    def test_all_time_values_are_not_confused_with_recent_values(self):
        data = parse_profile(profile(('1,234', 456, 18, 7, 25, 3)), 'test')
        self.assertEqual((data['citedby'], data['hindex'], data['i10index']), (1234, 18, 25))
        self.assertEqual((data['citedby5y'], data['hindex5y']), (456, 7))

    def test_actual_zero_metrics_are_valid(self):
        self.assertEqual(parse_profile(profile((0,)*6), 'test')['hindex'], 0)

    def test_missing_or_malformed_metrics_fail_instead_of_defaulting_to_zero(self):
        for html in ('<html>Consent required</html>', profile().replace('gsc_rsb_std', 'changed'),
                     profile(('-', 0, 0, 0, 0, 0)), profile().replace('h-index', 'unexpected')):
            with self.subTest(html=html), self.assertRaises(ScholarError):
                parse_profile(html, 'test')

    def test_captcha_is_rejected(self):
        with self.assertRaisesRegex(ScholarError, 'CAPTCHA'):
            parse_profile('<form id="captcha-form"></form>' + profile(), 'test')

    def test_valid_fetch_is_one_request_and_generates_success_timestamp(self):
        client = Mock()
        client.get.return_value = response()
        data = fetch_profile('test', client)
        self.assertEqual(client.get.call_count, 1)
        self.assertIn('updated', data)
        self.assertEqual(client.get.call_args.kwargs['timeout'], (10, 20))

    def test_blocked_responses_fail_without_retry(self):
        for code in (403, 429):
            client = Mock()
            client.get.return_value = response(status=code)
            with self.assertRaisesRegex(ScholarError, str(code)):
                fetch_profile('test', client)
            self.assertEqual(client.get.call_count, 1)

    @patch('main.time.sleep')
    def test_network_timeouts_are_bounded(self, sleep):
        client = Mock()
        client.get.side_effect = requests.Timeout()
        with self.assertRaises(ScholarError):
            fetch_profile('test', client)
        self.assertEqual(client.get.call_count, 2)
        sleep.assert_called_once_with(5)

    def test_redirect_to_different_profile_is_rejected(self):
        client = Mock()
        client.get.return_value = response(url='https://scholar.google.com/citations?user=other')
        with self.assertRaises(ScholarError):
            fetch_profile('test', client)

    def test_invalid_id_is_rejected_before_request(self):
        client = Mock()
        with self.assertRaises(ScholarError):
            fetch_profile('https://example.com/', client)
        client.get.assert_not_called()

    def test_output_contract_matches_homepage(self):
        with tempfile.TemporaryDirectory() as directory:
            data = dict(parse_profile(profile(), 'test'), updated='2026-09-24T00:00:00+00:00')
            write_results(data, Path(directory))
            saved = json.loads((Path(directory)/'gs_data.json').read_text())
            self.assertEqual(saved, data)
            badge = json.loads((Path(directory)/'gs_data_shieldsio.json').read_text())
            self.assertEqual(badge['message'], '62')

    def test_failed_run_preserves_previous_file_and_timestamp(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'gs_data.json'
            old = '{"citedby":60,"hindex":4,"updated":"2026-09-22"}'
            path.write_text(old)
            with patch.dict('os.environ', {'GOOGLE_SCHOLAR_ID': 'test'}), \
                 patch('sys.argv', ['main.py', '--output-dir', directory]), \
                 patch('main.fetch_profile', side_effect=ScholarError('blocked')):
                self.assertEqual(main(), 1)
            self.assertEqual(path.read_text(), old)


if __name__ == '__main__':
    unittest.main()
