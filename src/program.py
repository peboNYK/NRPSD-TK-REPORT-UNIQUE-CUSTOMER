import requests
import os
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

# Set the path to the file you want to upload
file_path = 'testdata.csv'

# Set the name of the Teams channel where you want to upload the file
teams_channel_id = 'your_teams_channel_id'

# Set your Azure AD app's client ID and client secret
client_id = 'your_client_id'
client_secret = 'your_client_secret'
tenant_id = 'your_tenant_id'

# Authenticate and get the access token
token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
token_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'https://graph.microsoft.com/.default'
}
token_r = requests.post(token_url, data=token_data)
token = token_r.json().get('access_token')

# Upload the file
upload_url = f'https://graph.microsoft.com/v1.0/teams/{teams_channel_id}/drive/root:/path/to/file/{os.path.basename(file_path)}:/content'
headers = {
    'Authorization': 'Bearer ' + token
}
with open(file_path, 'rb') as file:
    file_content = file.read()
    requests.put(upload_url, headers=headers, data=file_content)

print('File uploaded successfully!')
