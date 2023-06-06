#!/usr/bin/python
import yaml

yaml_file = """
---
 focus: "Samochód, model Forda "
 saturn: "Planeta w układzie słonecznym"
 powierzchnia: 510,22
 ocean: true
 Dni: 5
 Waluty:
   - dolar
   - złotówka
   - euro
   - funt
 wakacje:
   transport: samolot
   nocleg: hotel
   posiłki: "na miejscu"
"""

x = yaml.load(yaml_file)
print(x)
print(type(x))
