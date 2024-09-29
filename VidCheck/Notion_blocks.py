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

def create_heading(nth = 1,text=""):
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
