from pytube import YouTube

DOWNLOAD_FOLDER = "/Downloads"

video_url = "https://www.youtube.com/watch?v=EEfw9vgHRMI"

video_obj = YouTube(video_url)

stream = video_obj.streams.get_highest_resolution()

stream.download(DOWNLOAD_FOLDER)