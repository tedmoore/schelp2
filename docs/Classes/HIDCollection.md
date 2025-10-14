# HIDCollection

*A class describing a group of elements of an HID device*

**Categories:** External Control>HID

**Related:** [HID](../Classes/HID.md), [Working_with_HID](../Guides/Working_with_HID.md), [HIDElement](../Classes/HIDElement.md), [HIDUsage](../Classes/HIDUsage.md)

## Description

An HIDCollection defines a group of controls on a low level of the HID device, i.e. the device reports these groups. The main use to access it is to retrieve information about what kind of function the HID device performs, e.g. a GamePad, a Joystick or a Mouse.
This class is populated with information read from the device, and represents some of the internal information of the device.


## Class Methods



## Instance Methods

### `postCollection`
Post a human readable description of the collection to the post window.### `usage`
Retrieve the usage index of this collection.**Returns:** a Number - the usage index of this collection### `usagePage`
Retrieve the usage page index of this collection.**Returns:** a Number- the usage page index### `usageName`
Retrieve the usage name of this collection. The name is looked up from the standardized HID usage tables using the usage page index.**Returns:** a String - the usage name### `pageName`
Retrieve the page name of this collection. The name is looked up from the standardized HID usage tables using the usage page index.**Returns:** a String - the usage page name### `type`
The type of collection.**Returns:** a number describing the type of collection.### `device`
Get the device to which this collection belongs.
> **Note:** do not set this as a user!

**Returns:** an instance of HID### `id`
Index of this collection**Returns:** a Number### `parent`
Index of the parent of this collection.**Returns:** a Number### `numElements`
Number of elements in this collection**Returns:** a Number### `firstElement`
The first element that is part of this collection.**Returns:** a Number - an index indicating the first element### `numCollections`
Number of (child) collections in this collection**Returns:** a Number### `firstCollection`
The first collection that is part of this collection.**Returns:** a Number - an index indicating the first collection

