# UAV-Human

**Official repository for CVPR2021: UAV-Human: A Large Benchmark for Human Behavior Understanding with Unmanned Aerial Vehicle**

![](imgs/samples.png)

## Paper

[[CVF OpenAccess](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_UAV-Human_A_Large_Benchmark_for_Human_Behavior_Understanding_With_Unmanned_CVPR_2021_paper.pdf)] [[arXiv](https://arxiv.org/abs/2104.00946)] [[ResearchGate](https://www.researchgate.net/publication/350558689_UAV-Human_A_Large_Benchmark_for_Human_Behavior_Understanding_with_Unmanned_Aerial_Vehicles)]

## Dataset Download

The dataset is available for [Download](https://sutdcv.github.io/UAV-Human) now!

<!-- **FAQs:**

**Q1:** Is my competition result in MMVRAC comparable with the results reported in your original paper?

**A1:** No. During our ICCVW2021 MMVRAC competition, only part of the testing data is released, and therefore the result obtained in the MMVRAC competition is **NOT** comparable with the results reported in our paper. If you try to publish an academic paper on our benchmark, please follow the above [link](https://sutdapac-my.sharepoint.com/:f:/g/personal/tianjiao_li_mymail_sutd_edu_sg/EtLLkN49_C9Bq14ur0ZLpHkB-bi9Tc_LlIQBv0Ds4JE49A?e=IqX67X) and download the whole released dataset.

**Q2:** Which identity should I use to train my ReID model, the person ID or the setup ID?

**A2:** In our original paper, we combined the person IDs and subject IDs as the identities to train our model. However, we provide person ID and setup ID to give more choices for you to train and evaluate your own models.

**Q3:** In your ReID dataset, is it the case that you combined the subject ids with the setup ids to obtain 1,144 identities?

**A3:** Yes. In order to publish our ReID dataset to the public, we have to obtain the consent forms from all the captured subjects, and then we are allowed to distribute the videos containing the captured subjects to the community. -->

## Annotations

VideoNames: **P**070**S**01**G**10**B**00**H**10**UC**102000**LC**092000**A**031**R**0\_**09131758**.avi

**P**070: (**P**ersonID) unique person ID for the main subject in current video

**S**01: (**S**etupID) setup id that indicates changing of clothing, hat, backpack of the main subject

**G**10: (**G**ender) first bit is main subject's gender, second bit is auxiliary subject's gender

`0: n/a; 1: male; 2: female`

**B**00: (**B**ackpack) first bit is main subject's backpack color, second bit is auxiliary subject's backpack color

`0: n/a; 1: red; 2: black; 3: green; 4: yellow`

**H**10: (**H**at) first bit is main subject's hat color, second bit is auxiliary subject's hat color

`0: n/a; 1: red; 2: black; 3: green; 4: white`

**UC**102000: (**U**pper**C**lothing) first three bits are main subject's upper clothing color and style, last three bits are auxiliary subject's upper clothing color and style

`color: 0: n/a; 1: red; 2: black; 3: blue; 4: green; 5: multicolor; 6: grey; 7: white; 8: yellow; 9: dark brown; 10: purple; 11: pink`

`style: 0: n/a; 1: long; 2: short; 3: skirt`

**LC**102000: (**L**ower**C**lothing) first three bits are main subject's lower clothing color and style, last three bits are auxiliary subject's lower clothing color and style

`color: 0: n/a; 1: red; 2: black; 3: blue; 4: green; 5: multicolor; 6: grey; 7: white; 8: yellow; 9: dark brown; 10: purple; 11: pink`

`style: 0: n/a; 1: long; 2: short; 3: skirt`

**A**031: (**A**ction) action labels of current sample

**R**00: (**R**eplicate) replicate capturing

09131758: capturing timestamp, month/day/hour/minute

<!-- SkeletonFileNames: -->
<!-- **P**070**S**01**G**10**B**00**H**10**UC**102000**LC**092000**A**031**R**0_09131758.txt -->

<!-- ImageFileNames: -->
<!-- **P**070**S**01**G**10**B**00**H**10**UC**102000**LC**092000**A**031**R**0_09131758_117_bbox.jpg -->

<!-- |Seg|Descriptions|Detailed Description
|:-:|:-:|:-:|
|**P**070| Main Subject Person ID | Unique person ID for each subject |
|**S**01| Main Subject Setup ID | Setup ID when main subject changes clothing/backpack/hat |
|**G**10| Genders: 2bits  | 0 - N/A <br> 1 - Male <br>  2 - Female |
|**B**00| Backpack Color | 0 - No Backpack <br> 1 - Red, 2 - Black <br> 3 - Green, 4 - Yellow|
|**H**10| Hat Color | 0 - No Backpack <br> 1 - Red, 2 - Black <br> 3 - Yellow, 4 - White|
|**UC**102000| Upper Clothing <br> Style & Color | *Style*: 0 - N/A, 1 - Long, 2 - Short, 3 - Skirt <br> *Color*: 0 - N/a, 1 - Red, 2 - Black, 3 - Blue, 4 - Green, 5 - Multicolor, 6 - Grey, 7 - White, 8 - Yellow, 9 - Dark Brown, 10 - Purple, 11 - Pink |
|**LC**092000| Lower Clothing <br> Style & Color | *Style*: 0 - N/A, 1 - Long, 2 - Short, 3 - Skirt <br> *Color*: 0 - N/a, 1 - Red, 2 - Black, 3 - Blue, 4 - Green, 5 - Multicolor, 6 - Grey, 7 - White, 8 - Yellow, 9 - Dark Brown, 10 - Purple, 11 - Pink |
|**A**031| Action Category | Action label starting from 0 |
|**R**0| Replicate | Replicate capturing |
|09/13/17/58| Timestamp | Month/Day/Hour/Minute

**Note: For Two-Persons Attr, number(s) before slash '/' represent the first person attribute and number(s) after slash '/' represent the second person attribute** -->

## Citation

```bibtex
@InProceedings{Li_2021_CVPR,
    author    = {Li, Tianjiao and Liu, Jun and Zhang, Wei and Ni, Yun and Wang, Wenqian and Li, Zhiheng},
    title     = {UAV-Human: A Large Benchmark for Human Behavior Understanding With Unmanned Aerial Vehicles},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month     = {June},
    year      = {2021},
    pages     = {16266-16275}
}
```

## Contact

`tianjiao_li [at] mymail.sutd.edu.sg`
