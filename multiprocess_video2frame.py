
import cv2
import os
import glob
from multiprocessing import Pool
import random
import json

video_paths = glob.glob('{video dir}')  # replace with the specific video dir
frame_save_dir = '{output dir}'  # replace with the specific output dir
print("total video:", len(video_paths))
gap = 6  # the interval 
num_process = 32  

# import IPython
# IPython.embed()
# random.shuffle(video_paths)
# gap = 15


def process_video2frame(part_video_list):
    cnt = 0
    for idx, video_path in enumerate(part_video_list):
        v_name = os.path.basename(video_path)
        v_name = v_name[:v_name.rfind('.')]
        video_frame_save_dir = os.path.join(frame_save_dir, v_name)
        if not os.path.exists(video_frame_save_dir):
            os.makedirs(video_frame_save_dir)
        else:
            print("already exist, ", video_frame_save_dir)
            if os.path.exists(os.path.join(video_frame_save_dir, '00000.jpg')):
                continue
            # continue

        frame_cnt = 0
        cap = cv2.VideoCapture(video_path)
        success, frame = cap.read()
        while success:
            # frame = cv2.resize(frame, (171, 128))
            if frame_cnt % gap == 0:
                cv2.imwrite(os.path.join(video_frame_save_dir,
                                         '{:0>5d}.jpg'.format(frame_cnt)), frame)
            frame_cnt += 1
            success, frame = cap.read()
        cap.release()

        print("{}: {} done.".format(idx + 1, v_name))


print('Parent process %s.' % os.getpid())
p = Pool(num_process)
part_list_len = len(video_paths) // num_process
for i in range(num_process):
    if i == num_process - 1:
        part_list = video_paths[part_list_len * i:]
    else:
        part_list = video_paths[part_list_len * i:part_list_len * (i + 1)]
    p.apply_async(process_video2frame, args=(part_list,))
print('Waiting for all subprocesses done...')
p.close()
p.join()
print('All subprocesses done.')

