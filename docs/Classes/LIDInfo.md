# LIDInfo

*Helper class for LID to hold the information about an LID device.*

**Categories:** Platform>Linux, External Control>HID

**Related:** [LID](../Classes/LID.md)

## Description

This class contains the basic information about an LID device to access and open it. The class is mostly used internally and rarely accessed directly by the user.
This class is populated with information read from the device, and represents some of the internal information of the device.


## Instance Methods


### `open`
Open the device that is described by this LIDInfo**Returns:** an LID - the device
### `postInfo`
post the LIDInfo in a human readable way
### `findArgs`
An Array of the arguments that can be passed into `LID.findBy` to find this device.
### `name`
The name of the device, as reported by the device itself.
### `vendorID`
The vendor ID of the device, this is a number encoded by the device itself.
### `productID`
The product ID of the device, this is a number encoded by the device itself.
### `path`
The path of the device, this is a path defined by the operating system, essential to distinguish devices with the same vendor and product ID from each other.
### `version`
The version number of the device.
### `physical`
The physical location of the device, as defined by the operating system.
### `unique`
The unique identifier of the device, as defined by the operating system.
### `bustype`
The bustype of this device

