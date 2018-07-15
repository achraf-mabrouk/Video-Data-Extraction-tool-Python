import binascii
import os
from gtts import gTTS
import Security.Steganography as Steg


def Secret_Code_Generator():
    return str(binascii.hexlify(os.urandom(6)))


def text_to_speech(secret_code, folder_path, audio_format):
    tts = gTTS(text=secret_code, lang='en')
    code_file_path = folder_path + "/code." + audio_format
    tts.save(code_file_path)
    return code_file_path


def concat_2_audio(video, audio_format):
    folder_path = os.path.expanduser('~/Documents') + '/' + os.path.dirname(video.get_audio_path())
    code_file_path = text_to_speech(video.get_secret_code(), folder_path, audio_format)
    abs_audio_path = os.path.expanduser('~/Documents') + '/' + video.get_audio_path()

    file_name = os.path.basename(video.get_audio_path())
    if audio_format == 'mp3':
        os.system(
            'ffmpeg -i "concat:{}|{}" -acodec copy "{}"/output.mp3'.format(abs_audio_path, code_file_path, folder_path))

        # remove the old audio file and code file then rename the output file
        os.remove(abs_audio_path)
        os.remove(code_file_path)
        os.rename('{}/output.mp3'.format(folder_path), '{}/{}'.format(folder_path, file_name))
    else:  # if the audio format is WAV
        os.system('ffmpeg -i "{}" -i "{}" -filter_complex "[0:0][1:0]concat=n=2:v=0:a=1[out]" \
            -map "[out]" "{}"/output.wav'.format(abs_audio_path, code_file_path, folder_path))

        # remove the old audio file and code file then rename the output file
        os.remove(abs_audio_path)
        os.remove(code_file_path)
        os.rename('{}/output.wav'.format(folder_path), '{}/{}'.format(folder_path, file_name))


def hide_code_in_image(img_path, video):
    Steg.encode(img_path, video)
