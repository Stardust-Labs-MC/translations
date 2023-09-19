import json
import os

def main():
    lang = input("Choose language (ex: en_us): ")
    
    # Copy English strings
    for component in ["incendium", "terralith", "nullscape"]:
        with open(f"{os.getcwd()}/{component}/en_us.json", 'r') as f:
            data = json.load(f)

        for string in data:
            data[string] = ""

        # Duplicate into new lang
        with open(f"{os.getcwd()}/{component}/{lang}.json", 'w') as f:
            json.dump(data, f, indent=2)

    # Add new lang to lang list
    with open(f"{os.getcwd()}/languages.json", 'r') as f:
        langs = json.load(f)
    
    langs.append(lang)

    with open(f"{os.getcwd()}/languages.json", 'w') as f:
        json.dump(langs, f, indent=2)

if __name__ == '__main__':
    main()
