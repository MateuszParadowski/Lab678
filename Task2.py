#!/usr/bin/python
import json
plik=open('pathFile1.json',encoding='utf-8')
obj=json.load(plik)
print(obj)
print(type(obj))
plik.close()
