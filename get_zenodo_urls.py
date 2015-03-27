"""Write a file containing data file urls from zenodo for a given DOI
example DOI is "10.5281/zenodo.16407"

usage: python get_zenodo_url.py DOI output_filename
"""

import sys
import requests

#Zenodo Access token - use Phil's for demo
#TODO: take as argument when available from web app user config
ACCESS_TOKEN="koumNv9K77DM2mehN1pEzOpuzjV89OhpHhSldUWx877Y6R5LniXMTA8iU1hD"

#DOI & output file from command line args
#TODO error handling!
doi = sys.argv[1]
output_filename = sys.argv[2]

def get_dep_id(doi):
	
	"""get the deposition id for the DOI"""
	
	response = requests.get("https://zenodo.org/api/deposit/depositions/?access_token="+ACCESS_TOKEN)	

	json_data = response.json()
	
	for deposition in json_data:
		if deposition["doi"]==str(doi):
			dep_id=deposition["id"]	
	return dep_id


dep_id = get_dep_id(doi)

url="https://zenodo.org/api/deposit/depositions/"+str(dep_id)+"?access_token=koumNv9K77DM2mehN1pEzOpuzjV89OhpHhSldUWx877Y6R5LniXMTA8iU1hD"

deposition_json = requests.get(url).json()
	
with open(output_filename, 'w')as f:

	for dep_file in deposition_json["files"]:
		file_id=dep_file["id"]
		url="https://zenodo.org/api/deposit/depositions/"+str(dep_id)+"/files/"+ str(file_id) +"?access_token=koumNv9K77DM2mehN1pEzOpuzjV89OhpHhSldUWx877Y6R5LniXMTA8iU1hD"
		file_json = requests.get(url).json()
		file_url = "https://zenodo.org/record/"+str(dep_id)+"/files/"+str(file_json["filename"])
	
		f.write(file_json["filename"]+"	"+file_url+"\n")
