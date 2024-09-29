import requests as req
from bs4 import BeautifulSoup
import random
import json
# get name ,link,description and image
URL = "https://github.com/Harinder441?tab=repositories"
END_URL = "https://github.com"

res = req.get(url=URL)
content = res.text
soup = BeautifulSoup(content, "html.parser")

repo = soup.findAll(itemprop="name codeRepository")
desc_name = soup.findAll(itemprop="description")
data_r = []
for i in range(len(desc_name)):
    data = {}

    data['name'] = repo[i].get_text().strip('\n ')
    data['github-link'] = END_URL + repo[i]['href']
    data['description'] = desc_name[i].get_text().strip('\n ')
    data_r.append(data)

images = ["https://unsplash.com/photos/OqtafYT5kTw",
          "https://images.unsplash.com/photo-1523800503107-5bc3ba2a6f81?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fGNvZGluZ3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60"
    ,
          "https://images.unsplash.com/photo-1607706189992-eae578626c86?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cHl0aG9uJTIwY29kaW5nfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
          "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTd8fHB5dGhvbiUyMGNvZGluZ3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60"]


def get_animation_img(url):
    res = req.get(url=url)
    content = res.text
    soup = BeautifulSoup(content, "html.parser")
    repo = soup.select('.markdown-body p a')
    if repo:
        return repo[0]['href']
    else:
        return random.choice(images)


for data in data_r:
    data['img_url'] = get_animation_img(data['github-link'])
print(data_r)

with open("data.json",mode="w") as file:
    data=json.dumps(data_r)
    file.write(data)
    pass
