"""Write a file containing data file urls from zenodo for a given DOI
example DOI is "10.5281/zenodo.16407"

"""

import sys
import requests
import pprint 

#import json
#pp = pprint.PrettyPrinter(indent=4)

#DOI supplied as only command line arg
doi = sys.argv[1]

def get_dep_id(doi):
	
	"""get a valid deposition id for the zenodo user"""

	response = requests.get("https://zenodo.org/api/deposit/depositions/?access_token=koumNv9K77DM2mehN1pEzOpuzjV89OhpHhSldUWx877Y6R5LniXMTA8iU1hD")
	
	json_data = response.json()
	
	for deposition in json_data:
		if deposition["doi"]==str(doi):
			dep_id=deposition["id"]	
	return dep_id


dep_id = get_dep_id(doi)

url="https://zenodo.org/api/deposit/depositions/"+str(dep_id)+"?access_token=koumNv9K77DM2mehN1pEzOpuzjV89OhpHhSldUWx877Y6R5LniXMTA8iU1hD"

deposition_json = requests.get(url).json()
	
files={}

for dep_file in deposition_json["files"]:
	file_id=dep_file["id"]
	url="https://zenodo.org/api/deposit/depositions/"+str(dep_id)+"/files/"+ str(file_id) +"?access_token=koumNv9K77DM2mehN1pEzOpuzjV89OhpHhSldUWx877Y6R5LniXMTA8iU1hD"
	file_json = requests.get(url).json()
	file_url = "https://zenodo.org/record/"+str(dep_id)+"/files/"+str(file_json["filename"])
	
	print(file_json["filename"]+"	"+file_url)
