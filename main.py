import xml.etree.ElementTree as ET

tree = ET.parse('sample.xml')
root = tree.getroot()

print (root.tag)
print (len(root))