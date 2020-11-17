# HC-STVG
The HC-STVG Dataset
## The videos are available at https://pan.baidu.com/s/1t6-rCLwaTtn-HKoIUfYAQg
key(提取码)：3viv     
The duration of all videos is 20s.
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
