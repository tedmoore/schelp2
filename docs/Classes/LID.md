# LID

*Linux Input Device*

**Categories:** Platform>Linux, External Control>HID

**Related:** [HID](../Classes/HID.md), [LIDInfo](../Classes/LIDInfo.md), [LIDSlot](../Classes/LIDSlot.md), [LIDGui](../Classes/LIDGui.md)

## Description

This class provides a way to access devices in the Linux input layer, which supports many input devices (mouse, keyboard, joystick, gamepad, tablet) and busses (serial, PS/2, USB).

> **Note:** For external HID devices it is recommended to use the [HID](../Classes/HID.md) interface, as described in [Working_with_HID](../Guides/Working_with_HID.md), as it will ensure that your code is cross platform compatible. Only in cases where the raw HID interface does not provide access because the device needs a special driver (and this driver is provided in Linux kernel), or in case you want to access internal devices, you should use this class.


NOTE: if you have trouble opening a device, e.g. when you get the message `ERROR: LID: Could not open device`, please check the [LID_permissions](../Guides/LID_permissions.md)

### First example:

```
LID.findAvailable;
LID.postAvailable; // pick one that you want to open, and fill in the vendor and product id in the next line:
d = LID.open(2, 10); // trackpoint

d.postInfo;
d.postSlots;

d.debug_(true); // wiggle a little and see the data coming in

d.debug_(false);

// create a GUI:
d.makeGui;

// close the device (don't do this yet, if you want to excecute the further examples in this class)
d.close;
```





## Class Methods



### Finding devices
An example of finding a device:


```
LID.findAvailable;

LID.available;

LID.postAvailable;

// look for the one you want and find it:

LID.findBy(2, 10) // by vendor and product
```



### `findAvailable`
queries the operating system which LID devices are attached to the system and can be accessed. When using LID this is the first method you need to execute, before you can access any device.**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | The basic path to look for, by default this is `"event"`. See also `deviceRoot`. |  
**Returns:** an IdentityDictionary of available devices

