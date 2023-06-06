#!/usr/bin/python
#zapis danych z obiektu do pliku w formacie i zgodnie ze składnią .json
import json
def save_json(a, 'pathFile1.json'):
    try:
        with open('pathFile1.json', 'w') as plik:
            json.dump(a, plik)
        print("Udana konwersja do formatu JSON")
    except Exception:
        print("Błąd")
