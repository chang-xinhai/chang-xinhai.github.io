---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am an undergraduate student at [Yuanpei College](https://yuanpei.pku.edu.cn/en/), [Peking University (PKU)]([https://www.pku.edu.cn/](https://english.pku.edu.cn/)). I am advised by Prof. [Yixin Zhu](https://yzhu.io/) at [Core Lab](https://pku.ai/). I am also working on research under the guidance of [Kaichen Zhou](https://wang.hms.harvard.edu/team/kaichen-zhou-phd/) from the Harvard AI and Robotics Lab.

My research passion lies in embodied AI, with a focus on mobile manipulation and 3D reconstruction. I aim to build digital twins that seamlessly fuse the virtual and physical worlds by harnessing large-scale parallel simulation, ultimately creating general-purpose robotic models that can both perceive and reconstruct. I'm always eager to explore fresh ideas and collaborations—let's connect!

In addition to my research, I am an amateur photographer and motorcyclist. Love for life and the savor of freedom lingers without a moment’s lapse.

# 🔥 News
- *2025.06*: &nbsp;🎉🎉 [PAGE-4D](https://arxiv.org/abs/2510.17568) is accepted by ICLR 2026!
- *2025.06*: &nbsp;🎉🎉 [AutoMoMa](https://openreview.net/pdf?id=mi766Y2K6Y) is accepted by RSS 2025 MoMa!
- *2025.06*: &nbsp;🎉🎉 [TerraX](http://poss.pku.edu.cn/terrax.html) is accepted by IROS 2025 as **Oral**!
- *2025.02*: &nbsp;🎉🎉 [SplatMesh](https://arxiv.org/abs/2312.15856) is accepted by CVPRW 2025!
 <!-- - *2025.07*: &nbsp;🎉🎉 [AADNet]() is accepted by SMC 2025! -->
 <!-- - *2025.04*: &nbsp;🎉🎉 [StyleCraft](https://doi.org/10.1007/978-981-96-9866-0_20) is accepted by ICIC 2025! -->

# 📝 Publications 

<!-- RAD -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='images/papers/RAD.png' alt="RAD" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[RAD: A Realistic Multi-View Benchmark for Pose-Agnostic Anomaly Detection](https://arxiv.org/abs/2410.00713v3)

[Kaichen Zhou](https://wang.hms.harvard.edu/team/kaichen-zhou-phd/)\*, [**Xinhai Chang**](https://chang-xinhai.github.io/)\*, [Taewhan Kim](https://scholar.google.com/citations?user=aQTkWjQAAAAJ&hl=en)\*, Jiadong Zhang\*, Yang Cao, Chufei Peng, [Fangneng Zhan](https://fnzhan.com/), Hao Zhao, [Hao Dong](https://zsdonghao.github.io/), Kai Ming Ting, [Ye Zhu](https://experts.deakin.edu.au/41905-ye-zhu)

[**Paper**](https://arxiv.org/abs/2410.00713v3)
<!-- |
[**Project**](https://github.com/kaichen-z/rad)-->
|
[**Code**](https://github.com/kaichen-z/rad) 

- RAD (Realistic Anomaly Detection) is a robot-captured, multi-view dataset designed to address the challenges of pose variation, reflective materials, and viewpoint-dependent defect visibility. It provides a benchmark for pose-agnostic anomaly detection across 13 object categories under uncontrolled lighting conditions.

</div>
</div>


<!-- PAGE-4D -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/papers/PAGE_4D.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[PAGE-4D: Disentangled Pose and Geometry Estimation for 4D Perception](https://page-4d.github.io/anonymous-submission/)

[Kaichen Zhou](https://wang.hms.harvard.edu/team/kaichen-zhou-phd/)\*, [Yuhan Wang](https://scholar.google.com/citations?user=gYhZ614AAAAJ&hl=en)\*, [Grace Chen](https://wang.hms.harvard.edu/team/grace-chen/)\*, [**Xinhai Chang**](https://chang-xinhai.github.io/), [Gaspard Beaudouin](https://wang.hms.harvard.edu/team/gaspard-beaudouin/), [Fangneng Zhan](https://fnzhan.com/), [Paul Pu Liang](https://pliang279.github.io/), [Mengyu Wang](https://wang.hms.harvard.edu/team/dr-wang/)

[**Paper**](https://arxiv.org/abs/2510.17568)
|
[**Project**](https://page-4d.github.io/anonymous-submission/)
|
[**Code**](https://drive.google.com/file/d/1caBtmWK8I-t6RyG2gAsUjSLWM0dl_1kh/view?usp=drive_link)

- PAGE-4D is a feedforward 4D perception model that disentangles static and dynamic scene elements to simultaneously achieve accurate camera pose estimation, depth prediction, and point cloud reconstruction in dynamic environments.

</div>
</div>

<!-- AutoMoMa -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">RSS 2025 Workshop</div><img src='images/papers/AutoMoMa.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[A Scalable Whole-body Trajectory Generator for Coordinated Mobile Manipulation](https://page-4d.github.io/anonymous-submission/)

[Yida Niu](https://github.com/fi6)\*, [**Xinhai Chang**](https://chang-xinhai.github.io/)\*, [Xin Liu](https://openreview.net/profile?id=~Xin_Liu72)\*, [Ziyuan Jiao](https://sites.google.com/g.ucla.edu/zyjiao/home), [Yixin Zhu](https://yzhu.io/)

[**Paper**](https://openreview.net/pdf?id=mi766Y2K6Y)
|
[**Project**](https://automoma.pages.dev/)
<!-- | -->
<!-- [**Code**]() -->

- AutoMoMa is a system that efficiently generates high-quality whole-body trajectories using Virtual Kinematic Chain (VKC) modeling and GPU-accelerated motion planning at a rate of 2.5k valid episodes per hour per consumer-level GPU, which generalizes across diverse household layouts, interactive objects, robot morphologies, and manipulation tasks while ensuring physical feasibility and strict constraint satisfaction.

</div>
</div>

<!-- TerraX -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IROS 2025 Oral</div><img src='images/papers/TerraX.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[TerraX: Visual Terrain Classification Enhanced by Vision-Language Models](http://poss.pku.edu.cn/terrax.html)
  
[Hongze Li](https://lhz1016.github.io/)\*, [Xuchuan Huang](https://huangxuchuan.github.io/)\*, [**Xinhai Chang**](https://chang-xinhai.github.io/)\*, Jun Zhou, [Huijing Zhao](http://poss.pku.edu.cn/members/zhaohj/index.htm)

[**Paper**](https://ieeexplore.ieee.org/document/11246334)
|
[**Project**](http://poss.pku.edu.cn/terrax.html)
|
[**Code**](http://poss.pku.edu.cn/OpenDataResource/TerraX/code.zip)

- TerraX is a vision-language framework for terrain classification, featuring the TerraData dataset, TerraBench benchmark, and TerraCLIP model.


</div>
</div>


<!-- EpiS -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='images/papers/EpiS.png' alt="EpiS" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Neural Surface Reconstruction from Sparse Views Using Epipolar Geometry](https://arxiv.org/abs/2406.04301)

[**Xinhai Chang**](https://chang-xinhai.github.io/), [Kaichen Zhou](https://wang.hms.harvard.edu/team/kaichen-zhou-phd/)

[**Paper**](https://arxiv.org/abs/2406.04301)
<!-- |
[**Project**]() -->
<!-- | -->
<!-- [**Code**]() -->

- EpiS is a generalizable neural surface reconstruction framework that explicitly leverages epipolar geometry. By using an epipolar transformer to fuse multi-view information and incorporating a pretrained monocular depth model for geometry regularization, EpiS achieves state-of-the-art performance in sparse-view surface estimation without per-scene optimization.

</div>
</div>


<!-- SplatMesh -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPRW 2025</div><img src='images/papers/SplatMesh.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[SplatMesh: Interactive 3D Segmentation and Editing Using Mesh-Based Gaussian Splatting](https://arxiv.org/abs/2312.15856)
  
[Kaichen Zhou](https://wang.hms.harvard.edu/team/kaichen-zhou-phd/)\*, [Lanqing Hong](https://racheltechie.github.io/)\*, [**Xinhai Chang**](https://chang-xinhai.github.io/)\*, [Yingji Zhong](https://openreview.net/profile?id=~Yingji_Zhong1), [Enze Xie](https://xieenze.github.io/), [Hao Dong](https://zsdonghao.github.io/), Zhihao Li, [Yongxin Yang](https://yang.ac/), [Zhenguo Li](https://www.ee.columbia.edu/~zgli/), [Wei Zhang](https://openreview.net/profile?id=~Wei_Zhang45)

[**Paper**](https://arxiv.org/abs/2312.15856)
<!-- | -->
<!-- [**Project**]() -->
|
[**Code**](https://github.com/kaichen-z/SplatMesh)

- SplatMesh is a novel fine-grained interactive 3D segmentation and editing algorithm that integrates 3D Gaussian Splat with a precomputed mesh and could adjust the memory request based on the requirement. 

</div>
</div>

<!-- AADNet -->
<div style="display:none">
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">SMC 2025</div><img src='images/papers/AADNet.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[AADNet: A Human-Mind-Inspired Multi-Modal Framework for Object Concept Learning]()
  
Chao Tang\*, **Xinhai Chang**\*

</div>
</div>
</div>

<!-- StyleCraft -->
<div style="display:none">
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICIC2025 Oral</div><img src='images/papers/StyleCraft.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[StyleCraft: High-Quality Arbitrary Style Transfer via Unified Content-Style Fusion](https://doi.org/10.1007/978-981-96-9866-0_20)
  
Chao Tang\*, **Xinhai Chang**\*

[**Paper**](https://doi.org/10.1007/978-981-96-9866-0_20)

</div>
</div>
</div>




# 🎖 Honors and Awards
- *2025* **National Scholarship**
- *2024* Second-class Scholarship, Peking University
- *2024* **First Prize**, 21st Jiang Zehan Cup Mathematical Modeling Competition
- *2023* Xing Zhengde Scholarship, Yuanpei College
- *2023* Third-class Scholarship, Peking University


# 📖 Experiences
- *2022.09 - now*, **Undergraduate Student**, Data Science and Artificial Intelligence, Peking University
- *2024.05 - 2024.08*, **Volunteer Teacher**, International Asian Liver Center, Gansu, China


# 💁 Services
- Teaching Assistant: Introduction to Computation B (Autumn 2025, by Prof. [Jun Sun](https://deepvideolab.top/))
- Teaching Assistant: Introduction to Computation C (Autumn 2025, by Prof. [Baobao Chang](https://cs.pku.edu.cn/info/1090/1648.htm))
- Teaching Assistant: Introduction to Computer System (Autumn 2024, by Prof. [Lu Zhang](https://cs.pku.edu.cn/info/1086/1729.htm))


# [📸 Photography](https://500px.com.cn/walkerch)
