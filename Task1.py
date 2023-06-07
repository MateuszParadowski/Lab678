#!/usr/bin/python
#parsowanie argumentów przekazywanych przy uruchomieniu programu
import sys
if len(sys.argv) != 3:
        print("Dozwolone sa tylko dwa argumenty")
        return
else:
        pass

open_file = sys.argv[1]
save_file = sys.argv[2]

a = None

if open_file.endswith('.json'):
        a = open_json(open_file)
elif open_file.endswith('.yaml'):
        a = open_yaml(open_file)
elif plik_wej.endswith('.xml'):
        a = open_xml(open_file)
else:
        print("Błędny format pliku.")
        return

if save_file.endswith('.json'):
        save_json(a, save_file)
elif plik_wyj.endswith('.yaml'):
        save_yaml(a, save_file)
elif plik_wyj.endswith('.xml'):
        save_xml(a, save_file)
else:
        print("Błędny format pliku.")
        return
