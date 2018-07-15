import sqlite3
import sys
import shutil
import os
from Model.Video import Video
import pkg_resources


class DBConnection:

    def __init__(self):
        self.db_file = pkg_resources.resource_filename('Database', 'multimedia_content_mining.db')
        self.con = None
        self.connect()

    def connect(self):
        try:
            self.con = sqlite3.connect(self.db_file)
        except sqlite3.Error as e:
            print('connect() Error %s:' % e.args[0])
            self.close()
            sys.exit(1)

    # never used xD
    def close(self):
        if self.con:
            self.con.close()

    def insert_video(self, video):
        with self.con:
            c = self.con.cursor()
            c.execute("""insert into videos VALUES(?,?,?,?,?,?,?)""", (video.get_search_keywords(), video.get_title(),
                                                                       video.get_link(), video.get_video_path(), None,
                                                                       None, video.get_secret_code()))
            self.con.commit()

    def delete_video_by_video_path(self, video):
        with self.con:
            c = self.con.cursor()
            c.execute('DELETE FROM videos WHERE video_path=?', (video.get_video_path(),))
            self.con.commit()
            fullPath = os.path.expanduser('~/Documents') + "/Videos/{}".format(video.get_title())
            print(fullPath)
            shutil.rmtree(fullPath, ignore_errors=False)

    def get_all_videos(self):
        with self.con:
            c = self.con.cursor()
            c.execute("SELECT * FROM videos")
            rows = c.fetchall()
            list_videos = []
            for row in rows:
                list_videos.append(Video(row[0], row[1], row[2], row[3], None, None, row[6]))

            return list_videos

    def get_video_by_title(self, title):
        with self.con:
            c = self.con.cursor()
            c.execute("""SELECT * FROM videos WHERE title=?""", (title,))
            rows = c.fetchall()

            list_videos = []
            for row in rows:
                list_videos.append(Video(row[0], row[1], row[2], row[3]))

            return list_videos

    def get_audio_path(self, _audio_path):
        with self.con:
            c = self.con.cursor()
            c.execute("""SELECT audio_path FROM videos WHERE audio_path=?""", (_audio_path,))
            rows = c.fetchall()
            return len(rows)

    def check_audio_path(self, video_path):
        with self.con:
            c = self.con.cursor()
            c.execute("""SELECT audio_path FROM videos WHERE video_path=?""", (video_path,))
            return c.fetchall()

    def update_audio_path(self, video):
        with self.con:
            c = self.con.cursor()
            c.execute("""UPDATE videos 
                    SET audio_path=?
                    WHERE video_path =?""", (video.get_audio_path(), video.get_video_path()))
            self.con.commit()

    def get_frames_path(self, _frames_path):
        with self.con:
            c = self.con.cursor()
            c.execute("""SELECT frames_path FROM videos WHERE frames_path=?""", (_frames_path,))
            rows = c.fetchall()
            return len(rows)

    def update_frames_path(self, video):
        with self.con:
            c = self.con.cursor()
            c.execute("""UPDATE videos 
                    SET frames_path=?
                    WHERE video_path=?""", (video.get_frames_path(), video.get_video_path()))
            self.con.commit()
