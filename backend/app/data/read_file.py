import json


def read_file():
    try:
        with open("favorites.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(e)
        return []




def write_file(favorites):
    try:
        with open("favorites.json", "w", encoding="utf-8") as file:
            json.dump(favorites, file, indent=4)
    except Exception as e:
        print(e)
        
        