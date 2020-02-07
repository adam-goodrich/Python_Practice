
import os
import pygame
from tkinter.filedialog import askdirectory
from tkinter import *
import mutagen

root = Tk()
root.minsize(0,0)


files_in_folder = os.listdir("/Users/agoodrich/Music/mp3")
print(files_in_folder)
print(f"/Users/agoodrich/Music/mp3/{files_in_folder[3]}")
# print(files_in_folder)

list_of_songs = []

index = 0

def directorychooser():
    directory = askdirectory()
    os.chdir(directory)
    os.listdir(directory)
    list_dir = os.listdir(directory)
    list_dir.sort()
    for files in list_dir:
        if files.endswith(".mp3"):
            list_of_songs.append(files)
            print(files)
    
def music_player():
    another_song = "y"
    pygame.mixer.init()
    while another_song == "y":
        pygame.mixer.music.load(list_of_songs[int(input("What track do you want to play?: "))-1])
        pygame.mixer.music.play()
        next_input = input("Type STOP to stop music: ")
        next_input = next_input.upper()
        print(next_input)
        if next_input == "STOP":
            pygame.mixer.music.stop()
            another_song = input("Do you want to hear another song? y/n: ")
            another_song = another_song.lower
        else:
            continue



directorychooser()
music_player()

label = Label(root,text="Adam's Music Player")
label.pack()

listbox = Listbox(root)
listbox.pack()

for i in list_of_songs:
    listbox.insert(0,i)

next_button = Button(root,text="Next Song")
next_button.pack()

previous_button = Button(root,text="Previos Song")
previous_button.pack()

stop_button = Button(root,text="Stop")
stop_button.pack()





root.mainloop()






