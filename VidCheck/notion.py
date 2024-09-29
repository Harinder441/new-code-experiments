# from notion_client import Client
love_bobber_id ="bbdd306d887f40b397f7fdd36bdf762c"
import os
from notion_client import Client
from notion_client.errors import APIResponseError

def create_text_paragraph(text=" "):
    para={
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text,
                        }
                    }
                ]
            }
        }
    return para

def create_heading(nth = 1,text="",is_toggleable="false",color="default"):
    head= {
            "object": "block",
            "type": f"heading_{nth}",
            f"heading_{nth}": {
                "rich_text": [{"type": "text", "text": {"content": text}}]
            },

            }
    return head

def create_embed(link):
    return {
                "object": "block",
  "type": "embed",
  "embed": {
    "url": link
  }
}

def create_codeblock(code="",language = "python"):
    return {
  "type": "code",
  "code": {
    "rich_text": [{
      "type": "text",
      "text": {
        "content": code
      }
    }],
    "language": language
  }
}
# Authenticate with the Notion API using your API key
notion = Client(auth="secret_lYRoD00YCYVQMbZzhQDg6pp3Bu8zqaGOMgjHB6P6Ykm")

# Retrieve the database ID for the database where you want to create the page
database_id = "a8fbd903ed4943aba6323b10c20ff5b3"

# Create a new page in the database

new_page_name = "My New Page 4"
new_page_content = "This is a sample paragraph."
new_checkbox_value = True

# Create a new page and set checkbox property
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
    "Tags": {"multi_select": [{"name": "tag1"}, {"name": "tag2"}]},

}
children =[
        create_embed(link="https://www.youtube.com/watch?v=WQoB2z67hvY&list=PLDzeHZWIZsTryvtXdMr6rPh4IDexB5NIA&index=1"),
        create_heading(nth=2,text="Notes"),
        create_text_paragraph(),
        create_heading(nth=2,text="Codes"),
        create_codeblock(),
        create_codeblock(),
        create_heading(nth=2,text="Files or links"),
        create_text_paragraph(),

    ]
icon =  {
  	"emoji": "🧑‍💻"
}


try:
    created_page = notion.pages.create(parent={"database_id": database_id}, properties=new_page,children=children,icon =icon)
    print(f"Created page {created_page['url']}")
except APIResponseError as e:
    print(e)
