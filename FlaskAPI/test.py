import requests

# Test for api.py file

BASE = "http://127.0.0.1:5000/"

# data = [
#     {'likes': 99, 'name': 'GitHub Advanced', 'views': 86_00},
#     {'likes': 3110, 'name': 'SQLite explained in 100seconds', 'views': 31_000},
#     {'likes': 71_000, 'name': 'REST API for Dummies', 'views': 100_000}
# ]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), json=data[i])
#     print(response.json())

# input()
# response = requests.delete(BASE + "video/0")
# print(response)
input()
response = requests.patch(BASE + "video/1", json={'views': 50_000, 'likes': 20020})
print(response.json())

# response = requests.put(BASE + "video/1", json={"likes": 1000, "name": "JS in 100seconds", "views": 1_000_000})
# print(response.json())
# input()
# response = requests.get(BASE + "video/1")
# print(response.json())