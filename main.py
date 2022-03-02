from pytube import YouTube

DOWNLOAD_FOLDER = "PATH_TO_DOWNLOAD_FOLDER"

video_url = "VIDEO_URL"

video_obj = YouTube(video_url)

stream = video_obj.streams.get_highest_resolution()

stream.download(DOWNLOAD_FOLDER)
