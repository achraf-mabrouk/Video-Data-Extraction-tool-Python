from Database.DbAccess import *
import cv2


def PlayVideo(video_path):
    fullpath = os.path.expanduser('~/Documents') + '/' + video_path

    cap = cv2.VideoCapture(fullpath)
    # prepare the frame window
    cv2.namedWindow("Video Player", 0)
    cv2.resizeWindow("Video Player", 800, 600)
    while cap.isOpened():
        ret, frame = cap.read()

        Default_Color = cv2.cvtColor(frame, 0)
        cv2.imshow('Video Player', Default_Color)
        # 25 milliseconds
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('Video Player', cv2.WND_PROP_VISIBLE) < 1:
            break
    cap.release()
    cv2.destroyAllWindows()

