import requests
import urllib.request
import json

URL = "https://dl.ibdocs.re/api/"

main_dir = requests.get("https://dl.ibdocs.re/api/IB%20BOOKS/")
json_main_dir = main_dir.json()
URLs_List = []
files_List = []

for dict_item in json_main_dir:
    if dict_item["type"] == "directory":
        item = dict_item["name"]
        item = item.replace(" ", "%20")
        print("Name: " + item)
        URLs_List.append(URL + "IB%20BOOKS/" + item + "/")

for i in URLs_List:
    request = requests.get(i)
    json_request = request.json()
    for dict_item in json_request:
        if dict_item["type"] == "directory":
            item = dict_item["name"]
            item = item.replace(" ", "%20")
            print("Name: " + item)
            URLs_List.append(i + item + "/")
        if dict_item["type"] == "file":
            item = dict_item["name"]
            item = item.replace(" ", "%20")
            print("Name: " + item)
            files_List.append(i + item)

print(URLs_List)
print(files_List)
