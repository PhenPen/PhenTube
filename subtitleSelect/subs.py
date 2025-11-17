import os

#Still working on this 


def subs(url) :
    while True:
        subs_Select_input = ("Do you want subtitles (y/n) : ").upper()
        if subs_Select_input == "Y" :
            print("Selected Subtitles")
            subs_Lang_Select(url)
        elif subs_Select_input == "N" :
            print("Selected no Subtitles")
            break
        else:
            print("Invalid selection.Try again")


def subs_Lang_Select(url) :
    print()
    print("Do you want default subs or another language")
    while True :
        subs_selection = input("Enter D for default subs and A for another language").upper()
        if subs_selection == "D" :
            os.system(f'yt-dlp --write-subs "{url}"')
        elif subs_selection == "A" :
            os.system(f"yt-dlp --list-subs {url}")
        else :
            print("Invalid Selection.Try again")


subs ("https://www.youtube.com/watch?v=dQw4w9WgXcQ")