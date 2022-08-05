# Youtube Video Downloader (Single Video)

from pytube import YouTube

link = "https://youtu.be/BddP6PYo2gs" #link of video

youtube_1 = YouTube(link)

print(youtube_1.title)
print(youtube_1.thumbnail_url)

# videos = youtube_1.streams.all() # All format 

videos = youtube_1.streams.filter(only_audio = True) # Omly Audio

vid = list(enumerate(videos))
for i in vid:
    print(i)

strm = int(input(" Enter : "))
videos[strm].download()

print("Successfully")    