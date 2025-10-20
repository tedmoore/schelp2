# LIDSlot

*Handles incoming LID data.*

**Categories:** Platform>Linux, External Control>HID

**Related:** [LID](../Classes/LID.md)

## Description



## Class Methods



### `slotTypeStrings`
An IdentityDictionary mapping the evtTypes to descriptive strings.

## Instance Methods


### `postInfo`
Post the slots properties in a nice, human readable way.
### `debug`
Turn on or off the debug posting for this slot.
### `action`
Set the action for this slot.
### `value`
Get the current value of this slot, mapped according to its spec.
### `spec`
The ControlSpec to map this slots value.
### `rawValue`
Get the rawValue; the setter of this method is called from the primitive `LID.prHandleEvent` and should not be called by the user.
### `next`
Convenience method to use a LIDSlot in a pattern; this will call the value of the slot.
### `createBus`
Create a bus on the server. The slot's value will automatically be set to this bus on the server.**Arguments:**

| Argument | Description |
|----------|-------------|
| `server` | The server on which to create the bus and forward the value to. By default this is `Server.default` |  

### `bus`
The bus on the server that this slot's value is mapped to.
### `freeBus`
Free the bus on the server and remove the action to forward the value.
### `kr`
JITLib support to access the bus in NodeProxy's. This will create the bus if it does not already exist.
### `device`
The device to which this slot belongs.
### `type`
The type of slot that this is.
### `code`
The eventCode for this slot.
### `key`
The key by which this slot is known in the spec of the device.
## Examples


```
LID.findAvailable;
LID.postAvailable; // pick one that you want to open, and fill in the vendor and product id in the next line:
d = LID.open(2, 10); // trackpoint

s.boot;

d.slot(2, 1).createBus;

Ndef(\checkbus, { d.slot(2, 1).kr.poll });

d.slot(2, 1).freeBus;

Ndef(\checkbus).clear;
```