### `deviceRoot`
This is the base path where to look for devices. By default this is: `"/dev/input"`. With `findAvailable` this is extended with the `name` that is passed in, which has as a default `"event"`. Hence, by default we look for devices that match the path: `"/dev/input/event*"`.See below for some [#Opening devices with alternative deviceRoot](#opening-devices-with-alternative-deviceroot)

### `available`
A dictionary of available devices, or rather info about them in an instance of [LIDInfo](../Classes/LIDInfo.md), populated by the method findAvailable**Returns:** an IdentityDictionary

### `postAvailable`
posts a human readable list of available LID devices and their properties (see also [LIDInfo](../Classes/LIDInfo.md))

### `findBy`
Find devices in the available device dictionary by specifying one or more characteristics of the device**Arguments:**

| Argument | Description |
|----------|-------------|
| `vendorID` | The vendor ID of the device, this is a number encoded by the device itself. |  
| `productID` | The product ID of the device, this is a number encoded by the device itself. |  
| `path` | The path of the device, this is a path defined by the operating system. |  
| `version` | The version of the device. |  
| `physical` | The physical location of the device, this is a path defined by the operating system. |  
| `unique` | A unique identifier for the device, defined by the operating system. |  
**Returns:** an IdentityDictionary of devices the match the search query, or nil if no arguments are given
```
LID.findBy(2); // by vendorID
LID.findBy(2, 10) // by vendor and product
LID.findBy(productID: 10);
LID.findBy(path: "/dev/input/event4");
LID.findBy(version: 0);
LID.findBy(physical: 'synaptics-pt/serio0/input0')
LID.findBy(physical: "synaptics-pt/serio0/input0") // argument is converted to symbol for check
LID.findBy(unique: '')
LID.findBy(unique: "") // argument is converted to symbol for check

// using all possible arguments:
LID.findBy(2, 10, "/dev/input/event4", 0x0000, 'synaptics-pt/serio0/input0')
```




### Opening devices

### `open`
Open a device with a given vendorID and product ID. For arguments description see [#*findBy](#*findby). The method will call the method `findBy` and use the first available result as the device to open.**Returns:** The LID device - an instance of `LID`.

### `new`
Same as `LID.openPath`.

### `openPath`
Open a device using its path in the operating system.**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | The path in the operating system, e.g. `"/dev/input/event4"` |  
**Returns:** The LID device - an instance of `LID`.

### `openAt`
Open a device using its index in the dictionary of available devices**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The index into the dictionary of available devices |  
**Returns:** The LID device - an instance of `LID`.

### `openDevices`
A dictionary of the opened devices**Returns:** an IdentityDictionary


### Adding functions to LID events
Whenever data comes in from an opened LID device, there are two types of actions fired. An action for the incoming element data and an action for the device, indicating that there has been a change in one of the elements. In most cases you will want to use the first action; only in cases where the order of parsing the element data is important, you may want to use the second type - e.g. when dealing with very accurately timed button press combinations.

There are three levels where you can set actions:

- at the global level - called for any LID device, for any slot
- at the device level - called for the specific device, for any slot
- at the slot level - called for the specific element of the specific device



### `debug`
When set to true, the incoming data from any opened LID device will be printed to the post window.

### `action`
Set or get the action to be performed upon receiving element data from any device. The function will be passed the following arguments: the value (mapped between 0 and 1), the raw value, element usage page, the element usage, the element id, the device id, the device (an instance of LID).**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | The function to be performed upon receiving element data from the device |  


### `addRecvFunc`
add a function to the internal FunctionList that will be evaluated whenever element data comes in from an open device. The arguments passed to the function are as defined above. Use this method if you want to add actions to LID functions from classes you write, so that you still keep the option to add an action on the fly from user code.**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | The function to be added to the list. |  


### `removeRecvFunc`
remove a function to the internal FunctionList that will be evaluated whenever data comes in from a device.**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | The function to remove from the list, this must be a reference to the Function that was originally added to the list |  



### Managing the LID subsystem
The following methods are used internally to initialize and finalize the LID subsystem, but in rare cases you may wish to manage these methods manually.


### `initializeLID`
Initialize the LID subsystem, this method is called automatically when calling the method findAvailable.

### `running`
Indicates whether or not the LID subsystem is running.

### `closeAll`
This method is called automatically upon Shutdown, if the LID subsystem was initialized. It can be stopped manually, in order to save system resources. This method will close all opened LID devices.


### Creating specs for devices
Device specs are mappings between event codes and symbolic control names. New specs can be added to LID.specs via LID>>*register.


```
// Add a mouse device spec for a Logitech trackball
LID.register('Logitech Trackball', LID.mouseDeviceSpec);

// Add a custom device spec for a Logitech gamepad
(
LID.register('Logitech WingMan RumblePad', (
    // key
    rumble: #[0x0001, 0x0102],    // rumble (toggles ff)
    mode: #[0x0001, 0x0103],    // mode (switches h and l)
    a: #[0x0001, 0x0120],        // button a
    b: #[0x0001, 0x0121],        // button b
    c: #[0x0001, 0x0122],        // button c
    x: #[0x0001, 0x0123],        // button x
    y: #[0x0001, 0x0124],        // button y
    z: #[0x0001, 0x0125],        // button z
    l: #[0x0001, 0x0126],        // left front button
    r: #[0x0001, 0x0127],        // right front button
    s: #[0x0001, 0x0128],        // button s
    // abs
    lx: #[0x0003, 0x0000],        // left joystick x
    ly: #[0x0003, 0x0001],        // left joystick y
    rx: #[0x0003, 0x0005],        // right joystick x
    ry: #[0x0003, 0x0006],        // right joystick y
    hx: #[0x0003, 0x0010],        // hat x
    hy: #[0x0003, 0x0011],        // hat y
    slider: #[0x0003, 0x0002]    // slider
));
)
```



### `register`
This will register the spec for the specified device. If the device was opened and did not use the spec before, it will use this spec. See also [LID#*specs](../Classes/LID.md#*specs).**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | The name of the device to register it for. |  
| `spec` | The spec to be added. This should be an IdentityDictionary. |  


### `specs`
This returns the specs that have been registered.

### `mouseDeviceSpec`
This returns a default spec for a mouse device; any mouse, trackball, trackpad or trackpoint should be able to use this spec.

### `keyboardDeviceSpec`
This returns a default spec for a keyboard device; any keyboard or numpad should be able to use this spec.


## Instance Methods


### `close`
Close the LID device, closing a device is asynchronous. You can set a closeAction (see below), which will be performed when the device closes.
### `isOpen`
Returns true if the device is open, false if the device was closed.
```
d.isOpen;
d.close;
d.isOpen;
```


### Posting human readable information about the device

### `postInfo`
Post the LIDInfo of this device in a human readable format. See also [LIDInfo](../Classes/LIDInfo.md).

### `postSlots`
Post information about all the slots of this device in a human readable format

### `dumpCaps`
Post the list of available capabilities in a human readable format

### `makeGui`
Create a [LIDGui](../Classes/LIDGui.md) for the device.

### Accessing slots
Device capabilities are reported as event type and event code mappings. Event type and event code constants can be found in `/usr/include/linux/input.h`


### `slot`
Access a slot by its evtType and evtCode. See also [LIDSlot](../Classes/LIDSlot.md)**Arguments:**

| Argument | Description |
|----------|-------------|
| `evtType` | The eventType to access the slot. |  
| `evtCode` | The eventCode to access the slot. |  


### `at`
If a `spec` is defined for this device, then you can use a controlName to look up a slot.

### `spec`
The IdentityDictionary that maps labels for slots to slot indices.**Arguments:**

| Argument | Description |
|----------|-------------|
| `forceLookup` | If set to true, this will force the dictionary to be reinitialised with the registered spec for this device. |  


### Adding functionality to the device

### `debug`
When set to true, the incoming data from this LID device will be printed to the post window.
```
d.debug_(true);
d.debug_(false);
```



### `closeAction`
Function to be performed when device is closed.
```
d.closeAction_({ "hey, I got closed!".postln });
d.close;
```



### `action`
Set or get the action to be performed upon receiving data from the device. The function will be passed in the evtType, the evtCode, the value (mapped according to the slot's spec), and the raw value.
```
d.action_({ |...args| ("my action" + args).postln });
d.action_(nil);
```



### Properties of the device

### `slots`
An IdentityDictionary holding all the slots, i.e. controls, of the device

### `path`
Retrieve the path of this device
```
d.path;
```



### `info`
Retrieve the LIDInfo of this device
```
d.info;
```



### `vendor`
Retrieve the vendor id of this device
```
d.vendor;
```



### `product`
Retrieve the product id of this device
```
d.product;
```



### `caps`
The list of available capabilities.

### Grabbing devices
Given proper permissions, devices can be grabbed to prevent use in other applications (including X). Be careful when grabbing mouse or keyboard, as you will not be able to use them for normal interaction (like typing code or moving the mouse pointer) anymore!


```
d[\b].action = { d.ungrab };
d.grab;

d.isGrabbed;
```



### `grab`
Grab the device to use exclusively for SC.

### `ungrab`
Release the device to use it no longer exclusively for SC.

### `isGrabbed`
Check whether the device is grabbed.

## Examples


### Finding and opening the device

```
LID.findAvailable;
LID.postAvailable; // pick one that you want to open, and fill in the vendor and product id in the next line:
d = LID.open(2, 10); // trackpoint

d.postInfo;
d.postSlots;

d.debug_(true); // wiggle a little and see the data coming in
d.debug_(false);
```




### Event actions (raw events)
The device's 'action' instance variable can be used for event notifications. it is passed the event type, code and current value.


```
(
d.action = { |evtType, evtCode, evtValue|
    [evtType.asHexString(4), evtCode.asHexString(4), evtValue].postln
}
)

d.action = nil;
```


If a device is detached LID will detect this, and close the device. It will execute a closeAction, which can be defined by the user:


```
d.closeAction = { "device was detached".postln };
```




### Event actions (raw slot events)
When 'action' is nil, actions can be bound to specific events.


```
(
d.slot(0x0002, 0x0001).action = { |slot|
    [slot.type.asHexString(4), slot.code.asHexString(4), slot.value].postln;
}
)
```


Relative slots can have deltaActions:


```
(
d.slot(0x0002, 0x0001).deltaAction = { |slot|
    [slot.type.asHexString(4), slot.code.asHexString(4), slot.delta].postln;
}
)
```




### Event actions (symbolic slot events)
When a device spec was registered for a given device name, slot actions can be assigned by using the symbolic control name.


```
    d[\x].action = { |slot| [\x, slot.value].postln };
```




### LED's
some devices have LEDs which can be turned on and off. These show up with d.caps as events of type 0x0011


```
d = LID("/dev/input/event0");
// LED's can be turned on:
d.setLEDState(0x0, 1)
// (LED 0x0 should be available on any keyboard)
// and off:
d.setLEDState(0x0, 0)
d.close;

// setLEDState(evtCode, evtValue): value should be 1 or 0
```




### Closing devices

```
d.close;
LID.closeAll;
```




### Opening devices with alternative deviceRoot
Input devices are accessed through device nodes, typically `/dev/input/event[0-9]`. When using a userspace daemon like udev, meaningful names can be assigned to devices.

raw device name:


```
d = LID("/dev/input/event4");
```


symbolic device name


```
d = LID("/dev/input/trackball");
```


device name relative to LID.deviceRoot


```
d = LID("gamepad");
```


build a list of the available devices:


```
LID.findAvailable;
```


buildDeviceList builds a table of the devices found in LID.deviceRoot+"/event", trying to open all that it finds, looking up its name and closing them again. The result is returned and can later be accessed by LID.deviceList. You can query another name than "/event" by passing an argument. (the search will be: LID.deviceRoot++"/"++name++"*")


```
LID.findAvailable("mouse");
```





> **Note:** this is likely to give the info that the devices could not be opened, as "mouse" uses another interface (you can of course access mice via the "event" interface)



> **Note:** if you cannot open the devices at all, please look in the helpfile for: [LID_permissions](../Guides/LID_permissions.md)






