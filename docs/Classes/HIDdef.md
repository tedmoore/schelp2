# HIDdef

*HID response reference definition*

**Categories:** External Control>HID

**Related:** [HID](../Classes/HID.md), [HIDFunc](../Classes/HIDFunc.md), [OSCdef](../Classes/OSCdef.md), [MIDIdef](../Classes/MIDIdef.md), [Working_with_HID](../Guides/Working_with_HID.md)

## Description

HIDdef provides a global reference to the functionality of its superclass HIDFunc. Essentially it stores itself at a key within a global dictionary, allowing replacement at any time. Most methods are inherited from its superclass.


## Class Methods


### `all`
Get the global dictionary of all HIDdefs.**Returns:** An [IdentityDictionary](../Classes/IdentityDictionary.md)
### `freeAll`
Clears and deactivates all HIDdefs from the global collection.
### `new`
Access an existing HIDdef. This is a shortcut to access an HIDdef created with one of the methods below, and allows to change its function, or call free on it.**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | The key at which to store this HIDdef in the global collection. Generally this will be a [Symbol](../Classes/Symbol.md). |  
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. It will be passed... |  

### `usage`
Create a new, enabled HIDdef. If an HIDdef already exists at this key, its parameters will be replaced with the ones provided (args for which nil is passed will use the old values).A convenience method to filter an incoming HID value based on the name of its control usage. E.g. the name of an X-axis of a joystick or the horizontal movement of a mouse has the name `\X`. These usage names are standardized by manufacturers and are looked up in usage tables based on the information coming from the device. If you have an open HID device, you can look up the available usages with: `~hid.postUsages`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | The key at which to store this HIDdef in the global collection. Generally this will be a [Symbol](../Classes/Symbol.md). |  
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. It will be passed... |  
| `elUsageName` | The name of the usage to look for. This can be one usage name, or an array of usage names. |  
| `devUsageName` | The name of the device usage to look for, e.g. `\GamePad` or `\Mouse`. If left blank, the `HIDdef` will match any device. |  
| `deviceInfo` | An [IdentityDictionary](../Classes/IdentityDictionary.md) with a more detailed filtering for a device. |  
| `argTemplate` | This should be an object that implements the method `matchItem`. Depending on the `argTemplateType`, it will be passed either the rawValue of the value of the element to be matched. |  
| `argTemplateType` | If the argTemplateType is `\rawValue` (the default) then the matching is done based on the incoming raw value of the element (not mapped according to the logical min and max). Otherwise the matching is done according to the mapped value. |  
| `dispatcher` | An optional instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md). This can be used to allow for customised dispatching. Normally this should not be needed. The default for this type of `HIDdef` is `HIDUsageDispatcher` |  
**Returns:** A new instance of HIDdef which responds to a specific element usage and device type.
### `device`
Create a new, enabled HIDdef. If an HIDdef already exists at this key, its parameters will be replaced with the ones provided (args for which nil is passed will use the old values).A convenience method to filter an incoming HID value based on the name of the device. This type of HIDdef differs from `HIDdef.usage` in that it filter specifically by device name, rather than device usage, otherwise the arguments are the same.**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | The key at which to store this HIDdef in the global collection. Generally this will be a [Symbol](../Classes/Symbol.md). |  
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. It will be passed... |  
| `elUsageName` | The name of the usage to look for. This can be one usage name, or an array of usage names. |  
| `deviceName` | The name of the device to look for, note that this has to match the string as returned by the device exactly. You can look this string up in the device list: `HID.postAvailable` |  
| `deviceInfo` | An [IdentityDictionary](../Classes/IdentityDictionary.md) with a more detailed filtering for a device. |  
| `argTemplate` | This should be an object that implements the method `matchItem`. Depending on the `argTemplateType`, it will be passed either the rawValue of the value of the element to be matched. |  
| `argTemplateType` | If the argTemplateType is `\rawValue` (the default) then the matching is done based on the incoming raw value of the element (not mapped according to the logical min and max). Otherwise the matching is done according to the mapped value. |  
| `dispatcher` | An optional instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md). This can be used to allow for customised dispatching. Normally this should not be needed. The default for this type of `HIDdef` is `HIDDeviceDispatcher` |  
**Returns:** A new instance of HIDdef which responds to a specific element usage for a specific device.
### `usageID`
Create a new, enabled HIDdef. If an HIDdef already exists at this key, its parameters will be replaced with the ones provided (args for which nil is passed will use the old values).A convenience method to filter an incoming HID value based on the number of its control usage. If the device is using a non-standard usage number, then this method can be used to look for it. A controls usage is fully specified by the combination of its usage ID and its usage page.**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | The key at which to store this HIDdef in the global collection. Generally this will be a [Symbol](../Classes/Symbol.md). |  
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. It will be passed...usage |  
| `elUsageID` | The id (an [Integer](../Classes/Integer.md)) of the usage to look for. This can be one usage id, or an array of usage ids. |  
| `elPageID` | The id (an [Integer](../Classes/Integer.md)) of the page of the usage to look for. This can be one page id, or an array of page ids. |  
| `deviceName` | Since this type of HIDdef is meant for non-standardized controls, you can filter by a specific device name, rather than a general usage, similar to `HIDdef.device` |  
| `deviceInfo` | An [IdentityDictionary](../Classes/IdentityDictionary.md) with a more detailed filtering for a device. |  
| `argTemplate` | This should be an object that implements the method `matchItem`. Depending on the `argTemplateType`, it will be passed either the rawValue of the value of the element to be matched. |  
| `argTemplateType` | If the argTemplateType is `\rawValue` (the default) then the matching is done based on the incoming raw value of the element (not mapped according to the logical min and max). Otherwise the matching is done according to the mapped value. |  
| `dispatcher` | An optional instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md). This can be used to allow for customised dispatching. Normally this should not be needed. The default for this type of `HIDdef` is `HIDElementProtoDispatcher` |  
**Returns:** A new instance of HIDdef which responds to a specific element usage id for a specific device.
### `proto`
Create a new, enabled HIDdef. If an HIDdef already exists at this key, its parameters will be replaced with the ones provided (args for which nil is passed will use the old values).A convenience method to filter an incoming HID value based on a matching template of an element (a [HIDElementProto](../Classes/HIDElementProto.md)). If you have number of conditions for the element that should be matched, then this method can be used to look for it.**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | The key at which to store this HIDdef in the global collection. Generally this will be a [Symbol](../Classes/Symbol.md). |  
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. It will be passed...usage |  
| `protoElement` | The id (an [Integer](../Classes/Integer.md)) of the usage to look for. This can be one usage id, or an array of usage ids. |  
| `deviceInfo` | An [IdentityDictionary](../Classes/IdentityDictionary.md) with a more detailed filtering for a device. |  
| `argTemplate` | This should be an object that implements the method `matchItem`. Depending on the `argTemplateType`, it will be passed either the rawValue of the value of the element to be matched. |  
| `argTemplateType` | If the argTemplateType is `\rawValue` (the default) then the matching is done based on the incoming raw value of the element (not mapped according to the logical min and max). Otherwise the matching is done according to the mapped value. |  
| `dispatcher` | An optional instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md). This can be used to allow for customised dispatching. Normally this should not be needed. The default for this type of `HIDdef` is `HIDElementProtoDispatcher` |  
**Returns:** A new instance of HIDdef which responds to a specific prototype element.
### `element`
Create a new, enabled HIDdef. If an HIDdef already exists at this key, its parameters will be replaced with the ones provided (args for which nil is passed will use the old values).A convenience method to filter an incoming HID value based on the index of its element. If the device is using something non-standard, or you want to access keyboard elements directly, then this method can be used to look for it. Note that the element index is not necessarily the same across different operating systems (i.e. it may vary between Linux and macOS and Windows).**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | The key at which to store this HIDdef in the global collection. Generally this will be a [Symbol](../Classes/Symbol.md). |  
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. It will be passed... |  
| `elID` | The id (an [Integer](../Classes/Integer.md)) of the element to look for. This can be one element id, or an array of element ids. |  
| `deviceName` | Since this type of HIDdef is meant for non-standardized elements, you can filter by a specific device name, rather than a general usage, similar to `HIDdef.device` |  
| `deviceInfo` | An [IdentityDictionary](../Classes/IdentityDictionary.md) with a more detailed filtering for a device. |  
| `argTemplate` | This should be an object that implements the method `matchItem`. Depending on the `argTemplateType`, it will be passed either the rawValue of the value of the element to be matched. |  
| `argTemplateType` | If the argTemplateType is `\rawValue` (the default) then the matching is done based on the incoming raw value of the element (not mapped according to the logical min and max). Otherwise the matching is done according to the mapped value. |  
| `dispatcher` | An optional instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md). This can be used to allow for customised dispatching. Normally this should not be needed. The default for this type of `HIDdef` is `HIDElementDispatcher` |  
**Returns:** A new instance of HIDdef which responds to a specific element id for a specific device.

