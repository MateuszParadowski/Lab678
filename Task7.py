#!/usr/bin/python
import xml.etree.ElementTree as et
d = et.parse("pathFile3.xml")
d.write("pathFile3.1.xml",encoding="utf-8")
