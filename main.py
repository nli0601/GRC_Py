import xml.etree.ElementTree as ET

mytree = ET.parse('sample.xml')
myroot = mytree.getroot()
print(myroot)