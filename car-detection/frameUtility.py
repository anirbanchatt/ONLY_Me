import shutil

# This function copies key frames to destination folders
def copy_frames(vid_num, accident_frames, non_accident_frames):
    
    frame_path = '../../major project/dataset/frames/'
    key_frame_path = '../../major project/dataset/keyFrames/'
    
    try:
        for frame_num in accident_frames:
            frame_name = "vid" + str(vid_num) + "-shot" + str(frame_num) + ".jpg"
            shutil.copy(frame_path+frame_name, key_frame_path+"accident/")

        for frame_num in non_accident_frames:
            frame_name = "vid" + str(vid_num) + "-shot" + str(frame_num) + ".jpg"
            shutil.copy(frame_path+frame_name, key_frame_path+"non accident/")
    except:
        print('Frame index out of bound')


# this function returns frame no of frame which is to be included in non-accident
def giveNoAccidentFrameList(accident_frames):
    non_accident_frames = []
    l = len(accident_frames) # size of list
    i = 0
    while i < l:
        j = i+1
        while j < l and accident_frames[j]-accident_frames[j-1] == 1:
            j += 1
        
        continuous_frames = j-i
        
        # going before accident
        for k in range(0,continuous_frames//2):
            frame_no = accident_frames[i]-k-1
            if (frame_no in accident_frames) or frame_no <= 0:
                break
            else:
                non_accident_frames.append(frame_no)
        
        # going after accident
        for k in range(0,continuous_frames//2):
            frame_no = accident_frames[j-1]+k+1
            if (frame_no in accident_frames):
                break
            else:
                non_accident_frames.append(frame_no)
        
        if continuous_frames == 1:
            if accident_frames[i]-1 >= 0:
                non_accident_frames.append(accident_frames[i]-1)
            elif (1 not in accident_frames):
                non_accident_frames.append(1)
        
        i = j
    
    return non_accident_frames