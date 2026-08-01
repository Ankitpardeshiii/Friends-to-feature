import json

def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)