# HC-STVG

***We are preparing the DATA based on the DATA of the PIC 3.0 challenge, where we conduct a refinement and extension. The DATA is used for the [PIC workshop](http://picdataset.com/challenge/task/hcvg/) in ACM MM 2022.***

We  have added data and cleaned the labels in HC-STVG to build the **HC-STVG2.0**.

While the original database contained 5660 videos, the new database has been re-annotated and modified and now contains 16,000 + videos for this challenge.

The HC-STVG Dataset. The duration of all videos is 20s.

## Introduction

Human-centric Spatio-Temporal Video Grounding(HC-STVG), which only focuses human in the videos. We provide 16k annotation-video paris with different movie scenes. Specifically, we annotated the description statement and all the trajectories of the corresponding person (a series of Bounding Boxes). It's worth noting that all of our clips will include multiple people to increase the challenge of video comprehension.

![](task_hcvg.jpg)

## The annotations are available

annotations of train and val set.
querys of the test set.

We manually re-annotated the noisy data, and the cleaned data was originally provided in the anno_v2 directory.

[Baidu Pan](https://pan.baidu.com/s/1myLcXN9wOs5eEdRQU4fmWw?pwd=umhs) extraction code: **umhs**

The current v2 share includes HCVG_train.json; the cleaned anno_v2 directory and separate validation/test annotations are not included.

We provide the annotations and videos for the HC-STVG v1 with 5660 videos in total [Baidu Pan](https://pan.baidu.com/s/1zTvaN293vbpScb02hp0jjQ?pwd=sv6x) extraction code: **sv6x** | [Google Drive](https://drive.google.com/file/d/1m5NhtC0JSw3p-4QJmLMcmxQvAL0NcRaM/view?usp=drive_link) （updated）

## The videos are available

HC-STVG 2.0

[Baidu Pan](https://pan.baidu.com/s/1myLcXN9wOs5eEdRQU4fmWw?pwd=umhs) extraction code: **umhs**

We divided all the videos into 10 separate packages and provided the corresponding video_parts.json to represent the name of the video in each package.

Note: The current share provides only parts 0.zip–8.zip (9 packages). 9.zip is currently unavailable, so some annotated videos are not included in the available packages.

Because part of the data has been cleaned again, the total number of videos contained in the end will be slightly less than the previous 16,685.

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
