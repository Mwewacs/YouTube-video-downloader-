#import the package
from pytube import YouTube

url= input("paste a video link here")
my_video=YouTube(url)

print("-------------------video title----------------------")
print(my_video.title)

print("-------------------thumbnail image-------------------")
print(my_video.thumbnail_url)

print("---------------------download video-------------------")
 
my_video= my_video.streams.get_highest_resolution()
#for stream in my_video.streams.first()
#    Print(stream)

my_video.download()
