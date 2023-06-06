#!/usr/bin/python
#wczytywanie do obiektu z pliku .json i weryfikacja poprawności składni pliku
import json
def open_json('pathFile1.json'):
    try:
        with open('pathFile1.json', 'r') as plik:
            a = json.load(plik)
            return a
    except json.JSONDecodeError:
        print("Taki plik nie istnieje, sprawdź nazwę")
    except FileNotFoundError:
        print("Taki plik nie istnieje")
    else:
        print("Taki plik istnieje")
