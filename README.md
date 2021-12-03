# UAV-Human

**Official repository for CVPR2021: UAV-Human: A Large Benchmark for Human Behavior Understanding with Unmanned Aerial Vehicles**

![](imgs/samples.png)

## Paper

[[CVF OpenAccess](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_UAV-Human_A_Large_Benchmark_for_Human_Behavior_Understanding_With_Unmanned_CVPR_2021_paper.pdf)] [[arXiv](https://arxiv.org/abs/2104.00946)] [[ResearchGate](https://www.researchgate.net/publication/350558689_UAV-Human_A_Large_Benchmark_for_Human_Behavior_Understanding_with_Unmanned_Aerial_Vehicles)]

## Dataset Download

The dataset is available for [Download](https://sutdcv.github.io/uav-human-web/) now!

**FAQs:**

**Q1:** Is my competition result in MMVRAC comparable with the results reported in your original paper?

**A1:** No. During our ICCVW2021 MMVRAC competition, only part of the testing data is released, and therefore the result obtained in the MMVRAC competition is **NOT** comparable with the results reported in our paper. If you try to publish an academic paper on our benchmark, please follow the above [link](https://sutdcv.github.io/uav-human-web/) and download the whole released dataset.

**Q2:** Which identity should I use to train my ReID model, the person ID or the setup ID?

**A2:** We have provided person IDs and setup IDs.

In our original paper, we concatenated the person IDs and subject IDs as the identities to train our model. However, we provide person ID and setup ID to give more choices for you to train and evaluate your own models. 

<!-- with the purpose of providing 2 research evaluation protocol - appearance id -->

Also note that we obtained consent forms from all captured subjects. 

**Q3:** In your ReID dataset, is it the case that you combined the subject ids with the setup ids to obtain 1,144 identities?

**A3:** Yes. In order to publish our ReID dataset to the public, we have to obtain the consent forms from all the captured subjects, and then we are allowed to distribute the videos containing the captured subjects to the community.

## Action Classes

The UAV-Human dataset contains 155 action classes, and the action categories are list below:

* A000: drink
* A001: eat snacks
* A002: brush hair 
* A003: drop something
* A004: pick up something
* A005: throw away something
* A006: sit down
* A007: stand up
* A008: applaud 
* A009: read 
* A010: write
* A011: put on a coat
* A012: take off a coat
* A013: put on glasses
* A014: take off glasses
* A015: put on a hat
* A016: take off a hat
* A017: throw away a hat
* A018: cheer
* A019: wave hands
* A020: kick something
* A021: reach into pockets
* A022: jump on single leg
* A023: jump on two legs
* A024: make a phone call
* A025: play with cell phones
* A026: point somewhere
* A027: look at the watch
* A028: rub hands
* A029: bow
* A030: shake head
* A031: salute
* A032: cross palms together
* A033: cross arms in front to say no
* A034: wear headphones
* A035: take off headphones
* A036: make a shh sign
* A037: touch the hair
* A038: thumb up
* A039: thumb down
* A040: make an OK sign
* A041: make a victory sign
* A042: punch with fists
* A043: figure snap
* A044: open the bottle
* A045: smell
* A046: squat
* A047: apply cream to face
* A048: apply cream to hands
* A049: grasp a bag
* A050: put down a bag
* A051: put something into a bag
* A052: take something out of a bag
* A053: open a box
* A054: move a box
* A055: put up hands
* A056: put hands on hips
* A057: wrap arms around
* A058: shake arms
* A059: step on the spot walk
* A060: kick aside
* A061: kick backward
* A062: cough
* A063: sneeze
* A064: yawn
* A065: blow nose
* A066: stagger
* A067: headache
* A068: chest discomfort
* A069: backache
* A070: neck-ache
* A071: vomit
* A072: use a fan
* A073: stretch body
* A074: punching someone
* A075: kicking someone
* A076: pushing someone
* A077: slap someone on the back
* A078: point someone
* A079: hug
* A080: give something to someone
* A081: steal something from other’s pocket
* A082: rob something from someone
* A083: shake hands
* A084: walk toward someone
* A085: walk away from someone
* A086: hit someone with something
* A087: threat some with a knife
* A088: bump into someone
* A089: walk side by side
* A090: high five
* A091: drink a toast
* A092: move something with someone
* A093: take a phone for someone
* A094: stalk someone
* A095: whisper in someone’s ear
* A096: exchange something with someone
* A097: lend an arm to support someone
* A098: rock-paper-scissors
* A099: hover
* A100: land
* A101: land at designated locations
* A102: move forward
* A103: move backward
* A104: move left
* A105: move right
* A106: ascend
* A107: descend
* A108: accelerate
* A109: decelerate
* A110: come over here
* A111: stay where you are
* A112: rear right turn
* A113: rear left turn
* A114: abandon landing
* A115: all clear
* A116: not clear
* A117: have command
* A118: follow me
* A119: turn left 
* A120: turn right
* A121: throw litter
* A122: dig a hole
* A123: mow
* A124: set on fire
* A125: smoke
* A126: cut the tree
* A127: fishing
* A128: pick a lock
* A129: pollute walls
* A130: hold someone hostage
* A131: threat someone with a gun
* A132: wave a goodbye
* A133: chase someone
* A134: comfort someone
* A135: drag someone
* A136: sweep the floor
* A137: mop the floor
* A138: bounce the ball
* A139: shoot at the basket
* A140: swing the racket
* A141: leg pressing
* A142: escape (to survive)
* A143: call for help
* A144: wear a mask
* A145: take off a mask
* A146: bend arms around someone’s shoulder
* A147: run
* A148: stab someone with a knife
* A149: throw a frisbee
* A150: carry a carrying pole
* A151: use a lever to lift something
* A152: walk
* A153: open an umbrella
* A154: close an umbrella


## Annotations

VideoNames: **P**070**S**01**G**10**B**00**H**10**UC**102000**LC**092000**A**031**R**0\_**09131758**.avi

**P**070: (**P**ersonID) unique person ID for the main subject in current video

**S**01: (**S**etupID) setup id that indicates changes of clothing, hat, backpack of the main subject

**G**10: (**G**ender) first bit represents main subject's gender, second bit represents auxiliary subject's gender

`0: n/a; 1: male; 2: female`

**B**00: (**B**ackpack) first bit represents main subject's backpack color, second bit represents auxiliary subject's backpack color

`0: n/a; 1: red; 2: black; 3: green; 4: yellow; 5: n/a`

**H**10: (**H**at) first bit represents main subject's hat color, second bit represents auxiliary subject's hat color

`0: n/a; 1: red; 2: black; 3: yellow; 4: white; 5: n/a`

**UC**102000: (**U**pper**C**lothing) first three bits represent main subject's upper clothing color (2 bits) and style (1 bit), last three bits represent auxiliary subject's upper clothing color (2 bits) and style (1 bit)

`color: 0: n/a; 1: red; 2: black; 3: blue; 4: green; 5: multicolor; 6: grey; 7: white; 8: yellow; 9: dark brown; 10: purple; 11: pink`

`style: 0: n/a; 1: long; 2: short; 3: skirt`

**LC**102000: (**L**ower**C**lothing) first three bits are main subject's lower clothing color (2 bits) and style (1 bit), last three bits are auxiliary subject's lower clothing color (2 bits) and style (1 bit)

`color: 0: n/a; 1: red; 2: black; 3: blue; 4: green; 5: multicolor; 6: grey; 7: white; 8: yellow; 9: dark brown; 10: purple; 11: pink`

`style: 0: n/a; 1: long; 2: short; 3: skirt`

**A**031: (**A**ction) action labels of current sample

**R**00: (**R**eplicate) replicate capturing

09131758: capturing timestamp, month(2 bits)/day(2 bits)/hour(2 bits)/minute(2 bits)

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

## Action Recognition Evaluation Protocols

### Cross-Subject-v1

In cross-subject-v1 evaluation, we split 119 subjects into training and testing groups. The IDs of training subjects are 0, 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 59, 61, 62, 63, 64, 65, 67, 68, 69, 70, 71, 73, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 98, 100, 102, 103, 105, 106, 110, 111, 112, 114, 115, 116, 117, 118; the remaining subjects are for testing.

### Cross-Subject-v2

In cross-subject-v2 evaluation, we split 119 subjects into training and testing groups. The IDs of training subjects are 0, 3, 4, 5, 6, 8, 10, 11, 12, 14, 16, 18, 19, 20, 21, 22, 24, 26, 29, 30, 31, 32, 35, 36, 37, 38, 39, 40, 43, 44, 45, 46, 47, 49, 52, 54, 56, 57, 59, 60, 61, 62, 63, 64, 66, 67, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 99, 100, 101, 102, 103, 104, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 117, 118; the remaining subjects are for testing.

### Results

#### Evaluation on I3D

| Modality      | CSv1 - Acc (%) | CSv2 - Acc (%) |
| ------------- | -------------- | -------------- |
| RGB Video     | 23.86          | 29.53          |
| Fisheye Video | 20.76          | 34.12          |

#### Evaluation on skeleton

| Methods   | CSv1 - Acc (%) | CSv2 - Acc (%) |
| --------- | -------------- | -------------- |
| DGNN      | 29.90          | -              |
| ST-GCN    | 30.25          | 56.14          |
| 2s-AGCN   | 34.84          | 66.68          |
| HARD-Net  | 36.97          | -              |
| Shift-GCN | 37.98          | 67.04          |
<!-- MS-G3D | -              | 69.87          | -->

## Video Processing Guidance

Please refer to [utils/convert_videos_to_frames.py](utils/convert_videos_to_frames.py) and following:

`python convert_videos_to_frames.py --videos path/to/all/videos --frames path/to/output/frames`

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
