#!/opt/globus/bin/python
#Must be run on box that has a GCSv5 install

import globus_sdk

client_id=""
client_secret=""
admin_uuid=""
endpoint_uuid=""

scopes = 'urn:globus:auth:scope:transfer.api.globus.org:all'

def main():
    client = globus_sdk.ConfidentialAppAuthClient(client_id=client_id, client_secret=client_secret)
    token_response = client.oauth2_client_credentials_tokens(requested_scopes=scopes)

    transfer_token = token_response['access_token']
    
    authorizer = globus_sdk.AccessTokenAuthorizer(transfer_token)
    api = globus_sdk.TransferClient(authorizer=authorizer)

    result = api.add_endpoint_role(endpoint_uuid, { "DATA_TYPE": "role", "principal_type": "identity", "principal": admin_uuid, "role": "administrator" })
    print(result)

if __name__ == "__main__":
    main()
