# HIDElement

*A class describing an element of an HID device*

**Categories:** External Control>HID

**Related:** [HID](../Classes/HID.md), [Working_with_HID](../Guides/Working_with_HID.md), [HIDCollection](../Classes/HIDCollection.md), [HIDUsage](../Classes/HIDUsage.md)

## Description

An HIDElement describes an element, or a control, of an HID device. These are created for the device automatically when you open a device. The only interaction a user will have with elements are to query the properties of the element (with `.postElement`), query the `value` or `rawValue`, or set the value, set the `repeat` property or set an `action` to be performed when new data comes in.


## Class Methods



## Instance Methods

### `action`
Set or get the action to be performed upon receiving element data. The function will be passed the following arguments: the value (mapped between 0 and 1) and the raw value.### `value`
set or get the value of the element. Setting only makes sense for an output element.**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | The raw value to send to the device |  
### `repeat`
By default element's data from the device is not updated unless the data is changing. For certain elements however, you may want to receive updates even if the data is not changing, e.g. for scrollwheel of mice.**Arguments:**

| Argument | Description |
|----------|-------------|
| `rp` | a Boolean to turn repeat on or off |  
### `rawValue`
The raw value of the element.### `logicalValue`
The logical value of the element. In principal the same as value.### `physicalValue`
The physical value of the element. This can be calculated from the raw value and the device's specification for conversion: the physical minimum, the physical maximum, the unit and unit exponent. How the conversion works is described in the USB HID standard documentation.
> **Note:** The conversion is not yet implemented in the backend.

### `arrayValue`
The array value of the element. This value is only of importance for those elements which can represent multiple usages, such as from keyboards. In that case it indicates the key that is pressed, and by adding this number to the usage of the element you know which function the key has.
> **Note:** values from a keyboard are parsed in two ways: first as the element how they come in, second just with the usage and the value (on or off) as the data comes in.


### Properties of the element
### `postElement`
Post a human readable description of the element to the post window.
### `id`
The index of this element. This index may vary between operating systems.
### `device`
Get the device to which this element belongs.
> **Note:** do not set this as a user!

**Returns:** an instance of HID
### `collection`
Get the collection index to which this element belongs.
### `usage`
Retrieve the usage index of this collection.**Returns:** a Number - the usage index of this element
### `usagePage`
Retrieve the usage page index of this element.**Returns:** a Number- the usage page index
### `usageName`
Retrieve the usage name of this element. The name is looked up from the standardized HID usage tables using the usage page index.**Returns:** a String - the usage name
### `pageName`
Retrieve the page name of this element. The name is looked up from the standardized HID usage tables using the usage page index.**Returns:** a String - the usage page name
### `type`
A byte describing the type of element.**Returns:** a number describing the type of element.
### `typeSpec`
The type of element, decoded from the type byte.**Returns:** an Array with Strings describing the type of element.
### `ioType`
Type of the element, input (1), output (2) or feature (3)**Returns:** a Number indicating the ioType
### `iotypeName`
Type of the element, one of `\input`, `\output`, or `\feature`**Returns:** a Symbol indicating the type
### `logicalMin`
Minimum value of the range that is to be expected. This is reported by the device. The element's raw value is mapped between the logical minimum and maximum to obtain the element's value.
### `logicalMax`
Maximum value of the range that is to be expected. This is reported by the device. The element's raw value is mapped between the logical minimum and maximum to obtain the element's value.
### `physicalMin`
Minimum value of the range that is to be expected in a physical sense. This is reported by the device. For example, for a hat switch the physical range may be the direction in degrees in which the hat switch is pointing.
### `physicalMax`
Maximum value of the range that is to be expected in a physical sense. This is reported by the device. For example, for a hat switch the physical range may be the direction in degrees in which the hat switch is pointing.
### `unit`
Index for the unit of the physical range.
### `unitExponent`
The exponent for the physical range.
### `usageMin`
Minimum value of the usage range that is to be expected. This is reported by the device. This is only relevant for elements that report array values.
### `usageMax`
Maximum value of the usage range that is to be expected. This is reported by the device. This is only relevant for elements that report array values.
### `getUsages`
This method is used to get a dictionary of all the usages that this element produces. In most cases an element has only one usage, but in the case of an array-element it will have several uses (for a keyboard, an element represents one keypress, but they can be various different keys).
### `reportID`
The report ID with which this element receives the data. This is a low level device specific identifier
### `reportSize`
The report size in bits with which this element receives the data. This is a low level device specific identifier
### `reportIndex`
The report index with which this element receives the data. This is a low level device specific identifier

## Examples


```supercollider
HID.findAvailable; // find available devices
HID.postAvailable; // post available devices
~myhid = HID.open(1103, 53251); // open a device
~myhid.postElements; // post available elements
// Set actions for the second element:
~myhid.elements[1].action = { |...args| args.postln };
```




