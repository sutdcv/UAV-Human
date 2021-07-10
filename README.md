# UAV-Human

**Official repository for CVPR2021: UAV-Human: A Large Benchmark for Human Behavior Understanding with Unmanned Aerial Vehicle**

![](imgs/samples.png)

## Paper

[arXiv](https://arxiv.org/abs/2104.00946)

[ResearchGate](https://www.researchgate.net/publication/350558689_UAV-Human_A_Large_Benchmark_for_Human_Behavior_Understanding_with_Unmanned_Aerial_Vehicles)

## Dataset
Dataset now available! [link](https://sutdapac-my.sharepoint.com/:f:/g/personal/tianjiao_li_mymail_sutd_edu_sg/EtLLkN49_C9Bq14ur0ZLpHkB-bi9Tc_LlIQBv0Ds4JE49A?e=IqX67X)

## Annotations

VideoNames: **P**070**S**01**G**10**B**00**H**10**UC**102000**LC**092000**A**031**R**0_**09131758**.avi

**P**070: Person ID for the main subject

**S**01:

<!-- SkeletonFileNames: -->
<!-- **P**070**S**01**G**10**B**00**H**10**UC**102000**LC**092000**A**031**R**0_09131758.txt -->

<!-- ImageFileNames: -->
<!-- **P**070**S**01**G**10**B**00**H**10**UC**102000**LC**092000**A**031**R**0_09131758_117_bbox.jpg -->


|Seg|Descriptions|Detailed Description
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

**Note: For Two-Persons Attr, number(s) before slash '/' represent the first person attribute and number(s) after slash '/' represent the second person attribute**



## Citation

```bibtex
@inproceedings{li2021uav,
  title={UAV-Human: A Large Benchmark for Human Behavior Understanding with Unmanned Aerial Vehicles},
  author={Li, Tianjiao and Liu, Jun and Zhang, Wei and Ni, Yun and Wang, Wenqian and Li, Zhiheng},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year={2021}
}
```

## Contact

tianjiao_li [at] mymail.sutd.edu.sg
