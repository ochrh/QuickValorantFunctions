import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

# DICTIONARY CONTAINING MAPS UUID
maps_dict = {
    "Ascent" : "7eaecc1b-4337-bbf6-6ab9-04b8f06b3319",
    "Split" : "d960549e-485c-e861-8d71-aa9d1aed12a2",
    "Fracture" : "b529448b-4d60-346e-e89e-00a4c527a405",
    "Bind" : "2c9d57ec-4431-9c5e-2939-8f9ef6dd5cba",
    "Breeze" : "2fb9a4fd-47b8-4e7d-a969-74b4046ebd53",
    "District" : "690b3ed2-4dff-945b-8223-6da834e30d24",
    "Kasbah" : "12452a9d-48c3-0b02-e7eb-0381c3520404",
    "Drift" : "2c09d728-42d5-30d8-43dc-96a05cc7ee9d",
    "Glitch" : "d6336a5a-428f-c591-98db-c8a291159134",
    "Abyss" : "224b0a95-48b9-f703-1bd8-67aca101a61f",
    "Lotus" : "2fe4ed3a-450a-948b-6d6b-e89a78e680a9",
    "Sunset" : "92584fbe-486a-b1b2-9faa-39b0f486b498",
    "Basic Training" : "1f10dab3-4294-3827-fa35-c2aa00213cf3",
    "Icebox" : "e2ad5c54-4114-a870-9641-8ea21279579a",
    "The Range" : "ee613ee9-28b7-4beb-9666-08db13bb2244",
    "Haven" : "2bee0dc9-4ffe-519b-1cbd-7fbe763a6047"
}

base_url = "https://valorant-api.com/v1/maps"

class SiteRoller(QWidget):
    def __init__(self):
        super().__init__()

def init_window():
    app = QApplication(sys.argv)
    site_roller = SiteRoller()
    site_roller.show()
    sys.exit(app.exec_())

def get_map_info(uuid):
    url = f"{base_url}/{map_uuid}"
    print(f"Acquiring data from '{url}'...")
    response = requests.get(url)

    match response.status_code:
        case 200:
            fetched_info = response.json()
            return fetched_info
        case 400:
            print("Error")
        case 404:
            print("Error")


if __name__ == '__main__':
    map_uuid = "7eaecc1b-4337-bbf6-6ab9-04b8f06b3319"
    map_info = get_map_info(map_uuid)
    print(f"{map_info['data']}")
    print(f"{map_info['data']['displayName']}")
    print(len(maps_dict))