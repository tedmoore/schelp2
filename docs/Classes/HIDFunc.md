# HIDFunc

*Fast responder for incoming data from human input devices (HID)*

**Categories:** External Control>HID

**Related:** [HID](../Classes/HID.md), [HIDdef](../Classes/HIDdef.md), [HIDProto](../Classes/HIDProto.md), [HIDElementProto](../Classes/HIDElementProto.md), [OSCFunc](../Classes/OSCFunc.md), [MIDIFunc](../Classes/MIDIFunc.md), [Working_with_HID](../Guides/Working_with_HID.md)

## Description

Human input devices can be used as controllers for making music. This class provides you with access to them in a way similar to OSCFunc and MIDIFunc.
HIDFunc (and its subclass [HIDdef](../Classes/HIDdef.md)) registers one or more functions to respond to an incoming HID message. Many of its methods are inherited from its superclass [AbstractResponderFunc](../Classes/AbstractResponderFunc.md).

> **Note:** HIDFuncs are removed on Cmd-. by default. This can be overridden using either of the fix or permanent methods.


The development of this SuperCollider implementation of HID access was funded by the SuperCollider community and BEK, Bergen Elektronisk Kunst, Bergen, Norway, [http://www.bek.no](http://www.bek.no)


## Class Methods


### `defaultDispatchers`
Get or set an [IdentityDictionary](../Classes/IdentityDictionary.md) containing the default dispatcher objects for HIDFuncs of different types (these are what you get if you pass nil as the dispatcher argument to [#*new](#*new)). These objects will decide if any of their registered HIDFuncs should respond to an incoming HID message. The dictionary should have the keys `[\usage, \usageID, \device, \proto, \element]` and values of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md) for each message type. By default these will be instances of `HIDUsageDispatcher`, `HIDElementProtoDispatcher`, `HIDDeviceDispatcher`, `HIDElementProtoDispatcher` and `HIDElementDispatcher` respectively.**Returns:** The getter returns an [IdentityDictionary](../Classes/IdentityDictionary.md).
### `usage`
A convenience method to filter an incoming HID value based on the name of its control usage. E.g. the name of an X-axis of a joystick or the horizontal movement of a mouse has the name `\X`. These usage names are standardized by manufacturers and are looked up in usage tables based on the information coming from the device. If you have an open HID device, you can look up the available usages with: `~hid.postUsages`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. It will be passed... |  
| `elUsageName` | The name of the usage to look for. This can be one usage name, or an array of usage names. If nil, it will match any usage. |  
| `devUsageName` | The name of the device usage to look for, e.g. `\GamePad` or `\Mouse`. If left blank, the `HIDFunc` will match any device. |  
| `deviceInfo` | An [IdentityDictionary](../Classes/IdentityDictionary.md) or [HIDProto](../Classes/HIDProto.md) with a more detailed filtering for a device. |  
| `argTemplate` | This should be an object that implements the method `matchItem`. Depending on the `argTemplateType`, it will be passed either the rawValue of the value of the element to be matched. |  
| `argTemplateType` | If the argTemplateType is `\rawValue` (the default) then the matching is done based on the incoming raw value of the element (not mapped according to the logical min and max). Otherwise the matching is done according to the mapped value. |  
| `dispatcher` | An optional instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md). This can be used to allow for customised dispatching. Normally this should not be needed. The default for this type of `HIDFunc` is `HIDUsageDispatcher` |  
**Returns:** A new instance of HIDFunc which responds to a specific element usage and device type.
### `device`
A convenience method to filter an incoming HID value based on the name of the device. This type of HIDFunc differs from `HIDFunc.usage` in that it filter specifically by device name, rather than device usage, otherwise the arguments are the same.**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. It will be passed... |  
| `elUsageName` | The name of the usage to look for. This can be one usage name, or an array of usage names. |  
| `deviceName` | The name of the device to look for, note that this has to match the string as returned by the device exactly. You can look this string up in the device list: `HID.postAvailable` |  
| `deviceInfo` | An [IdentityDictionary](../Classes/IdentityDictionary.md) or [HIDProto](../Classes/HIDProto.md) with a more detailed filtering for a device. |  
| `argTemplate` | This should be an object that implements the method `matchItem`. Depending on the `argTemplateType`, it will be passed either the rawValue of the value of the element to be matched. |  
| `argTemplateType` | If the argTemplateType is `\rawValue` (the default) then the matching is done based on the incoming raw value of the element (not mapped according to the logical min and max). Otherwise the matching is done according to the mapped value. |  
| `dispatcher` | An optional instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md). This can be used to allow for customised dispatching. Normally this should not be needed. The default for this type of `HIDFunc` is `HIDDeviceDispatcher` |  
**Returns:** A new instance of HIDFunc which responds to a specific element usage for a specific device.
### `usageID`
A convenience method to filter an incoming HID value based on the number of its control usage. If the device is using a non-standard usage number, then this method can be used to look for it. A controls usage is fully specified by the combination of its usage ID and its usage page.**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. It will be passed...usage |  
| `elUsageID` | The id (an [Integer](../Classes/Integer.md)) of the usage to look for. This can be one usage id, or an array of usage ids. If nil, it will match any usage id. |  
| `elPageID` | The id (an [Integer](../Classes/Integer.md)) of the page of the usage to look for. This can be one page id, or an array of page ids. |  
| `deviceName` | Since this type of HIDFunc is meant for non-standardized controls, you can filter by a specific device name, rather than a general usage, similar to `HIDFunc.device` |  
| `deviceInfo` | An [IdentityDictionary](../Classes/IdentityDictionary.md) or [HIDProto](../Classes/HIDProto.md) with a more detailed filtering for a device. |  
| `argTemplate` | This should be an object that implements the method `matchItem`. Depending on the `argTemplateType`, it will be passed either the rawValue of the value of the element to be matched. |  
| `argTemplateType` | If the argTemplateType is `\rawValue` (the default) then the matching is done based on the incoming raw value of the element (not mapped according to the logical min and max). Otherwise the matching is done according to the mapped value. |  
| `dispatcher` | An optional instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md). This can be used to allow for customised dispatching. Normally this should not be needed. The default for this type of `HIDFunc` is `HIDElementProtoDispatcher` |  
**Returns:** A new instance of HIDFunc which responds to a specific element usage id for a specific device.
### `proto`
A convenience method to filter an incoming HID value based on a matching template of an element (a [HIDElementProto](../Classes/HIDElementProto.md)). If you have number of conditions for the element that should be matched, then this method can be used to look for it.**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. It will be passed...usage |  
| `protoElement` | The id (an [Integer](../Classes/Integer.md)) of the usage to look for. This can be one usage id, or an array of usage ids. |  
| `deviceInfo` | An [IdentityDictionary](../Classes/IdentityDictionary.md) or [HIDProto](../Classes/HIDProto.md) with a more detailed filtering for a device. |  
| `argTemplate` | This should be an object that implements the method `matchItem`. Depending on the `argTemplateType`, it will be passed either the rawValue of the value of the element to be matched. |  
| `argTemplateType` | If the argTemplateType is `\rawValue` (the default) then the matching is done based on the incoming raw value of the element (not mapped according to the logical min and max). Otherwise the matching is done according to the mapped value. |  
| `dispatcher` | An optional instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md). This can be used to allow for customised dispatching. Normally this should not be needed. The default for this type of `HIDFunc` is `HIDElementProtoDispatcher` |  
**Returns:** A new instance of HIDFunc which responds to a specific prototype element.
### `element`
A convenience method to filter an incoming HID value based on the index of its element. If the device is using something non-standard, or you want to access keyboard elements directly, then this method can be used to look for it. Note that the element index is not necessarily the same across different operating systems (i.e. it may vary between Linux and macOS and Windows).**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. It will be passed... |  
| `elID` | The id (an [Integer](../Classes/Integer.md)) of the element to look for. This can be one element id, or an array of element ids. |  
| `deviceName` | Since this type of HIDFunc is meant for non-standardized elements, you can filter by a specific device name, rather than a general usage, similar to `HIDFunc.device` |  
| `deviceInfo` | An [IdentityDictionary](../Classes/IdentityDictionary.md) or [HIDProto](../Classes/HIDProto.md) with a more detailed filtering for a device. |  
| `argTemplate` | This should be an object that implements the method `matchItem`. Depending on the `argTemplateType`, it will be passed either the rawValue of the value of the element to be matched. |  
| `argTemplateType` | If the argTemplateType is `\rawValue` (the default) then the matching is done based on the incoming raw value of the element (not mapped according to the logical min and max). Otherwise the matching is done according to the mapped value. |  
| `dispatcher` | An optional instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md). This can be used to allow for customised dispatching. Normally this should not be needed. The default for this type of `HIDFunc` is `HIDElementDispatcher` |  
**Returns:** A new instance of HIDFunc which responds to a specific element id for a specific device.