## Instance Methods

### `key`
Get this HIDdef's key.**Returns:** Usually a [Symbol](../Classes/Symbol.md).### `free`
Clears this HIDdef from the global collection and deactivates it.
## Examples

For all the examples below here, you will need to have initialized an HID device (see also [Working_with_HID](../Guides/Working_with_HID.md)). The examples below should work with a standard USB mouse.

```supercollider
HID.findAvailable; // check which devices are attached
HID.postAvailable; // post the available devices
~myhid = HID.open(1103, 53251); // adapt this line for  the device that you want to open!
```



### Filtering based on usage

```supercollider
// filter all events coming from the x-axis of a mouse
HIDdef.usage(\example, { |...args| args.postln }, \X, \Mouse);

// filter all events coming from a mouse
HIDdef.usage(\example, { |...args| args.postln }, nil, \Mouse);

// filter all events coming from an X-axis (could be from a mouse or a joystick or a gamepad)
HIDdef.usage(\example, { |...args| args.postln }, \X);

// filter all events coming from an X-axis or an Y-axis (could be from a mouse or a joystick or a gamepad)
HIDdef.usage(\example, { |...args| args.postln }, [\X, \Y]);

// usage of argTemplate: matching the rawValue (is the default behaviour)

// only react when the values are below zero:
HIDdef.usage(\example, { |...args| args.postln }, [\X, \Y], argTemplate: { |val| val < 0 });

// only match when rawvalue == -1
HIDdef.usage(\example, { |...args| args.postln }, [\X, \Y], argTemplate: -1);

// only match when rawvalue is one of [-3, -2, -1]
HIDdef.usage(\example, { |...args| args.postln }, [\X, \Y], argTemplate: [-3, -2, -1]);

// usage of argTemplate: matching the scaled value when smaller than 0.5
HIDdef.usage(\example, { |...args| args.postln }, [\X, \Y], argTemplate: { |val| val < 0.5 }, argTemplateType: \value);

// using deviceInfo rather than deviceUsage (you can add more device specifications to match)
HIDdef.usage(\example, { |...args| args.postln }, \X, deviceInfo: (usageName: \Mouse));

HIDdef.usage(\example, { |...args| args.postln }, nil, deviceInfo: (usageName: \Mouse));

HIDdef(\example).free;
```




