import cv2
import os

from Security.Insert_Secret_Code import hide_code_in_image
from Database.DbAccess import DBConnection
from GUI.Alert_window import *


def NotExist(output_file):
    conn = DBConnection()
    return conn.get_frames_path(output_file) == 0


def Split_video_to_images(video):
    User_path = os.path.expanduser('~/Documents')
    folder_path = User_path + "/Videos/{}/frames".format(video.get_title())

    if NotExist(folder_path):
        # make the data folder
        try:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        except OSError:
            warning_alert_window('create folder', 'Error: Creating directory of data !')

        # Playing video from file:
        cap = cv2.VideoCapture(User_path + "/" + video.get_video_path())
        currentFrame = 0
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            # if we reach the end of the video ,we gonna break the while loop
            if not ret:
                break
            # Saves image of the current frame in jpg file
            file_name = 'frame' + str(currentFrame) + '.jpg'

            print('Creating...' + file_name)
            frame_fullpath = folder_path + "/" + file_name
            cv2.imwrite(frame_fullpath, frame)
            hide_code_in_image(frame_fullpath, video)
            # To stop duplicate images
            currentFrame += 1
        # When everything done, release the capture
        # release() : Closes video capture and video file.
        cap.release()
        cv2.destroyAllWindows()
        video.set_frames_path(folder_path)
        # add frames path in the database
        conn = DBConnection()
        conn.update_frames_path(video)
        info_alert_window("Extract Frames is finished", "Extraction of Frames is done with Success !!")
    else:
        critical_alert_window('Error Extracting Images..', 'the frames folder of this video is Already Exist !')
