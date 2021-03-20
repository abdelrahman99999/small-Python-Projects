import pytube
from pytube.cli import on_progress

url=input("Enter your youtube  video link \n")

video = pytube.YouTube(url, on_progress_callback = on_progress)

print(str("\nTitle : "+ video.title) +"\n")
for i in video.streams:
    print( str( video.streams.index(i)) + '\tType: ' + str(i.mime_type) + ' | Res ' + str(i.resolution)+ "\n")
ii=int(input("\nEnter index of needed video:  "))
stream = video.streams.filter(mime_type=video.streams[ii].mime_type, resolution=video.streams[ii].resolution)
stream.first().download('C:\\Users\\boody\\Downloads')
print("Done")
