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

<div class="lang-en" markdown="1">

Hi! I am Hairong Shi (史海容). I am a first-year Master's student in Computer Science at [Keio University](https://www.keio.ac.jp/), where I am fortunate to be supervised by Professor Komei Sugiura. My research interests lie in **Vision-Language Model** and **Computer Vision**. <a href='https://scholar.google.com/citations?user=bgb9UpgAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>

I am a member of [SMILAB@Keio University](https://smilab.org/) since September 2025. I received my Bachelor's degree in Biomedical Engineering from the [School of Biological Science and Medical Engineering](https://bme.buaa.edu.cn/) at [Beihang University](https://ev.buaa.edu.cn/). During my undergraduate studies, I had the privilege of working as a Research Assistant for two years at [Colab@Beihang](https://colalab.net/) with Professor Si Liu. I have also gained industry experience as an AIGC Research Intern at [RightBrain.AI](https://rightbrainai.cn/home).

</div>

<div class="lang-ja" markdown="1">

こんにちは。史海容（Hairong Shi）です。現在、[慶應義塾大学](https://www.keio.ac.jp/)で杉浦孔明教授のご指導のもと、情報理工学専攻の修士1年です。研究分野は **Vision-Language Model** と **Computer Vision** です。 <a href='https://scholar.google.com/citations?user=bgb9UpgAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>

2025年9月より [SMILAB@Keio University](https://smilab.org/) に所属しています。[北京航空航天大学](https://ev.buaa.edu.cn/) [生物医学工程学院](https://bme.buaa.edu.cn/) で生体医工学の学士号を取得しました。学部在学中は、Si Liu 教授のもと [Colab@Beihang](https://colalab.net/) で2年間リサーチアシスタントとして研究に従事しました。また、[RightBrain.AI](https://rightbrainai.cn/home) で AIGC リサーチインターンとしての産業経験もあります。

</div>

<span class='anchor' id='news'></span>

# 🔥 <span class="lang-en-inline">News</span><span class="lang-ja-inline">ニュース</span>

<div class="lang-en" markdown="1">

- *2026.06*: &nbsp;🎉🎉 Our paper "Grounding What Users Mean" was accepted to **MIRU 2026 (第29回 画像の認識・理解シンポジウム)** as an **Oral Presentation** (Acceptance Rate: 33.5%)!
- *2026.05*: &nbsp;🎉🎉 One paper was **Early Accepted** to **MICCAI 2026** (Top 9%)!
- *2025.03*: &nbsp;🎉🎉 Started my AIGC Research Internship at RightBrain.AI.
- *2024.12*: &nbsp;🎉🎉 Our paper "VideoEspresso" was accepted to **CVPR 2025** as an **Oral presentation** (Top 0.7%)!
- *2024.06*: &nbsp;🎉🎉 Our paper "Mask-Enhanced Segment Anything Model" was accepted to **MICCAI 2024**!

</div>

<div class="lang-ja" markdown="1">

- *2026.06*: &nbsp;🎉🎉 論文 "Grounding What Users Mean" が **MIRU 2026 (第29回 画像の認識・理解シンポジウム)** に **口頭発表** として採択されました（採択率: 33.5%）!
- *2026.05*: &nbsp;🎉🎉 論文1編が **MICCAI 2026** に **Early Accept** として採択されました（Top 9%）!
- *2025.03*: &nbsp;🎉🎉 RightBrain.AI で AIGC リサーチインターンを開始しました。
- *2024.12*: &nbsp;🎉🎉 論文 "VideoEspresso" が **CVPR 2025** に **口頭発表** として採択されました（Top 0.7%）!
- *2024.06*: &nbsp;🎉🎉 論文 "Mask-Enhanced Segment Anything Model" が **MICCAI 2024** に採択されました!

</div>

<span class='anchor' id='publications'></span>

# 📝 <span class="lang-en-inline">Publications</span><span class="lang-ja-inline">研究実績</span>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MIRU 2026</div><img src='images/miru.png' alt="Intent-R1" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<div class="lang-en" markdown="1">

Grounding What Users Mean: Open-Vocabulary Intention-Guided Object Detection in Diverse Scenes

**Hairong Shi**, 杉浦孔明

**MIRU 2026 (第29回 画像の認識・理解シンポジウム) Oral Presentation (Acceptance Rate: 33.5%)**

</div>

<div class="lang-ja" markdown="1">

Grounding What Users Mean: Open-Vocabulary Intention-Guided Object Detection in Diverse Scenes

**Hairong Shi**, 杉浦孔明

**MIRU 2026 (第29回 画像の認識・理解シンポジウム) 口頭発表（採択率: 33.5%）**

</div>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MICCAI 2026</div><img src='images/medvolr1.png' alt="MedVol-R1" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<div class="lang-en" markdown="1">

MedVol-R1: Reward-Driven Evidence Grounding for Volumetric Reasoning Segmentation

Zichun Wang<sup>†</sup>, **Hairong Shi**<sup>†</sup>, Zihua Wang, Bingzheng Wei, Yan Xu

<sup>†</sup>Equal Contribution | **MICCAI 2026 Early Accept (Top 9%)**

</div>

<div class="lang-ja" markdown="1">

MedVol-R1: Reward-Driven Evidence Grounding for Volumetric Reasoning Segmentation

Zichun Wang<sup>†</sup>, **Hairong Shi**<sup>†</sup>, Zihua Wang, Bingzheng Wei, Yan Xu

<sup>†</sup>Equal Contribution | **MICCAI 2026 Early Accept (Top 9%)**

</div>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2025</div><img src='images/videoespresso.png' alt="VideoEspresso" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<div class="lang-en" markdown="1">

[VideoEspresso: A Large-Scale Chain-of-Thought Dataset for Fine-Grained Video Reasoning via Core Frame Selection](https://github.com/hshjerry/VideoEspresso)

Songhao Han, Wei Huang, **Hairong Shi**, Le Zhuo, Xiu Su, Shifeng Zhang, Xu Zhou, Xiaojuan Qi, Yue Liao, Si Liu

[**Project**](https://github.com/hshjerry/VideoEspresso) | [**Paper**](https://openaccess.thecvf.com/content/CVPR2025/html/Han_VideoEspresso_A_Large-Scale_Chain-of-Thought_Dataset_for_Fine-Grained_Video_Reasoning_via_CVPR_2025_paper.html) | **CVPR 2025 Oral Presentation (Top 0.7%)**

</div>

<div class="lang-ja" markdown="1">

[VideoEspresso: A Large-Scale Chain-of-Thought Dataset for Fine-Grained Video Reasoning via Core Frame Selection](https://github.com/hshjerry/VideoEspresso)

Songhao Han, Wei Huang, **Hairong Shi**, Le Zhuo, Xiu Su, Shifeng Zhang, Xu Zhou, Xiaojuan Qi, Yue Liao, Si Liu

[**Project**](https://github.com/hshjerry/VideoEspresso) | [**Paper**](https://openaccess.thecvf.com/content/CVPR2025/html/Han_VideoEspresso_A_Large-Scale_Chain-of-Thought_Dataset_for_Fine-Grained_Video_Reasoning_via_CVPR_2025_paper.html) | **CVPR 2025 口頭発表（Top 0.7%）**

</div>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MICCAI 2024</div><img src='images/msam.png' alt="M-SAM" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<div class="lang-en" markdown="1">

[Mask-Enhanced Segment Anything Model for Tumor Lesion Semantic Segmentation](https://papers.miccai.org/miccai-2024/paper/0762_paper.pdf)

**Hairong Shi**, Songhao Han, Shaofei Huang, Yue Liao, Guanbin Li, Xiangxing Kong, Hua Zhu, Xiaomu Wang, Si Liu

[**Project**](https://github.com/nanase1025/M-SAM) | [**Paper**](https://papers.miccai.org/miccai-2024/paper/0762_paper.pdf) | **MICCAI 2024 Poster (Acceptance Rate: 31%)**

</div>

<div class="lang-ja" markdown="1">

[Mask-Enhanced Segment Anything Model for Tumor Lesion Semantic Segmentation](https://papers.miccai.org/miccai-2024/paper/0762_paper.pdf)

**Hairong Shi**, Songhao Han, Shaofei Huang, Yue Liao, Guanbin Li, Xiangxing Kong, Hua Zhu, Xiaomu Wang, Si Liu

[**Project**](https://github.com/nanase1025/M-SAM) | [**Paper**](https://papers.miccai.org/miccai-2024/paper/0762_paper.pdf) | **MICCAI 2024 ポスター（採択率: 31%）**

</div>
</div>
</div>

<span class='anchor' id='honors'></span>

# 🎖 <span class="lang-en-inline">Honors and Awards</span><span class="lang-ja-inline">受賞・奨学金</span>

<div class="lang-en" markdown="1">

- *2025.11* **2025 Academic Year Monbukagakusho Honors Scholarship**, JASSO for Privately Financed International Students
- *2025.06* **Outstanding Graduate Prize**, Beihang University
- *2024.06* **Academic Excellence Scholarship (Second Prize)**, Beihang University
- *2023.10* **Voyage Program Scholarship**, Beihang University
- *2023.06* **Academic Excellence Scholarship (Second Prize)**, Beihang University
- *2022.06* **Academic Excellence Scholarship (First Prize)**, Beihang University

</div>

<div class="lang-ja" markdown="1">

- *2025.11* **2025年度 文部科学省外国人留学生学習奨励費**, JASSO
- *2025.06* **優秀卒業生賞**, 北京航空航天大学
- *2024.06* **学業優秀奨学金（二等）**, 北京航空航天大学
- *2023.10* **Voyage Program Scholarship**, 北京航空航天大学
- *2023.06* **学業優秀奨学金（二等）**, 北京航空航天大学
- *2022.06* **学業優秀奨学金（一等）**, 北京航空航天大学

</div>

<span class='anchor' id='education'></span>

# 📖 <span class="lang-en-inline">Education</span><span class="lang-ja-inline">学歴</span>

<div class="lang-en" markdown="1">

- *2025.09 - 2027.09*, **Master of Computer Science**, Keio University, Japan
- *2021.09 - 2025.06*, **Bachelor of Biomedical Engineering** (Medical Artificial Intelligence), Beihang University, China
  - GPA: 3.78/4.0 (Top 5%), Rank: 4/72

</div>

<div class="lang-ja" markdown="1">

- *2025.09 - 2027.09*, **修士（情報理工学専攻）**, 慶應義塾大学, 日本
- *2021.09 - 2025.06*, **学士（生体医工学・医療人工知能）**, 北京航空航天大学, 中国
  - GPA: 3.78/4.0（上位5%）, 順位: 4/72

</div>

<span class='anchor' id='research-experience'></span>

# 🔬 <span class="lang-en-inline">Research Experience</span><span class="lang-ja-inline">研究経験</span>

<div class="lang-en" markdown="1">

- *2023.09 - 2025.03*, **Research Assistant**, Colab@Beihang, supervised by Prof. Si Liu
  - Focused on video understanding and medical image segmentation. Contributed to the "VideoEspresso" and "M-SAM" projects, leading to publications at CVPR and MICCAI.
- *2023.04 - 2023.07*, **Research Assistant**, Beihang University, supervised by A.P. Guanglei Zhang
  - Conducted research on Medical Computer Vision

</div>

<div class="lang-ja" markdown="1">

- *2023.09 - 2025.03*, **リサーチアシスタント**, Colab@Beihang, 指導教員: Si Liu 教授
  - 動画理解と医用画像セグメンテーションに関する研究に従事しました。"VideoEspresso" と "M-SAM" プロジェクトに貢献し、CVPR および MICCAI での発表につながりました。
- *2023.04 - 2023.07*, **リサーチアシスタント**, 北京航空航天大学, 指導教員: A.P. Guanglei Zhang
  - 医用コンピュータビジョンに関する研究に従事しました。

</div>

<span class='anchor' id='internships'></span>

# 💻 <span class="lang-en-inline">Internships</span><span class="lang-ja-inline">インターンシップ</span>

<div class="lang-en" markdown="1">

- *2025.03 - 2025.07*, **AIGC Research Intern**, RightBrain.AI, Beijing, China
  - Developed and experimented with generative models for lipsync, video generation agent.
- *2024.07 - 2024.09*, **Medical MLLM Research Intern**, United Imaging Intelligence, Beijing, China
  - Contributed to the development of a Multimodal Large Language Model for Medical MLLM.

</div>

<div class="lang-ja" markdown="1">

- *2025.03 - 2025.07*, **AIGC リサーチインターン**, RightBrain.AI, 北京, 中国
  - リップシンクおよび動画生成エージェント向けの生成モデルの開発と実験に従事しました。
- *2024.07 - 2024.09*, **医療 MLLM リサーチインターン**, United Imaging Intelligence, 北京, 中国
  - 医療 MLLM のためのマルチモーダル大規模言語モデルの開発に貢献しました。

</div>

<span class='anchor' id='skills'></span>

# 💪 <span class="lang-en-inline">Skills</span><span class="lang-ja-inline">スキル</span>

<div class="lang-en" markdown="1">

- **Programming**: Python (PyTorch, Hugging Face Transformers, timm), C++
- **Languages**:
  - Mandarin Chinese (Native)
  - English (IELTS: 7.0)
  - Japanese (JLPT N2)

</div>

<div class="lang-ja" markdown="1">

- **プログラミング**: Python (PyTorch, Hugging Face Transformers, timm), C++
- **言語**:
  - 中国語（母語）
  - 英語（IELTS: 7.0）
  - 日本語（JLPT N2）

</div>

<span class='anchor' id='contact'></span>

# 📧 <span class="lang-en-inline">Contact</span><span class="lang-ja-inline">連絡先</span>

<div class="lang-en" markdown="1">

- **Email**: shihr1025@gmail.com (Primary), shihr@keio.jp
- **GitHub**: [https://github.com/nanase1025](https://github.com/nanase1025)

</div>

<div class="lang-ja" markdown="1">

- **メール**: shihr1025@gmail.com（Primary）, shihr@keio.jp
- **GitHub**: [https://github.com/nanase1025](https://github.com/nanase1025)

</div>
