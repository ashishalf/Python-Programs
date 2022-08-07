from pytube import YouTube
url = 'https://youtu.be/4XmgqWXBnRA'
video=YouTube(url)
print("Downloaded")
print(video.title)
print(video.thumbnail_url)
video=video.streams.get_highest_resolution()
video.download()