### Debugging
### `trace`
A convenience method which dumps all incoming HID messages.**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | A [Boolean](../Classes/Boolean.md) indicating whether dumping is on or off. |  



## Instance Methods

### `type`
The type of HIDFunc.**Returns:** a [Symbol](../Classes/Symbol.md), one of `\usage`, `\device`, `\usageID`, `\proto` or `\element`.### `elUsage`
The usage name, usage id, or element id of the element/control to match, depending on the type of HIDFunc### `elementTemplate`
An instance of HIDElementProto, describing the template for the element to match.### `devUsage`
The device usage or device name of the element/control to match, depending on the type of HIDFunc### `deviceTemplate`
An instance of HIDProto, describing the template for the device to match.### `argTemplate`
This should be an object that implements the method `matchItem`. Depending on the `argTemplateType`, it will be passed either the rawValue of the value of the element to be matched.### `argTemplateType`
If the argTemplateType is `\rawValue` (the default) then the matching is done based on the incoming raw value of the element (not mapped according to the logical min and max). Otherwise the matching is done according to the mapped value.
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
a = HIDFunc.usage({ |...args| args.postln }, \X, \Mouse);
// disable the function again:
a.free;

// filter all events coming from a mouse
a = HIDFunc.usage({ |...args| args.postln }, nil, \Mouse);
// disable the function again:
a.free;

