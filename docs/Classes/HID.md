# HID

*This class provides access to human input devices, or in short HID, such as joysticks, gamepads, mice, keyboard, and so on.*

**Categories:** External Control>HID

**Related:** [HIDFunc](../Classes/HIDFunc.md), [Working_with_HID](../Guides/Working_with_HID.md), [HIDElement](../Classes/HIDElement.md), [HIDCollection](../Classes/HIDCollection.md), [HIDUsage](../Classes/HIDUsage.md), [HIDInfo](../Classes/HIDInfo.md)

## Description

Human input devices can be used as controllers for making music. This class provides you with access to them in a simple and transparent way.
The development of this SuperCollider implementation of HID access was funded by the SuperCollider community and BEK, Bergen Elektronisk Kunst, Bergen, Norway, [http://www.bek.no](http://www.bek.no)

### Introduction
In general using an Human Input Device follows this scheme:


**Find available devices:**
: `HID.findAvailable;`

**Print a readable list of available devices:**
: `HID.postAvailable;`

**Open a specific device:**
: `~myhid = HID.open(1103, 53251);`

**Set actions for specific elements:**
: `~myhid.elements[1].action = { |...args| args.postln };`See [Working_with_HID](../Guides/Working_with_HID.md) for a full introduction.






## Class Methods



### Finding devices

### `findAvailable`
queries the operating system which HID devices are attached to the system and can be accessed. When using HID this is the first method you need to execute, before you can access any device.**Returns:** an IdentityDictionary of available devices

### `available`
A dictionary of available devices, or rather info about them in an instance of [HIDInfo](../Classes/HIDInfo.md), populated by the method findAvailable**Returns:** an IdentityDictionary

### `postAvailable`
posts a human readable list of available HID devices and their properties (see also [HIDInfo](../Classes/HIDInfo.md))

### `findBy`
Find devices in the available device dictionary by specifying one or more characteristics of the device**Arguments:**

| Argument | Description |
|----------|-------------|
| `vendorID` | The vendor ID of the device, this is a number encoded by the device itself, and the same across platforms. |  
| `productID` | The product ID of the device, this is a number encoded by the device itself, and the same across platforms. |  
| `path` | The path of the device, this is a path defined by the operating system, and thus not the same across platforms, but essential to distinguish devices with the same vendor and product ID from each other. |  
| `serial` | The serial number of the device. This is dependent on the operating system, e.g. on Linux it is not set. |  
| `releaseNumber` | The release number of the device, this is a number encoded by the device itself, and the same across platforms. |  
**Returns:** an IdentityDictionary of devices the match the search query, or nil if no arguments are given

### `availableUsages`
A dictionary of available usages from all HIDs, populated automatically when devices are opened and closed.**Returns:** an IdentityDictionary

### `postAvailableUsages`
posts a human readable list of available HID usages and their properties (see also [HIDElement](../Classes/HIDElement.md) and [HIDUsage](../Classes/HIDUsage.md))


### Opening devices

### `open`
Open a device with a given vendorID, product ID and optionally a path.**Arguments:**

| Argument | Description |
|----------|-------------|
| `vendorID` | The vendor ID of the device |  
| `productID` | The product ID of the device |  
| `path` | (optional) The path in the operating system, e.g. "/dev/hidraw0" on Linux. If not specified, the method will look for a matching device in the device list, and open the first match it finds. |  
**Returns:** The HID device - an instance of HID.

### `new`
Same as HID.open

### `openPath`
Open a device using its path in the operating system**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | The path in the operating system, e.g. "/dev/hidraw0" on Linux |  
**Returns:** The HID device - an instance of HID.

### `openAt`
Open a device using its index in the dictionary of available devices**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The index into the dictionary of available devices |  
**Returns:** The HID device - an instance of HID.

### `openDevices`
A dictionary of the opened devices**Returns:** an IdentityDictionary


### Adding functions to HID events
Whenever data comes in from an opened HID device, there are two types of actions fired. An action for the incoming element data and an action for the device, indicating that there has been a change in one of the elements. In most cases you will want to use the first action; only in cases where the order of parsing the element data is important, you may want to use the second type - e.g. when dealing with very accurately timed button press combinations.

There are three levels where you can set actions:

- at the global level - called for any HID device, for any element
- at the device level - called for the specific device, for any element
- at the element level - called for the specific element of the specific device


Alternately, you can also use the [HIDFunc](../Classes/HIDFunc.md) interface.


### `debug`
When set to true, the incoming data from any opened HID device will be printed to the post window.

### `action`
Set or get the action to be performed upon receiving element data from the device. The function will be passed the following arguments: the value (mapped between 0 and 1), the raw value, element usage page, the element usage, the element id, the device id, the device (an instance of HID).**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | The function to be performed upon receiving element data from the device |  


### `addRecvFunc`
add a function to the internal FunctionList that will be evaluated whenever element data comes in from an open device. The arguments passed to the function are as defined above. Use this method if you want to add actions to HID functions from classes you write, so that you still keep the option to add an action on the fly from user code.**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | The function to be added to the list. |  


### `removeRecvFunc`
remove a function to the internal FunctionList that will be evaluated whenever data comes in from a device.**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | The function to remove from the list, this must be a reference to the Function that was originally added to the list |  


### `deviceAction`
set an action or function to be performed whenever there is an update to any device's elements.**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | The function to be performed upon receiving data from the device |  


### `addDevFunc`
add a function to the internal FunctionList that will be evaluated whenever data comes in from a device.**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | The function to be performed upon receiving data from the device |  


### `removeDevFunc`
remove a function to the internal FunctionList that will be evaluated whenever data comes in from a device.**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | The function to remove from the list, this must be a reference to the Function that was originally added to the list |  



### Managing the HID subsystem
The following methods are used internally to initialize and finalize the HID subsystem, but in rare cases you may wish to manage these methods manually.


### `initializeHID`
Initialize the HID subsystem, this method is called automatically when calling the method findAvailable.

### `running`
Indicates whether or not the HID subsystem is running.

### `closeAll`
This method is called automatically upon Shutdown, if the HID subsystem was initialized. It can be stopped manually, in order to save system resources. This method will close all opened HID devices.


## Instance Methods


### `elements`
An IdentityDictionary holding all the elements, i.e. controls, of the device
### `findElementWithUsage`
Find all elements with a certain usage and usagePage.**Arguments:**

| Argument | Description |
|----------|-------------|
| `elUsage` | The usage index of the element |  
| `elUsagePage` | The usage page of the element |  
**Returns:** an Array with the found elements
### `getElementWithID`
Get the element with the given index**Arguments:**

| Argument | Description |
|----------|-------------|
| `elid` | The index of the element |  
**Returns:** the HIDElement
### `close`
Close the HID device, closing a device is asynchronous. You can set a closeAction (see below), which will be performed when the device closes.
### `isOpen`
Returns true if the device is open, false if the device was closed.returns: a Boolean
### `collections`
An IdentityDictionary holding all the collections, i.e. groups of controls, of the device
### Adding functionality to the device

### `debug`
When set to true, the incoming data from this HID device will be printed to the post window.

### `closeAction`
Function to be performed when device is closed.

### `action`
Set or get the action to be performed upon receiving element data from the device. The function will be passed the following arguments: the value (mapped between 0 and 1), the raw value, element usage page, the element usage, the element id**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | The function to be performed upon receiving element data from the device |  


### `deviceAction`
set an action or function to be performed whenever there is an update to any of the device's elements.**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | The function to be performed upon receiving data from the device |  


### Posting human readable information about the device

### `postInfo`
Post the HIDInfo of this device in a human readable format

### `postCollections`
Post information about all the collections of this device in a human readable format

### `postElements`
Post information about all the elements of this device in a human readable format

### `postInputElements`
Post information about all the input elements of this device in a human readable format

### `postOutputElements`
Post information about all the output elements of this device in a human readable format

### `postFeatureElements`
Post information about all the feature elements of this device in a human readable format

### `postUsages`
Post information about all the usages of this device in a human readable format

### Properties of the device

### `info`
Retrieve the HIDInfo of this device**Returns:** an instance of HIDInfo

### `usage`
Retrieve the usage index of a collection of this device, or the main usage of the device (if called without an argument).**Arguments:**

| Argument | Description |
|----------|-------------|
| `collectionID` | The collection of which to retrieve the usage. Default is 0, which should define the primary usage of the device. |  
**Returns:** the usage index of this device

### `usageName`
Retrieve the usage name of a collection of this device, or the main usage of the device (if called without an argument). The name is looked up from the standardized HID usage tables using the usage index.**Arguments:**

| Argument | Description |
|----------|-------------|
| `collectionID` | The collection of which to retrieve the usage. Default is 0, which should define the primary usage of the device. |  
**Returns:** the usage name of this device

### `usagePage`
Retrieve the usage page index of a collection of this device, or the main page of the device (if called without an argument). The name is looked up from the standardized HID usage tables using the usage page index.**Arguments:**

| Argument | Description |
|----------|-------------|
| `collectionID` | The collection of which to retrieve the usage page. Default is 0, which should define the primary usage of the device. |  
**Returns:** the usage page index of this device

### `pageName`
Retrieve the page name of a collection of this device, or the main page of the device (if called without an argument). The name is looked up from the standardized HID usage tables using the usage page index.**Arguments:**

| Argument | Description |
|----------|-------------|
| `collectionID` | The collection of which to retrieve the usage page name. Default is 0, which should define the primary usage of the device. |  
**Returns:** the usage page name of this device

### `vendor`
Retrieve the vendor id of this device**Returns:** the vendor id

### `product`
Retrieve the product id of this device**Returns:** the product id

### `usages`
Retrieve the usages of the elements of this device.**Returns:** an IdentityDictionary with usages as keys and lists of elements as corresponding elements

## Examples


```
HID.findAvailable; // check which devices are attached
~myhid = HID.open(1103, 53251); // open the Run'N' Drive game controller

s.boot; // boot the server

Ndef(\sinewave, { |freq = 500, amp = 0.1| SinOsc.ar(freq, 0, amp * 0.2) });
Ndef(\sinewave).play;

~freqRange = [500, 5000, \exponential].asSpec; // create a frequency range

HIDdef.usage(\freq, { |value| Ndef(\sinewave).set(\freq, ~freqRange.map(value)) }, \X);
HIDdef.usage(\amp, { |value| Ndef(\sinewave).set(\amp, value) }, \Y);
```




