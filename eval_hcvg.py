import numpy as np
import json


def iou2d(box1, box2):
    '''
        box [x1,y1,x2,y2]
    '''
    area1 = (box1[2]-box1[0])*(box1[3]-box1[1])
    area2 = (box2[2]-box2[0])*(box2[3]-box2[1])
    area_sum = area1 + area2

    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    if x1 >= x2 or y1 >= y2:
        return 0
    else:
        inter_area = (x2-x1)*(y2-y1)
    iou = inter_area/(area_sum-inter_area)
    return iou


def hcvg_eval(pred_path, gt_path):
    '''
    input:
    pred and gt:
    {
        'video_id': {
        'ed_frame':st,
        'ed_frame':ed,
        'bbox':{
            'st':[x1,y1,x2,y2],
            'st+1':[x1,y1,x2,y2],
            ...
            'ed':[x1,y1,x2,y2],
            }
        },
    }
    output:
    mviou,mtiou,viou@0.3,viou@0.5,
    '''
    gt = json.load(open(gt_path, "r"))  # load gt json
    pred = json.load(open(pred_path, "r"))  # load pred json
    # print(eval_hcvg(pred, gt))
    vious = []
    tious = []
    for video in gt:
        if video not in pred:
            viou = 0
            tiou = 0
        else:
            # compute tiou
            gt_v = gt[video]
            pred_v = pred[video]
            ious = []
            for frame_id in gt_v['bbox']:
                if frame_id in pred_v['bbox']:
                    ious.append(
                        iou2d(pred_v['bbox'][frame_id], gt_v['bbox'][frame_id]))
            all_frame = max(gt_v['ed_frame'], pred_v['ed_frame']) - \
                min(gt_v['st_frame'], pred_v['st_frame']) + 1
            viou = sum(ious) / all_frame
            tiou = len(ious) / all_frame
        vious.append(viou)
        tious.append(tiou)
    vious = np.array(vious)
    return [np.mean(vious), np.mean(tious), np.mean((vious > 0.3) + 0), np.mean((vious > 0.5) + 0),]


# print(hcvg_eval("challenge/results_c.json", "challenge/hcvg_test.json"))

