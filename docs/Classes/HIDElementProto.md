# HIDElementProto

*Prototype HID element to match with HIDFunc*

**Categories:** External Control>HID

**Related:** [HIDFunc](../Classes/HIDFunc.md), [HIDdef](../Classes/HIDdef.md), [HIDProto](../Classes/HIDProto.md), [HID](../Classes/HID.md), [HIDElement](../Classes/HIDElement.md), [HIDInfo](../Classes/HIDInfo.md), [Working_with_HID](../Guides/Working_with_HID.md)

## Description

Human input devices can be used as controllers for making music. This class can be used in conjunction with [HIDFunc](../Classes/HIDFunc.md) or [HIDdef](../Classes/HIDdef.md) to match incoming messages with a particular [HID](../Classes/HID.md) device.
HIDElementProto has all the variables that specify an HID element. The more of these variables you specify, the more need to be matched when filtering the incoming HID data.


## Class Methods


### `new`
Create a new instance of HIDElementProto.

### `newType`
Create a new instance of HIDElementProto based on usage id and usage page id of the element.**Arguments:**

| Argument | Description |
|----------|-------------|
| `uName` | Name of the usage ID to match |  
| `pName` | Name of the usage page to match |  
**Returns:** an HIDElementProto

### `newTypeID`
Create a new instance of HIDElementProto based on usage id and usage page id of the element.**Arguments:**

| Argument | Description |
|----------|-------------|
| `uID` | Usage ID to match |  
| `pID` | Usage page ID to match |  
**Returns:** an HIDElementProto

### `newFromDict`
Create a new instance of HIDElementProto based on an IdentityDictionary with a set of parameters to match.**Arguments:**

| Argument | Description |
|----------|-------------|
| `dict` | An IdentityDictionary with a set of parameters to match. The keys in the dictionary should be one of the instance variables of HIDElementProto. |  
**Returns:** an HIDElementProto

## Instance Methods


### Instance variables that can be used to match a device

### `id`
The element index that should be matched. This index may vary between operating systems (see also [HIDElement](../Classes/HIDElement.md)).

### `usageName`
The usage name of the element to match (see also [HIDElement](../Classes/HIDElement.md)).

### `pageName`
The usage page name of the element to match (see also [HIDElement](../Classes/HIDElement.md)).

### `usage`
The usage index of the element to match (see also [HIDElement](../Classes/HIDElement.md)).

### `usagePage`
The usage page index of the element to match (see also [HIDElement](../Classes/HIDElement.md)).

### `usageMin`
The minimum usage index of the element to match (see also [HIDElement](../Classes/HIDElement.md)).

### `usageMax`
The maximum usage index of the element to match (see also [HIDElement](../Classes/HIDElement.md)).

### `type`
The type of the element to match (see also [HIDElement](../Classes/HIDElement.md)).

### `typeSpec`
The typeSpec of the element to match (see also [HIDElement](../Classes/HIDElement.md)).

### `ioType`
The IO type of the element to match - input (1), output (2) or feature (3) (see also [HIDElement](../Classes/HIDElement.md)).

### `iotypeName`
The IO type of the element to match - `\input`, `\output` or `\feature` (see also [HIDElement](../Classes/HIDElement.md)).

### Methods to match

### `matches`
Match the argument with the template.**Arguments:**

| Argument | Description |
|----------|-------------|
| `ele` | An instance of HIDElement |  
**Returns:** a Boolean indicating whether the incoming HID matches the template

### `shouldMatch`
The variables that should be matched when filtering**Returns:** a Set with variable names.

### Methods to add matching parameters

### `addTypeMatch`
Add a match for usage name and usage page name of the element.**Arguments:**

| Argument | Description |
|----------|-------------|
| `uName` | The usage name to match |  
| `pName` | The page name to match |  


### `addTypeIDMatch`
Add a match for usage id and usage page id of the element.**Arguments:**

| Argument | Description |
|----------|-------------|
| `uID` | The usage id to match |  
| `pID` | The usage page id to match |  


### `addDictionaryMatch`
Add an IdentityDictionary with a set of parameters to match. The keys in the dictionary should be one of the instance variables of HIDElementProto.**Arguments:**

| Argument | Description |
|----------|-------------|
| `dict` | An IdentityDictionary with a set of parameters to match. |  


## Examples


```
// create an prototype element with usageName \X
c = HIDElementProto.new.usageName_(\X);
a = HIDFunc.proto({ |...args| args.postln }, c);
a.free;
```




