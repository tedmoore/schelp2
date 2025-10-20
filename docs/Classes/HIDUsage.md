# HIDUsage

*Helper class to read usage information from HID usage tables*

**Categories:** External Control>HID

**Related:** [HID](../Classes/HID.md), [HIDElement](../Classes/HIDElement.md), [HIDCollection](../Classes/HIDCollection.md), [Working_with_HID](../Guides/Working_with_HID.md)

## Description

HID functionality is described by the USB HID standard usage tables. Each element and collection has a usage page and index, describing the type of control that it provides. This class allows to query the name of a usage and page based on the indices read from the device. This class is primarily used internally by other HID classes.


## Class Methods



### `getUsageDescription`
Retrieve the standard usage name and pagename of an HID usage element or collection.**Arguments:**

| Argument | Description |
|----------|-------------|
| `usagePage` | usage page number |  
| `usage` | usage index |  
**Returns:** an Array with the pageName and usageName

### `hutDirectory`
Directory where the yaml files with the HID usage tables are stored.

### `readHUTFile`
Reads and parses the HID usage table file. Called from getUsageDescription to read in the usage table.**Arguments:**

| Argument | Description |
|----------|-------------|
| `yamlfile` | the filename of the yamlfile with a particular usage table, relative to the hutDirectory. |  
**Returns:** an IdentityDictionary representing the table

### `getUsageIds`
Retrieve usage id and page id from the usageName.**Arguments:**

| Argument | Description |
|----------|-------------|
| `usageName` | the usage name |  
**Returns:** an Array with the page id and the usage id

### `idsToName`
Retrieve the standard usage name and pagename of an HID usage element or collection.**Arguments:**

| Argument | Description |
|----------|-------------|
| `page` | the usage page id |  
| `usage` | the usage id |  
**Returns:** the usage name

### `usageIDsToName`
MultiLevelIdentityDictionary containing a map of page ids, usage ids to usage names.

### `usageNameToIDs`
IdentityDictionary containing a map of usageNames to page ids and usage ids.
## Examples

Get the usage description for a collection or element with usage page 1 and usage index 5

```
HIDUsage.getUsageDescription(1, 5);
```




