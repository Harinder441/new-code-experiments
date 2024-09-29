import requests

url = "https://techcrunch-unofficial.p.rapidapi.com/news"

headers = {
	"X-RapidAPI-Key": "9b4a7d0f7amsh275fa682307c2eep161f9ejsn3787a1c66840",
	"X-RapidAPI-Host": "techcrunch-unofficial.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
