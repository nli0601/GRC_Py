import xml.etree.ElementTree as ET
import datetime

today = datetime.date.today()
today_string = today.strftime('%Y%m%d')

## API
#
# import requests
# from requests.auth import HTTPBasicAuth

# urlUserReq='https://usclwsapdg101.US.TDWORLDWIDE.COM:1443/sap/bc/srt/rfc/sap/grac_user_existing_assgn_ws/010/grac_user_existing_assgn_ws/grac_user_existing_assgn_ws_binding'
# headers = {'content-type': 'text/xml'}
# body = '''<?xml version='1.0' encoding='UTF-8'?>
#          <SOAP-ENV:Envelope xmlns:SOAP-ENV='http://schemas.xmlsoap.org/soap/envelope/' SOAP-ENV:encodingStyle='http://schemas.xmlsoap.org/soap/encoding/'>

#             <SOAP-ENV:Body><n0:GracIdmUserAsignmtServices xmlns:n0='urn:sap-com:document:sap:soap:functions:mc-style'>
#             <UserId>045292</UserId>
#         </n0:GracIdmUserAsignmtServices></SOAP-ENV:Body>
#          </SOAP-ENV:Envelope>'''

# response = requests.post(urlUserReq,data=body,headers=headers, auth=HTTPBasicAuth('', ''))
# print(response.content)


systemList = []


def xmlReading():
    tree_in = ET.parse('030322.xml')
    root_in = tree_in.getroot()   
    for child in root_in.findall('item'):
        sys_type = child.find('Type').text
        sys_name = child.find('Item').text
        sys_status = child.find('Status').text
        if sys_type == 'SYS' and sys_name.startswith('TG_') == True and sys_status !='EXPIRED':
            sys_element = child.find('Item').text
            systemList.append(sys_element)
    # print(len(systemList))


# Generation of xml file.
#
#
def xmlGeneration():
    root_out = ET.Element('RequestedLineItem')
    for child in systemList:
        item = ET.SubElement(root_out, 'item')
        ET.SubElement(item, 'ItemName').text = child
        ET.SubElement(item, 'Connector').text = child
        ET.SubElement(item, 'ProvItemType').text = 'SYS'
        ET.SubElement(item, 'ValidFrom').text = today_string
        ET.SubElement(item, 'ValidTo').text = today_string
        ET.SubElement(item, 'ProvAction').text = '002'
    tree_out = ET.ElementTree(root_out)
    tree_out.write('output.xml')

def main():
    xmlReading()
    xmlGeneration()

if __name__ == '__main__':
    main()


