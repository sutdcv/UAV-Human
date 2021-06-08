# UAV-Human

**Official repository for CVPR2021: UAV-Human: A Large Benchmark for Human Behavior Understanding with Unmanned Aerial Vehicle**

![](imgs/samples.png)

## Paper

[arXiv](https://arxiv.org/abs/2104.00946)

[ResearchGate](https://www.researchgate.net/publication/350558689_UAV-Human_A_Large_Benchmark_for_Human_Behavior_Understanding_with_Unmanned_Aerial_Vehicles)

## Dataset
Under construction, will be available soon!

## Annotations

VideoNames: **P**070**S**01**G**10**B**00**H**10**UC**102000**LC**092000**A**031**R**0_**09131758**.avi

<!-- SkeletonFileNames: -->
<!-- **P**070**S**01**G**10**B**00**H**10**UC**102000**LC**092000**A**031**R**0_09131758.txt -->

<!-- ImageFileNames: -->
<!-- **P**070**S**01**G**10**B**00**H**10**UC**102000**LC**092000**A**031**R**0_09131758_117_bbox.jpg -->


Two-Persons Attr |Seg|Note|Description
|:-:|:-:|:-:|:-:|
| &#10005; |**P**070| Subject1 <br> Person ID | Unique person ID for each subject |
|&#10005;|**S**01| Subject1 <br> Setup ID | Setup ID when changing clothing/backpack/hat |
|&#10004;|**G**1/0| Genders  | 0 - N/A <br> 1 - Male <br>  2 - Female |
|&#10004;|**B**0/0| Backpack Color | 0 - No Backpack <br> 1 - Red, 2 - Black <br> 3 - Green, 4 - Yellow|
|&#10004;|**H**1/0| Hat Color | 0 - No Backpack <br> 1 - Red, 2 - Black <br> 3 - Yellow, 4 - White|
|&#10004;|**UC**102/000| Upper Clothing <br> Style & Color | *Style*: 0 - N/A, 1 - Long, 2 - Short, 3 - Skirt <br> *Color*: 0 - N/a, 1 - Red, 2 - Black, 3 - Blue, 4 - Green, 5 - Multicolor, 6 - Grey, 7 - White, 8 - Yellow, 9 - Dark Brown, 10 - Purple, 11 - Pink |
|&#10004;|**LC**092/000| Lower Clothing <br> Style & Color | *Style*: 0 - N/A, 1 - Long, 2 - Short, 3 - Skirt <br> *Color*: 0 - N/a, 1 - Red, 2 - Black, 3 - Blue, 4 - Green, 5 - Multicolor, 6 - Grey, 7 - White, 8 - Yellow, 9 - Dark Brown, 10 - Purple, 11 - Pink |
|&#10005;|**A**031| Action Category | Action label starting from 0 |
|&#10005;|**R**0| Replicate | Replicate capturing |
| &#10005; |09/13/17/58| Timestamp | Month/Day/Hour/Minute

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
