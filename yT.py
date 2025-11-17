from contentSelect import video,playlist
from downloadSelect import downloaderVideo,downloaderPlaylist

# Video or Playlist selection
print("Enter V for Video and P for Playlist")
while True:
    content = input("Download Video or Playlist : ").upper()
    if content == "V":
        url = input("Enter Youtube Video URL : ")
        ID = video.video(url)
        downloaderVideo.downloader(ID,url)
        break
    elif content == "P":
        url = input("Enter Youtube Playlist URL : ")
        ID = playlist.playlist(url)
        downloaderPlaylist.downloader(ID,url)
        break
    else:
        print("Not a valid content selection. Try Again")


#os.system(f'yt-dlp -F "{url}"') #Could have used os.system here but subprocess seems better

