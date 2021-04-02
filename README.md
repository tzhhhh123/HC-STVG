# HC-STVG
***We Update the HC-STVG2.0 Dataset, which is now used for the [PIC workshop](http://picdataset.com/challenge/task/hcvg/) in CVPR 2021.***

The HC-STVG Dataset. The duration of all videos is 20s.

## Introduction

Human-centric Spatio-Temporal Video Grounding(HC-STVG), which only focuses human in the videos. We provide 16k annotation-video paris with different movie scenes. Specifically, we annotated the description statement and all the trajectories of the corresponding person (a series of Bounding Boxes). It's worth noting that all of our clips will include multiple people to increase the challenge of video comprehension.

![](task_hcvg.jpg)

## The videos are available

HC-STVG 2.0

[One Drive](https://buaaeducn-my.sharepoint.com/:f:/g/personal/tzhhhh123_buaa_edu_cn/EgCK1QFhUypLuGMMq7unj_AB0RtzLCwPhUPXnENaJ0obew?e=ODd9S6) key <u> tzhhhh123</u>     

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