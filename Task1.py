#parsowanie argumentów przekazywanych przy uruchomieniu programu
#!/usr/bin/python
import argparse
parser = argparse.ArgumentParser(description='Tutaj możemy podać zwięzły opis naszego skryptu')
parser.add_argument('filename', help="Opis tego argumentu (krótkie wyjaśnienie co przyjmuje) - tutaj uznajmy że nazwę pliku")
args = parser.parse_args()
parser.add_argument('-a', '--argument', help="Nasz opcjonalny argument", required=False)
parser.add_argument('-i', '--ilosc', help="Argument o konkretnym typie i wartością domyślną", type=int, default=5, required=False)
args = parser.parse_args()
print("Podana nazwa pliku: ", args.filename)
print("Wartosc argumentu dodatkowego: ", args.argument)
print("Wartosc argumentu z typem i domyslna wartoscia: ", args.ilosc)
