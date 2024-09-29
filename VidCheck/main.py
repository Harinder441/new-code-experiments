import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()





def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        video_list = get_video_list(folder_path)
        display_videos(video_list, folder_path)


def get_video_list(folder_path):
    video_extensions = ('.mp4', '.avi', '.mkv')
    video_list = []
    for file in os.listdir(folder_path):
        if file.endswith(video_extensions):
            video_list.append(file)
    return video_list


def display_videos(video_list, folder_path):
    for i, video in enumerate(video_list):
        # Create check button
        check_var = tk.BooleanVar()
        check_button = tk.Checkbutton(root, variable=check_var)
        check_button.grid(row=i, column=0)

        # Create play button
        play_button = tk.Button(root, text="Play", command=lambda video=video: play_video(video, folder_path))
        play_button.grid(row=i, column=1)

        # Display video filename
        video_label = tk.Label(root, text=video)
        video_label.grid(row=i, column=2)


# Function to play video
def play_video(video, base_path):
    os.startfile(base_path + "/" + video)


# Create GUI elements
folder_label = tk.Label(root, text="Select folder:")
folder_label.grid(row=0, column=0)

browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=1)

root.mainloop()
