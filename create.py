import json
import os

def main():
    component = input("Choose component (incendium): ")
    lang = input("Choose language (en_us): ")

    with open(f"{os.getcwd()}/{component}/en_us.json", 'r') as f:
        data = json.load(f)

    for string in data:
        data[string] = ""

    with open(f"{os.getcwd()}/{component}/{lang}.json", 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    main()