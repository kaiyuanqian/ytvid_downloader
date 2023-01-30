from pytube import YouTube

#Get link
link = input("Enter video link:\n")
yt = YouTube(link)

#Location of download
location = input("Enter directory address:\n")

print("Title: ", yt.title)
print("Views: ", yt.views)

vid = yt.streams.get_highest_resolution()

vid.download(location)