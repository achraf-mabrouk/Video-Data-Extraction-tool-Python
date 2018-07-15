class Video:

    # constructor
    def __init__(self, search_keywords, title, link, video_path=None, audio_path=None, frames_path=None,
                 secret_code=None):
        self.__search_keywords = search_keywords
        self.__title = title
        self.__link = link
        self.__video_path = video_path
        self.__audio_path = audio_path
        self.__frames_path = frames_path
        self.__secret_code = secret_code

    def get_search_keywords(self):
        return self.__search_keywords

    def set_search_keywords(self, search_keywords):
        self.__search_keywords = search_keywords

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_link(self):
        return self.__link

    def set_link(self, link):
        self.__link = link

    def get_video_path(self):
        return self.__video_path

    def set_video_path(self, audio_path):
        self.__video_path = audio_path

    def get_audio_path(self):
        return self.__audio_path

    def set_audio_path(self, audio_path):
        self.__audio_path = audio_path

    def get_frames_path(self):
        return self.__frames_path

    def set_frames_path(self, frames_path):
        self.__frames_path = frames_path

    def get_secret_code(self):
        return self.__secret_code

    def set_secret_code(self, secret_code):
        self.__secret_code = secret_code

    def display_data(self):
        print("Title : " + self.__title)
        print(self.__search_keywords)
        print("Link : " + self.__link)
        if self.__video_path:
            print("Video Path : " + self.__video_path)
        if self.__audio_path:
            print("Audio Path : " + self.__audio_path)
        if self.__frames_path:
            print("frames Path : " + self.__frames_path)