// filter all events coming from an X-axis (could be from a mouse or a joystick or a gamepad)
a = HIDFunc.usage({ |...args| args.postln }, \X);
// disable the function again:
a.free;

// filter all events coming from an X-axis or an Y-axis (could be from a mouse or a joystick or a gamepad)
a = HIDFunc.usage({ |...args| args.postln }, [\X, \Y]);
// disable the function again:
a.free;


// usage of argTemplate: matching the rawValue (is the default behaviour)

// only react when the values are below zero:
a = HIDFunc.usage({ |...args| args.postln }, [\X, \Y], argTemplate: { |val| val < 0 });
a.free;

// only match when rawvalue == -1
a = HIDFunc.usage({ |...args| args.postln }, [\X, \Y], argTemplate: -1);
a.free;

// only match when rawvalue is one of [-3, -2, -1]
a = HIDFunc.usage({ |...args| args.postln }, [\X, \Y], argTemplate: [-3, -2, -1]);
a.free;

// usage of argTemplate: matching the scaled value when smaller than 0.5
a = HIDFunc.usage({ |...args| args.postln }, [\X, \Y], argTemplate: { |val| val < 0.5 }, argTemplateType: \value);
a.free;


// using deviceInfo rather than deviceUsage (you can add more device specifications to match)
a = HIDFunc.usage({ |...args| args.postln }, \X, deviceInfo: (usageName: \Mouse));
a.free;

a = HIDFunc.usage({ |...args| args.postln }, nil, deviceInfo: (usageName: \Mouse));
a.free;
```




### Filtering based on usage ID

```supercollider
// filter by usage ID 48 on usage page 1
a = HIDFunc.usageID({ |...args| args.postln }, 48, 1);
a.free;

// filter by usage ID 48 or 49 on usage page 1
a = HIDFunc.usageID({ |...args| args.postln }, [48, 49], 1);
a.free;

// filter by any usage ID on usage page 1
a = HIDFunc.usageID({ |...args| args.postln }, nil, 1);
a.free;

// filter by usage ID 48 on usage page 1, of a device with an empty string as a name (fill in the name of your mouse there).
a = HIDFunc.usageID({ |...args| args.postln }, 48, 1, "");
a.free;

// filter by usage ID 48 on usage page 1, of a device with path "/dev/hidraw2" (adapt this path to the device you want to match)
a = HIDFunc.usageID({ |...args| args.postln }, 48, 1, deviceInfo: (path: "/dev/hidraw2")  );
a.free;
```




### Filtering based on a device

```supercollider
// filter for device with name "", and element with usage \X.
a = HIDFunc.device({ |...args| args.postln }, \X, "");
a.free;
```




### Filtering based on a prototype element

```supercollider
// create an prototype element with usageName \X
c = HIDElementProto.new.usageName_(\X);
a = HIDFunc.proto({ |...args| args.postln }, c);
a.free;
```




### Filtering based on an element ID

```supercollider
// filter for elements with element id 6:
a = HIDFunc.element({ |...args| args.postln }, 6);
a.free;
```






