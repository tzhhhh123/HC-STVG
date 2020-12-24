# HC-STVG

The HC-STVG Dataset. The duration of all videos is 20s.

## The videos are available

[Baidu pan](https://pan.baidu.com/s/1t6-rCLwaTtn-HKoIUfYAQg) key <u>3viv</u>     
[One Drive](https://buaaeducn-my.sharepoint.com/:f:/g/personal/tzhhhh123_buaa_edu_cn/EgRwMs64E1RIj0-wx2s06-MBij8TjFpZerJeZQ79eS8JdA?e=HGEOh5) key <u> tzhhhh123</u>     

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
