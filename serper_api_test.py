from backend.services.serper import serper_search

results = serper_search("Bob Smith Toronto")

for results in results:
    print(result["title"])
    print(result["link"])
    print()

# from backend.config import SERPER_API_KEY
# import requests

# def serper_search():
#     headers = {
#     "X-API-KEY": SERPER_API_KEY,
#     "Content-Type": "application/json",
#     }
#     body = {"q": "Bob Smith Toronto site:linkedin.com"}
#     response = requests.post("https://google.serper.dev/search", headers=headers, json=body)

#     print(response.status_code)
#     print(response.text)
        
#     data = response.json()
#     for result in data["organic"]:  
#         print(result["title"])
#         print(result["link"])
#         print()