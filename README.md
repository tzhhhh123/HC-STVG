# HC-STVG
***We Update the HC-STVG2.0 Dataset, which is now used for the [PIC workshop](http://picdataset.com/challenge/task/hcvg/) in CVPR 2021.***

We  have added data and cleaned the labels in HC-STVG to build the **HC-STVG2.0**.

While the original database contained 5660 videos, the new database has been re-annotated and modified and now contains 16,000 + videos for this challenge.

The HC-STVG Dataset. The duration of all videos is 20s.

## Introduction

Human-centric Spatio-Temporal Video Grounding(HC-STVG), which only focuses human in the videos. We provide 16k annotation-video paris with different movie scenes. Specifically, we annotated the description statement and all the trajectories of the corresponding person (a series of Bounding Boxes). It's worth noting that all of our clips will include multiple people to increase the challenge of video comprehension.

![](task_hcvg.jpg)

## The annotations are available


annotations of train and val set.


querys of the test set.


[One Drive](https://intxyz-my.sharepoint.com/:f:/g/personal/zongheng_picdataset_com/ErqA01jikPZKnudZe6-Za9MBe17XXAxJr9ODn65Z2qGKkw?e=7vKw1U) key <u> tzhhhh123</u>     （updated）

## The videos are available

HC-STVG 2.0

[One Drive](https://intxyz-my.sharepoint.com/:f:/g/personal/zongheng_picdataset_com/ErqA01jikPZKnudZe6-Za9MBe17XXAxJr9ODn65Z2qGKkw?e=7vKw1U) key <u> tzhhhh123</u>     （updated）

[Baidu Pan](https://pan.baidu.com/s/1aSVuZzHJk5bWLXm7bfJ0Xw) key <u> tzhh</u>     （updated）

We reorganized the video data.

For new users, we divided all the videos into 10 separate packages and provided the corresponding video_part.json to represent the name of the video in each package.

For those who have already downloaded the previous ZIP file, just download the additional video in Fix. zip (which contains a small portion of the data in question). [The Fix.zip (One Drive)](https://intxyz-my.sharepoint.com/:u:/g/personal/zongheng_picdataset_com/EUaL23x9HahDhthYHfWz6FoBND5JwwIBx4_eITyC8hIfPg?e=WOhGu9)  key <u> tzhhhh123</u>.

Because part of the data has been cleaned again, the total number of videos contained in the end will be slightly less than the previous 16,685. Please don't worry, we will release the remaining data as soon as possible.

## Baseline method

A simple solution is to first locate the time of the event and then locate the target person in it.

Here are some temporal video grounding methods.

https://github.com/SCZwangxiao/Temporal-Language-Grounding-in-videos

Here are some referring expression methods.

https://github.com/TheShadow29/awesome-grounding

## Paper

https://arxiv.org/abs/2011.05049

## An example of the json file
	{  
	'55_vfjywN5CN0Y.mp4':{  
	'bbox': [[x,y,w,h], ], # the bboxes of the target person,   
	'st_time': 8.914734192388288, # ground truth start time  
	'ed_time': 17.544734192388397, # ground truth end time  
	'img_num': 600, # img_num = fps*20, we use ffmpeg to extract the images  
	 'caption': 'The woman in red clothes turns in a circle.', #caption about the target person  
	 'width': 640, #image size  
	 'height': 360, #image size  
	 'st_frame': 268} # the first frame index in the bboxes.(start with 1)  
	 ......  
	}  
