
"""Write a file containing data file urls from zenodo for a given DOI
example DOI is "10.5281/zenodo.16407"

usage: python get_zenodo_url.py DOI output_filename

"""

import sys
import requests


def get_dep_id(doi):

    """get the deposition id for the DOI"""

    response = requests.get(ZENODO_URL_BASE + "?access_token=" + ACCESS_TOKEN)

    json_data = response.json()

    for deposition in json_data:
        if deposition["doi"] == str(doi):
            dep_id = deposition["id"]
    return dep_id


ZENODO_URL_BASE="https://zenodo.org/api/deposit/depositions/"


#Zenodo Access token - use Phil's for demo
#TODO: take as argument when available from web app user config
ACCESS_TOKEN="koumNv9K77DM2mehN1pEzOpuzjV89OhpHhSldUWx877Y6R5LniXMTA8iU1hD"

#DOI & output file from command line args
#TODO error handling!
doi = sys.argv[1]
output_filename = sys.argv[2]

#Get data file meta data from Zenodo
dep_id = get_dep_id(doi)
url = ZENODO_URL_BASE + str(dep_id) + "?access_token=" + ACCESS_TOKEN
deposition_json = requests.get(url).json()

#Write data file names and Zenodo urls to output file
with open(output_filename, 'w') as f:

    for dep_file in deposition_json["files"]:
        file_id = dep_file["id"]
        url = ZENODO_URL_BASE + str(dep_id) + "/files/" + str(file_id) + "?access_token=" + ACCESS_TOKEN
        file_json = requests.get(url).json()
        file_url = "https://zenodo.org/record/" + str(dep_id) + "/files/" + str(file_json["filename"])

        f.write(file_json["filename"] + "	" + file_url + "\n")
