import xml.etree.ElementTree as ET

systemList = []
# Reading xml file

def xmlReading():
    treeIn = ET.parse('sample.xml')
    rootIn = treeIn.getroot()   
    for child in rootIn.findall('item'):
        sysType = child.find('Type').text
        if sysType == 'SYS':
            systemName = child.find('Item').text
            systemList.append(systemName)


# Generation of xml file.
#
#
def xmlGeneration():
    rootOut = ET.Element('RequestedLineItem')
    for child in systemList:
        item = ET.SubElement(rootOut, "item")
        ET.SubElement(item, "ItemName").text = child
        ET.SubElement(item, "Connector").text = child
        ET.SubElement(item, "ProvItemType").text = "SYS"
        # replace with current date - datetime etc...
        ET.SubElement(item, "ValidFrom").text = "20231006"
        ET.SubElement(item, "ValidTo").text = "20231006"
        ET.SubElement(item, "ProvAction").text = "002"
    tree = ET.ElementTree(rootOut)
    tree.write("filename.xml")

def main():
    xmlReading()
    xmlGeneration()

if __name__ == "__main__":
        main()