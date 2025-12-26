from pathlib import Path

def default_location():
    filepath = Path(r"C:\Users\HP\AppData\Roaming\yt-dlp\config.txt")

    # Check if config file exists
    pathCheck = filepath.exists()
    if pathCheck == True :
        with open(filepath,mode="r",encoding="utf-8") as file:
            for line in file:
                if line.startswith("-o") :
                    output,downloadPathTitleExt = line.split()
                    downloadPath,title,ext = downloadPathTitleExt.split("%")
                    return (downloadPath.strip('"'))
    else :
        downloadPath = input("Enter default location for downloads : ")
        title_extension = r"\%(title)s.%(ext)s"
        with open(filepath,mode="w",encoding="utf-8") as file:
            file.write(f'# Save downloads to Downloads folder \n-o "{downloadPath}{title_extension}')
        return downloadPath


