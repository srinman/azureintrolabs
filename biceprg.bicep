targetScope = 'subscription'

resource resourceGroup 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: 'demoresourcegroup2'
  location: 'eastus2'
}
