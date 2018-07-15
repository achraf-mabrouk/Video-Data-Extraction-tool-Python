def remove_none_videos_links(video_list):
    if video_list:
        new_result = []
        for video in video_list:
            if "youtube.com" in video.get_link() or "dailymotion.com" in video.get_link() \
                    or "vimeo.com" in video.get_link() \
                    or "metacafe.com" in video.get_link() or "videa" in video.get_link() \
                    or "veoh.com" in video.get_link() or "facebook.com" in video.get_link():
                new_result.append(video)

        return new_result


def remove_duplications(video_list):
    new_list = []
    for video in video_list:
        if video not in new_list:
            new_list.append(video)
    return new_list
