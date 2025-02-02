import os
import socket
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Get environment variables
blob_endpoint = os.getenv('BLOB_ENDPOINT')
container_name = os.getenv('CONTAINER_NAME')
target_blob = os.getenv('TARGET_BLOB')
blob_sas_key = os.getenv('BLOB_SAS_KEY')

# Resolve FQDN to IP
fqdn = blob_endpoint.split('//')[-1].split('/')[0]
resolved_ip = socket.gethostbyname(fqdn)
print(f"Resolved FQDN IP: {resolved_ip}")

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient(account_url=blob_endpoint, credential=blob_sas_key)

# Create a blob client using the local file name as the name for the blob
blob_client = blob_service_client.get_blob_client(container=container_name, blob=target_blob)

# Upload the file
local_file_path = "localfile.txt"
with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"File {local_file_path} uploaded to blob {target_blob} in container {container_name}.")