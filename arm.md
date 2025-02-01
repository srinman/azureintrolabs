# Azure Resource Manager  



## How to list resources in a subscription using Azure Resource Manager REST API

Reference:  
https://learn.microsoft.com/en-us/rest/api/resources/resources/list?view=rest-resources-2021-04-01#code-try-0   


```bash
# Log in to Azure
az login

# Get the access token and store it in ACCESS_TOKEN variable
ACCESS_TOKEN=$(az account get-access-token --query accessToken --output tsv)

# Get the subscription ID and store it in SUBSCRIPTIONID variable
SUBSCRIPTIONID=$(az account show --query id --output tsv)

# Use the access token and subscription ID in the curl command
curl -X GET \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  "https://management.azure.com/subscriptions/$SUBSCRIPTIONID/resources?api-version=2021-04-01"
```

## List resources in a subscription using Azure Resource Manager REST CLI command

```bash
# Get the subscription ID and store it in SUBSCRIPTIONID variable
SUBSCRIPTIONID=$(az account show --query id --output tsv)

# Use the subscription ID in the az rest command
az rest --method get --uri "https://management.azure.com/subscriptions/$SUBSCRIPTIONID/resources?api-version=2021-04-01"
```

**Note:** az rest and curl are using the same REST API to list resources in a subscription but curl requires an access token to authenticate the request. az rest command uses the Azure CLI authentication context to authenticate the request.



## Azure CLI command to list resources in a subscription  

```bash
az resource list --subscription $SUBSCRIPTIONID
```


## Bicep 

```bash
az deployment sub create --location eastus2 --template-file ./biceprg.bicep
```


## List all resource providers in a subscription

```bash
az provider list --output table
```


## Azure Policy 

```bash
az policy definition list --output table
```

```bash
az policy definition create --name "deny-westus2" --rules ./deny-westus2-policy.json --mode All
```

```bash
az policy assignment create --name "deny-westus2-assignment" --policy "deny-westus2" --scope "/subscriptions/$SUBSCRIPTIONID"
```

Try to create a resource in the westus2 region to see the policy in action.  

```bash
az policy assignment delete --name "deny-westus2-assignment" --scope "/subscriptions/$SUBSCRIPTIONID"
```


## Activity Log

The Azure Monitor activity log is a platform log that provides insight into subscription-level events.   

```bash
az monitor activity-log list-categories
az monitor activity-log list --output table 
az monitor activity-log list --start-time 2025-02-01 15:45:00 -o table   
```

In portal: 
- Go to Monitor
- Activity log
- Filter by subscription, resource group, resource type, etc.


