from notion_client import Client
from notion_client.errors import APIResponseError
from Notion_blocks import create_codeblock, create_heading, create_embed, create_text_paragraph



def create_page(client,database_id,video_title, video_link):

    new_page_name = video_title
    new_page = {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": new_page_name
                    }
                }
            ]
        },



    }
    children = [
        create_embed(link=video_link),
        create_heading(nth=2, text="My Answer 1"),
        create_text_paragraph(),
        create_heading(nth=2, text="My Answer 2"),
        create_text_paragraph(),
        create_heading(nth=2, text="Recordings"),
        create_text_paragraph(),


    ]
    icon = {
        "emoji": "🧑‍💻"
    }
    try:
        created_page = client.pages.create(parent={"database_id": database_id}, properties=new_page, children=children,
                                           icon=icon)
        print(f"Created page {created_page['url']}")
    except APIResponseError as e:
        print(e)

if __name__ == "__main__":
    API_KEY = "secret_lYRoD00YCYVQMbZzhQDg6pp3Bu8zqaGOMgjHB6P6Ykm"
    notion = Client(auth=API_KEY)
    database_id = "a99a9cfee9c9466db108bb87847fe935"
    # create_page(notion,database_id,"Hello","https://www.youtube.com/watch?v=WQoB2z67hvY&list=PLDzeHZWIZsTryvtXdMr6rPh4IDexB5NIA&index=1")
    titles=[]
    links =[]
    with open("Diksha.txt") as file:
        lines = file.readlines()
        for i,line in enumerate(lines):
            if i%3==0:
                titles.append(line.strip(' \n'))
            elif i%3==1:
                links.append(line.strip(' \n'))
    for title,link in zip(titles[77:],links[77:]):
        if "Interview" in title:
            create_page(notion,database_id,title,link)
