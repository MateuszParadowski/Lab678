#!/usr/bin/python
#zapis danych z obiektu do pliku w formacie i zgodnie ze składnią .xml
import xmltodict
def save_xml(a, 'pathFile3.xml'):
    try:
        with open(a, 'w') as plik:
            xml_str = xmltodict.unparse('pathFile3.xml', pretty=True)
            plik.write(xml_str)
        print("Udana konwersja do formatu XML")
    except Exception:
        print("Błąd")
