# AutoMusicDL

## Description
This program runs a Python-based script to make easier the music downloads from the Internet. Up to now, it only runs on Windows. All requirements are shown below.

## Requirements
- Python libraries (installable using pip):
    - youtube-search.
    - fnmatch.
    - os.
    - subprocess.
- yt-dlp [(source)](https://github.com/yt-dlp/yt-dlp).

## How to use AutoMusicDL
In short:
1. Run the script in a terminal, using `python.exe automusicdl.py`
2. You'll be asked if you want to update yt-dlp before the start of the program. Default is no.
3. Then, You'll be asked the artist name. Type it, or type 'exit' to stop the program and leave.
4. Type the song name.
5. The program will show 3 results. You can select one typing its number.
    1. If it's not enough, you can type 'more', to show 3 more.
    2. If you have seen 9 results, and still you haven't found the correct song, you'll be given the option to add a result manually, or leave the program.
6. Once the link is selected, yt-dlp will start downloading the song.
7. When the sound has been downloaded, the program will rename it to the **artist** and **song name** given, using the format `Artist name - Song name.mp3`, so please, type it correctly from the start ;-).
8. The program will move the renamed file to the subfolder Music, where all songs are stored.
9. The process starts over from step 2, since it's an infinite `while` loop. You can exit now from the program typing `exit`.

---
Hope the script helps! Consider starring it.
Raúl Durán.
