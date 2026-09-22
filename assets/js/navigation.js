document.addEventListener('DOMContentLoaded', function () {
  const links = Array.from(document.querySelectorAll('.site-topbar__links a'));
  const sections = links.map(function (link) {
    return document.getElementById(link.hash.slice(1));
  });
  let scheduled = false;

  function updateCurrentSection() {
    const boundary = document.querySelector('.site-topbar').getBoundingClientRect().bottom + 40;
    let current = 0;
    sections.forEach(function (section, index) {
      if (section && section.getBoundingClientRect().top <= boundary) current = index;
    });
    links.forEach(function (link, index) {
      if (index === current) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    scheduled = false;
  }

  function scheduleUpdate() {
    if (!scheduled) {
      scheduled = true;
      window.requestAnimationFrame(updateCurrentSection);
    }
  }

  window.addEventListener('scroll', scheduleUpdate, { passive: true });
  window.addEventListener('resize', scheduleUpdate);
  updateCurrentSection();
});
