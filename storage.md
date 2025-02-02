# Azure Storage 

## Azure Storage Account

Azure Storage is a Microsoft-managed service providing highly available, secure, durable, scalable, and redundant storage. Azure Storage consists of the following data services: 

- Azure Blobs (object storage)
- Azure Files (file shares)
- Azure Queues (message queues)
- Azure Tables (NoSQL store)

Azure Storage Account is a unique namespace in Azure that provides storage services. The storage account provides a unique namespace for your Azure Storage data that is accessible from anywhere in the world over HTTP or HTTPS. Data in your Azure storage account is durable and highly available, secure, and massively scalable.

### Create a Storage Account

```bash
# Create a resource group
az group create --name myResourceGroup --location eastus

# Create a storage account
az storage account create --name mystorageaccount --resource-group myResourceGroup --location eastus --sku Standard_LRS
```

### List Storage Accounts

```bash
az storage account list --resource-group myResourceGroup --output table
```

### Get Storage Account Keys

```bash
az storage account keys list --account-name mystorageaccount --resource-group myResourceGroup --output table
```

### Create a Blob Container

```bash
az storage container create --name mycontainer --account-name mystorageaccount --account-key <account-key>
```

### Upload a Blob

```bash
az storage blob upload --container-name mycontainer --file /path/to/file --name myblob --account-name mystorageaccount --account-key <account-key>
```

### List Blobs

```bash
az storage blob list --container-name mycontainer --account-name mystorageaccount --account-key <account-key> --output table
```

### Download a Blob

```bash
az storage blob download --container-name mycontainer --file /path/to/file --name myblob --account-name mystorageaccount --account-key <account-key>
```

### Delete a Blob

```bash
az storage blob delete --container-name mycontainer --name myblob --account-name mystorageaccount --account-key <account-key>
```

## Azure Files

Azure Files offers fully managed file shares in the cloud that are accessible via the industry-standard Server Message Block (SMB) protocol. Azure file shares can be mounted concurrently by cloud or on-premises deployments of Windows, macOS, and Linux.

### Create an Azure File Share

```bash
az storage share create --name myshare --account-name mystorageaccount --account-key <account-key>
```

### List Azure File Shares

```bash
az storage share list --account-name mystorageaccount --account-key <account-key> --output table
```

### Upload a File to Azure File Share

```bash
az storage file upload --share-name myshare --source /path/to/file --account-name mystorageaccount --account-key <account-key>
```

### List Files in Azure File Share

```bash
az storage file list --share-name myshare --account-name mystorageaccount --account-key <account-key> --output table
```

## Azure Queues

Azure Queue storage is a service for storing large numbers of messages that can be accessed from anywhere in the world via authenticated calls using HTTP or HTTPS. A single queue message can be up to 64 KB in size, and a queue can contain millions of messages.

### Create a Queue

```bash
az storage queue create --name myqueue --account-name mystorageaccount --account-key <account-key>
```

### List Queues

```bash
az storage queue list --account-name mystorageaccount --account-key <account-key> --output table
```

### Enqueue a Message

```bash
az storage message put --queue-name myqueue --content "Hello, World!" --account-name mystorageaccount --account-key <account-key>
```

### Dequeue a Message

```bash
az storage message get --queue-name myqueue --account-name mystorageaccount --account-key <account-key>
```

## Azure Tables

Azure Table storage is a service that stores structured NoSQL data in the cloud, providing a key/attribute store with a schemaless design. Because Table storage is schemaless, it's easy to adapt your data as the needs of your application evolve.

### Create a Table

```bash
az storage table create --name mytable --account-name mystorageaccount --account-key <account-key>
```

### List Tables

```bash
az storage table list --account-name mystorageaccount --account-key <account-key> --output table
```

### Insert an Entity

```bash
az storage entity insert --table-name mytable --entity PartitionKey=part1 RowKey=row1 Name=John Age=25 --account-name mystorageaccount --account-key

```


## Azure Storage Explorer

Azure Storage Explorer is a standalone app that enables you to easily work with Azure Storage data on Windows, macOS, and Linux. You can connect to Azure Storage accounts or local storage, manage your blobs, files, queues, and tables, and easily work with Azure Data Lake Storage.

Download Azure Storage Explorer from [here](https://azure.microsoft.com/en-us/features/storage-explorer/).


## Azure Storage Pricing

Azure Storage pricing varies based on the type of storage service you choose, the region in which your storage account is located, the redundancy option chosen, and the amount of data stored or transferred. You can use the Azure Pricing Calculator to estimate the cost of using Azure Storage based on your requirements.

For more information on Azure Storage pricing, visit the [Azure Storage Pricing page](https://azure.microsoft.com/en-us/pricing/details/storage/).

## Azure Storage Security

Azure Storage provides several security features to help you secure your data, including:

- Azure Storage Firewalls and Virtual Networks: You can control access to your storage account by using Azure Storage firewalls and virtual networks. This feature allows you to create a virtual network rule that enables you to grant access to your storage account from specific virtual networks or IP addresses.

- EntraID - https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-access-azure-active-directory 

- Azure Storage Encryption: Azure Storage provides encryption at rest to help protect your data. Azure Storage automatically encrypts your data before persisting it to storage and decrypts it before retrieval.



## Azure Storage Options 

https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/storage-options 



## Demo  

```bash
export BLOB_ENDPOINT="https://srinmanntdemo.blob.core.windows.net/"
export CONTAINER_NAME="container1"
export TARGET_BLOB="blob1"
export BLOB_SAS_KEY="<your-sas-key>"
```

Run the following commands to upload a file to Azure Blob Storage:

```bash
echo "localfiledata" > localfile.txt
python blobwrite.py
```










