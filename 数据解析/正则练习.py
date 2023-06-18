import requests

url = "https://i0.hdslb.com/bfs/archive/4c1081869f5a6096a40357a285b38b0d6af3e26f.jpg"
reponse = requests.get(url).content
with open("text/img.jpg","wb") as fp:
    fp.write(reponse)