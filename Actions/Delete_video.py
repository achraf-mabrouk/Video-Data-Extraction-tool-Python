from GUI.Alert_window import info_alert_window
from Database.DbAccess import DBConnection


def delete_video(_video):
    conn = DBConnection()
    conn.delete_video_by_video_path(_video)
    info_alert_window("Delete Process", "'{}' has been successfully deleted!".format(_video.get_title()))

