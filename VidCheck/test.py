# import os
# from tkinter import filedialog
# def browse_folder():
#     return filedialog.askdirectory()
#
#
#
#
# def get_video_list():
#     folder_path = browse_folder()
#     video_extensions = ('.mp4', '.avi', '.mkv')
#     video_list = []
#     if folder_path:
#         for file in os.listdir(folder_path):
#             if file.endswith(video_extensions):
#                 video_list.append(file)
#         video_list.sort()
#         return video_list
#     else:
#         return []
#
# with open("LoveBobber",mode ="w") as file:
#     for file_name in get_video_list():
#         file.write(file_name+"\n")
#
titles=[]
links =[]
with open("Diksha.txt") as file:
    lines = file.readlines()
    for i,line in enumerate(lines):
        if i%3==0:
            titles.append(line.strip(' \n'))
        elif i%3==1:
            links.append(line.strip(' \n'))
newtitles = []
newlinks = []
for title,link in zip(titles,links):
    if "Interview" in title:
        newtitles.append(title)
        newlinks.append(link)

# print(len(titles),len(links),len(newlinks))
# print(titles)