### Filtering based on usage ID

```supercollider
// filter by usage ID 48 on usage page 1
HIDdef.usageID(\example2, { |...args| args.postln }, 48, 1);

// filter by usage ID 48 or 49 on usage page 1
HIDdef.usageID(\example2, { |...args| args.postln }, [48, 49], 1);

// filter by any usage ID on usage page 1
HIDdef.usageID(\example2, { |...args| args.postln }, nil, 1);

// filter by usage ID 48 on usage page 1, of a device with an empty string as a name (fill in the name of your mouse there).
HIDdef.usageID(\example2, { |...args| args.postln }, 48, 1, "");

// filter by usage ID 48 on usage page 1, of a device with path "/dev/hidraw2" (adapt this path to the device you want to match)
HIDdef.usageID(\example2, { |...args| args.postln }, 48, 1, deviceInfo: (path: "/dev/hidraw2")  );

HIDdef(\example2).free;
```




### Filtering based on a device

```supercollider
// filter for device with name "", and element with usage \X.
HIDdef.device(\example3, { |...args| args.postln }, \X, "");
HIDdef(\example3).free;
```




### Filtering based on a prototype element

```supercollider
// create an prototype element with usageName \X
c = HIDElementProto.new.usageName_(\X);
HIDdef.proto(\example4, { |...args| args.postln }, c);
HIDdef(\example4).free;
```




### Filtering based on an element ID

```supercollider
// filter for elements with element id 6:
HIDdef.element(\example5, { |...args| args.postln }, 6);
HIDdef(\example5).free;
```






