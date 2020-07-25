import json
import xmltodict

with open("C:\Users\Bruno Simoes\Google Drive\Georgian College\Second Term\Business Intelligence\Talentd Class Activity\stackoverflow.com-Posts\Posts.xml", 'r') as f:
    xmlString = f.read()

print("XML input (sample.xml):")
print(xmlString)

jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)

print("\nJSON output(output.json):")
print(jsonString)

with open("output.json", 'w') as f:
    f.write(jsonString)