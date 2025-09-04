import os, urllib.request

url = "https://gist.githubusercontent.com/trantuyen082001/1fc2f5c0ad1507f40e721e6d18b34138/raw/heart.csv"
path = os.path.join("..", "data", "heart.csv")

os.makedirs("../data", exist_ok=True)

if not os.path.exists(path):
    print("Downloading dataset...")
    urllib.request.urlretrieve(url, path)
    print("Saved to", path)
else:
    print("Dataset already exists.")
