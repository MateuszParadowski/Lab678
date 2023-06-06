#!/usr/bin/python
#zapis danych z obiektu do pliku w formacie i zgodnie ze składnią .yml
def save_yaml(a, 'pathFile2.yaml'):
    try:
        with open('pathFile2.yaml', 'w') as plik:
            yaml.dump(a, plik)
        print("Udana konwersja do formatu YAML")
    except Exception:
        print("Błąd")
