from Database.DbAccess import *
import youtube_dl
import os
from GUI.Alert_window import *
from Security.Insert_Secret_Code import Secret_Code_Generator


def download_video(video):
    # prepare folder path of the video
    path = os.path.expanduser('~/Documents') + '/Videos/%s/' % video.get_title()
    #  outtmpl: Template for output names.
    ydl_opts = {
        'outtmpl': path + '%(title)s.%(ext)s',
        'restrictfilenames': 'true',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video.get_link()])

        folder_name = video.get_title()
        # get the file name by listdir
        file = os.listdir(path)
        filename = file[0]
        video.set_video_path("Videos/{}/{}".format(folder_name, filename))
        video.set_secret_code(Secret_Code_Generator())
        # insert in the database
        conn = DBConnection()
        conn.insert_video(video)
        info_alert_window('Download is finished',  "'{}' has been Successfully Downloaded!".format(filename))


def download_all_videos(videos_list):
    if videos_list:
        for video in videos_list:
            download_video(video)
