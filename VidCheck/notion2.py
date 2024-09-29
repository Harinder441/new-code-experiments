import requests, json

token = "secret_lYRoD00YCYVQMbZzhQDg6pp3Bu8zqaGOMgjHB6P6Ykm"

databaseId = "a8fbd903ed4943aba6323b10c20ff5b3"

headers = {
    "Authorization": "Bearer " + token,
    "Notion-Version": "2022-06-28",
    "content-type": "application/json",
}


def createPage(databaseId, headers):
    createUrl = 'https://api.notion.com/v1/pages'

    newPageData = {
        "parent": {"database_id": databaseId},
        "properties": {
            "Name": {"title": [{"text": {"content": "My new page 3"}}]},
            "Tags": {"multi_select": [{"name": "tag1"}, {"name": "tag2"}]}, },
        "content": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": "Some words ",
                        "link": None,
                    },
                    "annotations": {
                        "bold": False,
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,




                        "code": False,
                        "color": "default"
                    },
                    "plain_text": "Some words ",
                    "href": None
                }, ]

        },
    }

    data = json.dumps(newPageData)
    # print(str(uploadData))

    res = requests.request("POST", createUrl, headers=headers, data=data)

    print(res.status_code)
    print(res.text)

createPage(databaseId,headers)
