import requests
import json

# rsp=requests.get("http://localhost:3000/data")
# with open("data.json", "w") as f:
#     json_obj = json.dumps(rsp.json(), indent=3)
#     f.write(json_obj)
data = {
    "username": "Tasneem",
    "password": "12345"
}
login = requests.post("http://localhost:4000/login", json=data)
login = login.json()
print(login)
token = login['token']
parms =    {
    "city": "Chennai",
    "temp": 40
}
headers={"Authorization": f"Bearer {token}"}
rsp = requests.post("http://localhost:4000/insert", json=parms, headers=headers)
xyz=rsp.json()
print(xyz)

print("Hello World")
