#!/usr/bin/python
#wczytywanie do obiektu z pliku .xml i weryfikacja poprawności składni pliku
import xmltodict

def open_xml('pathFile3.xml'):
    try:
        with open('pathFile3.xml', 'r') as plik:
            a = xmltodict.parse(plik.read())
            return a
    except FileNotFoundError:
        print("Taki plik nie istnieje")
    else:
        print("Taki plik istnieje")
