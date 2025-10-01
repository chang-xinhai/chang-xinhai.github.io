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
- *2025.06*: &nbsp;🎉🎉 [AutoMoMa](https://openreview.net/pdf?id=mi766Y2K6Y) is accepted by RSS 2025 MoMa!
- *2025.06*: &nbsp;🎉🎉 [TerraX](http://poss.pku.edu.cn/terrax.html) is accepted by IROS 2025 as **Oral**!
- *2025.02*: &nbsp;🎉🎉 [SplatMesh](https://arxiv.org/abs/2312.15856) is accepted by CVPRW 2025!
 <!-- - *2025.07*: &nbsp;🎉🎉 [AADNet]() is accepted by SMC 2025! -->
 <!-- - *2025.04*: &nbsp;🎉🎉 [StyleCraft](https://doi.org/10.1007/978-981-96-9866-0_20) is accepted by ICIC 2025! -->

# 📝 Publications 
<!-- AutoMoMa -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">RSS2025 Workshop</div><img src='images/papers/AutoMoMa.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[A Scalable Whole-body Trajectory Generator for Coordinated Mobile Manipulation](https://openreview.net/pdf?id=mi766Y2K6Y)

[Yida Niu](https://github.com/fi6)\*, [**Xinhai Chang**](https://chang-xinhai.github.io/)\*, Xin Liu\*, [Ziyuan Jiao](https://sites.google.com/g.ucla.edu/zyjiao/home), [Yixin Zhu](https://yzhu.io/)

[**Paper**](https://openreview.net/pdf?id=mi766Y2K6Y)
|
[**Project**](https://automoma.pages.dev/)
<!-- | -->
<!-- [**Code**]() -->

- AutoMoMa is a system that efficiently generates high-quality whole-body trajectories using Virtual Kinematic Chain (VKC) modeling and GPU-accelerated motion planning at a rate of 2.5k valid episodes per hour per consumer-level GPU, which generalizes across diverse household layouts, interactive objects, robot morphologies, and manipulation tasks while ensuring physical feasibility and strict constraint satisfaction.

</div>
</div>

<!-- TerraX -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IROS2025 Oral</div><img src='images/papers/TerraX.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[TerraX: Visual Terrain Classification Enhanced by Vision-Language Models](http://poss.pku.edu.cn/terrax.html)
  
[Hongze Li](https://lhz1016.github.io/)\*, [Xuchuan Huang](https://huangxuchuan.github.io/)\*, [**Xinhai Chang**](https://chang-xinhai.github.io/)\*, Jun Zhou, [Huijing Zhao](http://poss.pku.edu.cn/members/zhaohj/index.htm)

<!-- [**Paper**]() -->
<!-- | -->
[**Project**](http://poss.pku.edu.cn/terrax.html)
<!-- | -->
<!-- [**Code**]() -->

- TerraX is a vision-language framework for terrain classification, featuring the TerraData dataset, TerraBench benchmark, and TerraCLIP model.


</div>
</div>


<!-- SplatMesh -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPRW2025</div><img src='images/papers/SplatMesh.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[SplatMesh: Interactive 3D Segmentation and Editing Using Mesh-Based Gaussian Splatting](https://arxiv.org/abs/2312.15856)
  
[Kaichen Zhou](https://github.com/kaichen-z)\*, Lanqing Hong\*, [**Xinhai Chang**](https://chang-xinhai.github.io/)\*, Yingji Zhong, Enze Xie, [Hao Dong](https://zsdonghao.github.io/), Zhihao Li, Yongxin Yang, Zhenguo Li, Wei Zhang

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
