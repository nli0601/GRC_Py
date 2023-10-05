import xml.etree.ElementTree as ET

treeIn = ET.parse('sample.xml')
rootIn = treeIn.getroot()

# print (root.tag, root.attrib)
# print (len(root))


# print (root[0][7].text)
# print (len(root[0]))

# systemList = []
# for child in root:
#     if child[1].text == "SYS":
#         systemList.append(child[0].text)

# print (systemList)

rootOut = ET.Element('UserExistingAssignment')

item = ET.SubElement(rootOut, "item")

ET.SubElement(item, "ItemName").text = "some value1"
ET.SubElement(item, "Type").text = "some vlaue2"
ET.SubElement(item, "Connector").text = "some vlaue3"
ET.SubElement(item, "Status").text = "some vlaue4"
ET.SubElement(item, "ProvAction").text = "some vlaue5"
ET.SubElement(item, "ProvItemType").text = "some vlaue6"

tree = ET.ElementTree(rootOut)
tree.write("filename.xml")
