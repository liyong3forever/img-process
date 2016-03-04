__author__ = 'liyong3forever'
import cv2
import os
# to convert the video into images for further image process
def video2img(file_name,out_folder_name):
    if not os.path.isfile(file_name):
        print 'the file does not exist'
    if not os.path.isdir(out_folder_name):
        print 'make folder: ' +  out_folder_name
        os.makedirs(out_folder_name)
    cap = cv2.VideoCapture(file_name)
    frame_count=0
    basename_ext = os.path.basename(file_name)
    basename, extension = os.path.splitext(basename_ext)
    while True:
        ret, img = cap.read()
        if ret:
            frame_count+=1
            out_img_path=os.path.join(out_folder_name,basename+'_'+str(frame_count)+'.jpg')
            cv2.imwrite(out_img_path,img)
#            cv2.imshow('cap_img', img)
        else:
            break

# test sample
# video2img('test.flv','out_folder')


