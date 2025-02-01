provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "demoresourcegrouptf"
  location = "eastus2"
}