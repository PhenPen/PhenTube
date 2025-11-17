import subprocess

def table_short(url) :
    table_short = subprocess.run(['yt-dlp','-F',url],capture_output=True, text= True)