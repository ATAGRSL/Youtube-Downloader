import os
from pytube import YouTube

link = input("Enter the YouTube video link: ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

# get the current working directory
cwd = os.getcwd()
folder_name = os.path.join(cwd,'Downloads')

# Create a folder to store the downloaded videos
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Download video in highest resolution
yd = yt.streams.get_highest_resolution()
yd.download(folder_name)

# Print video information
print("Video codec: ", yd.video_codec)
print("Audio codec: ", yd.audio_codec)
print("Video format: ", yd.subtype)
print("Video file size: ", yd.filesize/(1024*1024), "MB")