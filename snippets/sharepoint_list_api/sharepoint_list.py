import requests
import yaml
from requests_ntlm2 import HttpNtlmAuth


#	Load details from the YAML file
with open('sharepoint_list_details.yaml', 'r') as file:
	sharepoint_variables = yaml.safe_load(file)

sharepoint_base_url_python = sharepoint_variables['sharepoint_base_url_python']
sharepoint_list_name = sharepoint_variables['sharepoint_list_name']
sharepoint_list_query = sharepoint_variables['sharepoint_list_query']

#	Assemble the full URL from those details
url = sharepoint_base_url_python.format(sharepoint_list_name) + sharepoint_list_query
# This creates the url: https://sharepoint.lab.martincrothers.com/ExampleSite/_api/Web/Lists/GetByTitle('
#               SupportTeamContacts')/items?$select=Title,email_address,incident_queue&$filter=(Title eq 'Network Team')


#	Disable console warnings for SSL verification
requests.packages.urllib3.disable_warnings()

#	Create the NTML authentication for OnPrem SharePoint
auth = HttpNtlmAuth('domain\\user', 'password')

headers = {'Accept': 'application/json;odata=verbose'}
response = requests.get(url, headers=headers, verify=False, auth=auth)
json = response.json()

#	This will output the value of the 'email_address' column where 'Title' = 'Network Team'.
print(json['d']['results'][0]['email_address'])