#!/usr/bin/python
#wczytywanie do obiektu z pliku .yaml i weryfikacja poprawności składni pliku
import yaml
def open_yaml('pathFile2.yaml'):
    try:
        with open('pathFile2.yaml', 'r') as plik:
            a = yaml.safe_load(plik)
            return a
    except yaml.YAMLError:
        print("Taki plik nie istnieje, sprawdź nazwę")
    except FileNotFoundError:
        print("Taki plik nie istnieje")
      else:
       print("Taki plik istnieje")
