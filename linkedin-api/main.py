import requests

# set the API endpoint
url = "https://www.linkedin.com/oauth/v2/accessToken"

# set the API headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# set the API parameters
data = {
    "grant_type": "client_credentials",
    "client_id": "773vdrjssiauca",
    "client_secret": "OOOKR5wFuR1oiZa3"
}

access_token = "AQWr4zKkHsESc97_IwL8O8HjDJoPG-KoKGTdVlpqFJ3hT89bKwDFMgDvFMK5qNVCdsRIdK7gz_87S_nnvjNInEjcMKJe71TgTAMLdsh3t9Ubst54qPhu0MO-YNEAx8Ou5ZcsFD2wEP6_Dmsw62Yej6V61SWC1pw5rBtB7QiXdOz8OErAARlpyQk8VYi8jTAwiWHiP19NXgpjAAr2-HvNJNqZhLEFM7yFEGGavR1a36oFbt-Cr2GRMn2HK10zSzl3eVcebLNTSSV2Xea0QP5m79-78tJstIxt2q69BMileu0Du6nrQmjj8e-z-uVP8I8yXibO-gMWf0pCbHRmMWEugrF9x7B2iQ"

# use the access token to get the user's profile
profile_url = "https://api.linkedin.com/v2/me"
profile_headers = {
    "Authorization": f"Bearer {access_token}"
}
profile_response = requests.get(profile_url, headers=profile_headers)
profile_response.raise_for_status()
profile_data = profile_response.json()

# print the user's name
print(profile_data["localizedFirstName"])
