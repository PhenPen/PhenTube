import os,subprocess,pathlib

def downloader(ID,url) :
    
    # Download Location Selection
    while True:
        download_location = input("Download to Default Location (y/n) : ").upper()
        if download_location == "Y" :
            result = subprocess.run(['yt-dlp' ,'-f', ID, url] ,text=True)
            break
        elif download_location == "N" : 
            downloadPath = pathlib.Path(input("Enter file location eg C:/Users/... : "))
            downloadPath.mkdir(parents=True, exist_ok=True)
            download_template = f'{downloadPath}/%(title)s.%(ext)s'
            result = subprocess.run(["yt-dlp", "-f", ID, "-o", download_template ,url],text=True)
            break 
        else: print("Invalid Selection.Try again")

    # For checking if download was successful    
    if result.returncode == 0 :
        print("Download Completed")
    else:
        print("Download failed")
        print(result.stderr)
