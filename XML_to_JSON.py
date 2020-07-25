import xmltodict
import json
with open('C:\Users\Bruno Simoes\Google Drive\Georgian College\Second Term\Business Intelligence\Talentd Class Activity\stackoverflow.com-Posts\Posts.xml') as xml_file:
    my_dict=xmltodict.parse(xml_file.read())
xml_file.close()
json_data=json.dumps(my_dict)
print(json_data)
