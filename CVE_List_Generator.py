import requests
import json
 

def main():
    content = requests.get("https://cve.circl.lu/api/last")
    Json = content.json()

    for item in Json:
       
        print("{}  {}".format("Vuln Numbers : " , item['id']))
        print("{}  {}".format("Description  : " , item['summary']))

main()