import json
with open('data.json') as file:
    data = file.read()
    data_js = json.loads(data)
with app.app_context():
    i=1
    for data in data_js:
        model = Project()
        model.title = data['name']
        model.description = data['description']
        model.tech_involved = 'Python'
        model.github_link = data['github-link']
        model.image_url = data['img_url']
        model.ranking = i
        db.session.add(model)
        db.session.commit()
        i+=1
