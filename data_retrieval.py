import requests
import json


def fetch_aurora_data():
    # Fetch data from Aurora
    response = requests.get(
        "https://services.swpc.noaa.gov/json/ovation_aurora_latest.json"
    )
    data = response.json()
    return data


def fetch_hpi_data():
    # Fetch data from HPI
    response = requests.get(
        "https://services.swpc.noaa.gov/text/aurora-nowcast-hemi-power.txt"
    )
    data = response.text

    return data
