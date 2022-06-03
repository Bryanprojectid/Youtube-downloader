from pytube import YouTube

Link = input("Masukan Link Youtube")

youtube = YouTube(Link)

video = youtube.streams.filter(only_audio=True)
video_2 = list(enumerate(video))
for i in video_2:
	print(i)
print()
select = int(input("Masukan: "))
video[select].download()
print('berhasil')