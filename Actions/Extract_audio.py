from Security.Insert_Secret_Code import concat_2_audio
from Database.DbAccess import *
from GUI.Alert_window import *
from pathlib import Path


def NotExist(video_path):
    conn = DBConnection()
    return conn.check_audio_path(video_path)[0][0] is None


def Extract_Audio(video, Audioformat):
    f = video.get_video_path()
    # check the file format
    if f.lower()[-3:] in ["mp4", "mkv", "m4v", "m4a", "mpg", "flv", "avi"]:
        print("processing", f)

        output = process(f, Audioformat.lower())
        if output != -1:
            video.set_audio_path(output)
            conn = DBConnection()
            conn.update_audio_path(video)
            concat_2_audio(video, Audioformat.lower())
            info_alert_window('Extract Audio is finished',
                              "Conversion to audio file (%s) is done with Success !!" % Audioformat)
        else:
            critical_alert_window('Error Extracting Audio..', 'the Audio file is Already Exist !')
    else:
        warning_alert_window("Error Video Format", "Error : Unexpected video format file !")


def process(input_file, Audioformat):
    output_file = input_file[:-3] + Audioformat
    if NotExist(input_file):
        # -i  : input file name
        # -vn : tells ffmpeg that we don't want video
        # -ab : bit rate
        # -f  : format of the output file
        home = str(Path.home())
        absolute_path_input = Path(home + "/Documents/" + input_file)
        absolute_path_output = Path(home + "/Documents/" + output_file)
        cmd = "ffmpeg -i \"{}\" -ab 192000 -vn -f {} \"{}\"".format(absolute_path_input, Audioformat,
                                                                    absolute_path_output)
        os.system(cmd)
        return output_file
    else:
        return -1
