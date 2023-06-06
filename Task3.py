#zapis danych z obiektu do pliku w formacie i zgodnie ze składnią .json
#!/usr/bin/python
import json
def save_json(a, save_file):
    try:
        with open(save_file, 'w') as plik:
            json.dump(a, plik)
        print("Udana konwersja do formatu JSON")
    except Exception:
        print("Błąd")
