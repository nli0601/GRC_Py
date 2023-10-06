import xml.etree.ElementTree as ET
import datetime

today = datetime.date.today()
todayString = today.strftime('%Y%m%d')

## API
#
# import requests
# from requests.auth import HTTPBasicAuth

# urlUserReq='https://usclwsapdg101.US.TDWORLDWIDE.COM:1443/sap/bc/srt/rfc/sap/grac_user_existing_assgn_ws/010/grac_user_existing_assgn_ws/grac_user_existing_assgn_ws_binding'
# headers = {'content-type': 'text/xml'}
# body = """<?xml version="1.0" encoding="UTF-8"?>
#          <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">

#             <SOAP-ENV:Body><n0:GracIdmUserAsignmtServices xmlns:n0="urn:sap-com:document:sap:soap:functions:mc-style">
#             <UserId>045292</UserId>
#         </n0:GracIdmUserAsignmtServices></SOAP-ENV:Body>
#          </SOAP-ENV:Envelope>"""

# response = requests.post(urlUserReq,data=body,headers=headers, auth=HTTPBasicAuth('', ''))
# print(response.content)


systemList = []
# Reading xml file

def xmlReading():
    treeIn = ET.parse('sample.xml')
    rootIn = treeIn.getroot()   
    for child in rootIn.findall('item'):
        sysType = child.find('Type').text
        sysName = child.find('Item').text
        if sysType == 'SYS' and sysName.startswith('TG_') == True:
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
        ET.SubElement(item, "ValidFrom").text = todayString
        ET.SubElement(item, "ValidTo").text = todayString
        ET.SubElement(item, "ProvAction").text = "002"
    treeOut = ET.ElementTree(rootOut)
    treeOut.write("output.xml")

def main():
    xmlReading()
    xmlGeneration()

if __name__ == "__main__":
        main()


