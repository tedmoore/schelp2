# HIDProto

*Prototype HID device to match with HIDFunc*

**Categories:** External Control>HID

**Related:** [HIDFunc](../Classes/HIDFunc.md), [HIDdef](../Classes/HIDdef.md), [HIDElementProto](../Classes/HIDElementProto.md), [HID](../Classes/HID.md), [HIDInfo](../Classes/HIDInfo.md), [Working_with_HID](../Guides/Working_with_HID.md)

## Description

Human input devices can be used as controllers for making music. This class can be used in conjunction with [HIDFunc](../Classes/HIDFunc.md) or [HIDdef](../Classes/HIDdef.md) to match incoming messages with a particular [HID](../Classes/HID.md) device.
HIDProto has all the variables that specify an HID device. The more of these variables you specify, the more need to be matched when filtering the incoming HID data.


## Class Methods

### `new`
Create a new instance of HIDProto.
### `newType`
Create a new instance of HIDProto based on usage and usagePage of the device.**Arguments:**

| Argument | Description |
|----------|-------------|
| `uName` | Name of the usage id |  
| `pName` | Name of the usage page id |  
**Returns:** an HIDProto
### `newProduct`
Create a new instance of HIDProto based on the product information.**Arguments:**

| Argument | Description |
|----------|-------------|
| `pName` | The product name to match. |  
| `vName` | The vendor name to match. |  
**Returns:** an HIDProto
### `newFromDict`
Create a new instance of HIDProto based on an IdentityDictionary with a set of parameters to match.**Arguments:**

| Argument | Description |
|----------|-------------|
| `dict` | An IdentityDictionary with a set of parameters to match. The keys in the dictionary should be one of the instance variables of HIDProto. |  
**Returns:** an HIDProto

## Instance Methods


### Instance variables that can be used to match a device
### `id`
The device id that should be matched. This is dependent on the order of opening HID devices.
### `productName`
The product name to match (see also [HIDInfo](../Classes/HIDInfo.md)).
### `vendorName`
The vendor name to match (see also [HIDInfo](../Classes/HIDInfo.md)).
### `productID`
The product id to match (see also [HIDInfo](../Classes/HIDInfo.md)).
### `vendorID`
The vendor id to match (see also [HIDInfo](../Classes/HIDInfo.md)).
### `interfaceNumber`
The interface number to match (see also [HIDInfo](../Classes/HIDInfo.md)).
### `releaseNumber`
The release number to match (see also [HIDInfo](../Classes/HIDInfo.md)).
### `serialNumber`
The serial number to match (see also [HIDInfo](../Classes/HIDInfo.md)).
### `path`
The path to match (see also [HIDInfo](../Classes/HIDInfo.md)).
### `usage`
The usage ID of the device to match (see also [HIDInfo](../Classes/HIDInfo.md)).
### `usagePage`
The usage page ID of the device to match (see also [HIDInfo](../Classes/HIDInfo.md)).
### `usageName`
The usage name of the device to match (see also [HIDInfo](../Classes/HIDInfo.md)).
### `pageName`
The page name of the device to match (see also [HIDInfo](../Classes/HIDInfo.md)).

### Methods to match
### `matches`
Match the argument with the template.**Arguments:**

| Argument | Description |
|----------|-------------|
| `hid` | An instance of HID. |  
**Returns:** a Boolean indicating whether the incoming HID matches the template
### `shouldMatch`
The variables that should be matched when filtering**Returns:** a Set with variable names.

### Methods to add matching parameters
### `addTypeMatch`
Add a match for usage name and usage page name of the device.**Arguments:**

| Argument | Description |
|----------|-------------|
| `uName` | The usage name to match |  
| `pName` | The page name to match |  

### `addProductMatch`
Add a match for product name and vendor name of the device.**Arguments:**

| Argument | Description |
|----------|-------------|
| `pName` | The product name to match |  
| `vName` | The vendor name to match |  

### `addDictionaryMatch`
Add an IdentityDictionary with a set of parameters to match. The keys in the dictionary should be one of the instance variables of HIDProto.**Arguments:**

| Argument | Description |
|----------|-------------|
| `dict` | An IdentityDictionary with a set of parameters to match. |  


## Examples


```supercollider
b = HIDProto.newFromDict((path: "/dev/hidraw2"));

a = HIDFunc.usage({ |...args| args.postln }, \X, deviceInfo: b);
a.free

b = HIDProto.newType(\Mouse, \GenericDesktop);

a = HIDFunc.usage({ |...args| args.postln }, \X, deviceInfo: b);
a.free;

b = HIDProto.newProduct("USB Mouse", "Logitech");

a = HIDFunc.usage({ |...args| args.postln }, \X, deviceInfo: b);
a.free;
```




