'''
--- YOUTUBE'S AUTOMATIC MUSIC DOWNLOADER ---
Created by: Raúl Durán García (http://github.com/rauldr37)
Creation date: 23 Ago 2023

This script was created to automate the process of downloading music from Youtube. It receives, as an input, the artist name, and the song name, it does a YouTube search,
it downloads it using yt-dlp, renames the song correctly, and places it in a spare folder.
'''

from youtube_search import YoutubeSearch
import os, fnmatch, subprocess

# Global variables for the song name and the artist name
artist = ""
song = ""

def find(pattern, path):
    '''
    Function to return a list of files according to a pattern given. Found in StackOverflow.
    Input:
    - pattern: A string containing the pattern of the file. Could be someting like 'asdf*.txt'.
    - path: A string containing the folder to start the search. '.' would serve as the current folder.
    Output:
    - result: A list containing strings for every file name.
    
    Resource: https://stackoverflow.com/questions/1724693/find-a-file-in-python
    '''
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def choose_between_three(results_list, i_1, i_2, i_3):
    '''
    Select an object between three. A function makes the decision programming process easier if the user does not choose a correct option.
    Input:
    - results_list: A list containing a lot of results.
    - i_1: Index number 1.
    - i_2: Index number 2.
    - i_3: Index number 3.
    Output:
    - sel_index: The list index of the selected link.
    '''
    print("Found these results on the Internet: ")
    print("1: " + str(results_list[i_1]['title']) + " https://youtube.com" + str(results_list[i_1]['url_suffix']).split("&pp")[0])
    print("2: " + str(results_list[i_2]['title']) + " https://youtube.com" + str(results_list[i_2]['url_suffix']).split("&pp")[0])
    print("3: " + str(results_list[i_3]['title']) + " https://youtube.com" + str(results_list[i_3]['url_suffix']).split("&pp")[0])

    sel_index = str(input("Which result are you downloading? (type: 1, 2, 3 or 'more' for more results): "))
    
    if sel_index == 'more':
        if i_3 + 3 >= 10:
            return 11 #Counts as error
        else:
            return choose_between_three(results_list, i_1 + 3, i_2 + 3, i_3 + 3)
    elif not sel_index == '1' and not sel_index == '2' and not sel_index == '3' and not sel_index == 'more':
        return choose_between_three(results_list, i_1, i_2, i_3)
    else:
        return int(sel_index) - 1


def search_song_link(song_name, artist_name):
    '''
    Function to search the link of a song. It uses the library youtube_search, and it returns the first result found.
    Input: 
    - song_name: A string containing the song name.
    - artist_name: A string containing the artist name.
    Output:
    - link: A string containing the link of the song.

    PyPi link of the library: https://pypi.org/project/youtube-search/
    '''
    results = YoutubeSearch(song_name.lower() + " " + artist_name.lower() + " \"Topic\"", max_results=10).to_dict()

    index = choose_between_three(results, 0, 1, 2)

    if index == 11:
        return "" #Counts as error

    link = "https://youtube.com" + str(results[index]['url_suffix'].split("&pp")[0])

    # Remove `list` statement from link.
    if '&list' in link:
        link = link.split('&list')[0]

    return link

def rename_and_replace_file(song_name, artist_name):
    '''
    Changes the original name from yt-dlp (which would be someting similar to 'Video title[yt link].mp3' to 'Artist name - Song name.mp3'.
    Uses the os library.
    Input: 
    - song_name: A string containing the song name.
    - artist_name: A string containing the artist name.
    '''
    song_file = find('*' + song_name[:3] + '*.mp3', '.')

    os.rename(song_file[0].strip(), f"{artist_name} - {song_name}.mp3")

    os.replace(f"{artist_name} - {song_name}.mp3", f"Music/{artist_name} - {song_name}.mp3")

if __name__ == '__main__':
    print("--- AUTOMUSICDL ---\nThanks a lot for using this Python script to download your music.\n")

    update = str(input("Would you like to check updates for yt-dlp before start? (y/n): "))

    while True:
        if update == 'y':
            subprocess.run("resources/yt-dlp.exe --update")
            
            print("Installation succeded.")     
        
        # Main program:
        print("\n--- REMEMBER --- \
            \nType \"exit\" to leave the program.")
        
        artist = str(input("Introduce the artist name: ")).strip()

        if (artist == "exit"):
            break
        else:
            song = str(input("Introduce the song name: ")).strip()

            # Search the link of the video in YouTube.
            song_link = search_song_link(song, artist)

            # If the link is empty, something went wrong.
            if song_link == "":
                print("Could not find a valid song link on YouTube.")

                manual_decision = str(input("Would you like to add one? (y/n): ")).strip()

                # Give the link manually, or leave the program.
                if manual_decision == 'y':
                    song_link = str(input("Add the link: ")).strip()
                else:
                    print("Leaving...")
                    break

            # Calls yt-dlp using subprocess, to download the song from YouTube
            subprocess.run(f"resources\\yt-dlp.exe \"{song_link}\" -x --audio-format mp3 --audio-quality 0 -R 5 --fragment-retries 5", shell = True, check=True)

            # Renames the file to the correct format, and places it in a spare folder.
            rename_and_replace_file(song, artist)

            print(f"Done downloading {song} from {artist}")

    print("\nThank you for using AutoMusicDL. See ya! :)\n")
