#wczytywanie do obiektu z pliku .json i weryfikacja poprawności składni pliku
#!/usr/bin/python
import json
def open_json(open_file):
    try:
        with open(open_file, 'r') as plik:
            a = json.load(plik)
            return a
    except json.JSONDecodeError:
        print("Taki plik nie istnieje, sprawdź nazwę")
    except FileNotFoundError:
        print("Taki plik nie istnieje")
    else:
        print("Taki plik istnieje")
