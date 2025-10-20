# HIDInfo

*This class contains the basic information about an HID device to access and open it.*

**Categories:** External Control>HID

**Related:** [HID](../Classes/HID.md), [Working_with_HID](../Guides/Working_with_HID.md)

## Description

This class contains the basic information about an HID device to access and open it. The class is mostly used internally and rarely accessed directly by the user.
This class is populated with information read from the device, and represents some of the internal information of the device.


## Class Methods



## Instance Methods


### `open`
Open the device that is described by this HIDInfo**Returns:** an HID - the device
### `postInfo`
post the HIDInfo in a human readable way
### `path`
The path of the device, this is a path defined by the operating system, and thus not the same across platforms, but essential to distinguish devices with the same vendor and product ID from each other.
### `vendorID`
The vendor ID of the device, this is a number encoded by the device itself, and the same across platforms.
### `productID`
The product ID of the device, this is a number encoded by the device itself, and the same across platforms.
### `vendorName`
The vendor name of the device, this is a string encoded by the device itself, and the same across platforms.
### `productName`
The product name of the device, this is a string encoded by the device itself, and the same across platforms.
### `serialNumber`
The serial number of the device. This is dependent on the operating system, e.g. on Linux it is not set.
### `releaseNumber`
The release number of the device, this is a number encoded by the device itself, and the same across platforms.
### `interfaceNumber`
Type of interface of the device, can be an index standing for USB, Bluetooth, etc.
### `usage`
Retrieve the usage index of this collection.**Returns:** a Number - the usage index of this collection
### `usagePage`
Retrieve the usage page index of this collection.**Returns:** a Number- the usage page index
### `usageName`
Retrieve the usage name of this collection. The name is looked up from the standardized HID usage tables using the usage page index.**Returns:** a String - the usage name
### `pageName`
Retrieve the page name of this collection. The name is looked up from the standardized HID usage tables using the usage page index.**Returns:** a String - the usage page name

