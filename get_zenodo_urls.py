
"""Write a file containing data file urls from zenodo for a given DOI and
zenodo access token. example DOI is "10.5281/zenodo.16407"

usage: python get_zenodo_url.py DOI token output_filename

"""

import sys
import json
import requests


def get_dep_id(doi, token):

    """get the deposition id for the DOI"""

    response = requests.get(ZENODO_URL_BASE + "?access_token=" + token)

    json_data = response.json()

    for deposition in json_data:
        if deposition["doi"] == str(doi):
            dep_id = deposition["id"]
    return dep_id


ZENODO_URL_BASE="https://zenodo.org/api/deposit/depositions/"


#DOI & output file from command line args
#TODO error handling!
doi = sys.argv[1]
token = sys.argv[2]
output_filename = sys.argv[3]

#Get data file meta data from Zenodo
dep_id = get_dep_id(doi, token)
url = ZENODO_URL_BASE + str(dep_id) + "?access_token=" + token
deposition_json = requests.get(url).json()

for dep_file in deposition_json["files"]:
    file_id = dep_file["id"]
    url = ZENODO_URL_BASE + str(dep_id) + "/files/" + str(file_id) + "?access_token=" + token
    file_json = requests.get(url).json()
    dep_file["url"] = "https://zenodo.org/record/" + str(dep_id) + "/files/" + str(file_json["filename"])

#Write data file names and Zenodo urls to output file
with open(output_filename, 'w') as f:
    f.write(json.dumps(deposition_json, indent = 2))
