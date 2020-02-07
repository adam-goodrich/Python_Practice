import random
import os
import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
# lets initalize the music mixer here. Why not
pygame.mixer.init()
# I am using Tkinter askdirectory function. Tkinter auto opens a window on your computer and this hides that window. Keep it clean.
root = tk.Tk()
root.withdraw()

# clears the screen, let's start fresh
os.system("clear")

directory = askdirectory()
os.chdir(directory)
list_dir = os.listdir(directory)
list_dir.sort()
print(f"\n{directory}\n")
# print("\nHere is an available track listing\n")

list_of_songs = []
for files in list_dir:
    if files.endswith(".mp3"):
        list_of_songs.append(files)
        # print(files)
# track_num = int(input("\nWhat track do you want to play?: "))
another_track = ""
score = 0
while another_track != "q":
    three_rand_songs = random.sample(range(len(list_of_songs)), 3)
    rando = random.randint(0,2)
    track_num = three_rand_songs[rando]
    choice = 1
    for i in three_rand_songs:
        rand_song_list = i
        print(f"\n{choice}) --- {list_of_songs[rand_song_list]}\n")
        choice += 1

    pygame.mixer.music.stop()
    pygame.mixer.init()
    pygame.mixer.music.load(list_of_songs[int(track_num)])
    pygame.mixer.music.play()
    which_song = input("\nWhich song is playing? 1, 2, or 3? \n\nPress q to quit \n\n")
    which_song = int(which_song) - 1
    which_song = int(which_song)
    if which_song == rando:
        print("\n..............................\n")
        print("\nCORRECT!\n")
        score += 1
        print(f"The score is\n\n{score}\n")
        print("\n..............................\n")
    else:
        print("\n..............................\n")
        print("\nsorry that is not it\n")
        print(f"The score is\n\n{score}\n")
        print("\n..............................\n")

print("\n..............................\n")
print(f"Thanks for playing the final score was {score}")
print("\n..............................\n")