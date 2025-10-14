# SerialPort

*serial port interface*

**Categories:** External Control

This class provides basic support for serial port communication. Ports are opened with [#*new](#*new) and closed with [#-close](#-close).
Each SerialPort object uses an 8KB internal buffer and reads data as soon as it is available. If the data is not read out of the buffer and the buffer fills up, incoming bytes will be dropped. Use [#-rxErrors](#-rxerrors) to get a count of the number of bytes dropped.
Since it is constantly polling the port for available data, a SerialPort object knows almost immediately when the port has been lost. When this happens, it will call the [#-doneAction](#-doneaction) callback and mark itself as closed.

## Class Methods


### `new`
Creates and opens the port. Throws if creation fails; this may be because the port does not exist, the port could not be opened, or the settings were invalid.**Arguments:**

| Argument | Description |
|----------|-------------|
| `port` | A [String](../Classes/String.md) representing the port to be opened. (An [Integer](../Classes/Integer.md) index into [#*devices](#*devices) is allowed, but this is deprecated.) |  
| `baudrate` | Integer baud rate, typically in the range `[4800..230400]`. |  
| `databits` | Bits per character. Typically 8, but can be any integer. |  
| `stopbit` | A [Boolean](../Classes/Boolean.md) indicating whether to use two stop bits (`true`) or one stop bit (`false`). |  
| `parity` | Whether the port uses even, odd, or no parity. Pass `'even'`, `'odd'`, or `nil` (for none). |  
| `crtscts` | A [Boolean](../Classes/Boolean.md) indicating whether to use hardware flow control (RTS/CTS signals). |  
| `xonxoff` | A [Boolean](../Classes/Boolean.md) indicating whether to use software flow control (XON/XOFF signals). |  
| `exclusive` | A [Boolean](../Classes/Boolean.md) indicating whether to open the device exclusively. This option is not implemented on Windows. |  
`crtscts` and `xonxoff` cannot both be true; `*new` will throw an error if both are set.
### `devices`
Retrieve an array of available devices represented as [Strings](../Classes/String.md). On macOS and Linux, this list is obtained using a number of regular expression rules on files in the `/dev/` directory. On Windows, this is obtained using a registry key. The matching rules are designed to be identical to that of the Arduino IDE.For backward compatibility, if `SerialPort.devicePattern` is not nil, `SerialPort.devicePattern.pathMatch` is returned instead of the default behavior.
```supercollider
SerialPort.devices;
```


### `listDevices`
Prints the list of available devices, one per line. Shorthand for `SerialPort.devices.do(_.postln)`.
```supercollider
SerialPort.listDevices;
```


### `devicePattern`
If set to a non-nil value, `SerialPort.devicePattern` instead returns `SerialPort.devicePattern.patchMatch`. That is, the value of this class variable is used as a file glob.This is a legacy feature and no longer recommended. File globbing alone is not powerful enough to capture a general set of possible serial port paths, and this level of customization was not necessary for `SerialPort.devices`. If you need to refine the results returned by `SerialPort.devices`, it is better to do your own matching or filtering.
### `closeAll`
Calls [#-close](#-close) on all ports.
### `cleanupAll`
Deprecated; use [#*closeAll](#*closeall) instead.

## Instance Methods

### `isOpen`
Whether this object represents a valid serial port connection.### `next`
Read a byte from the device. Non-blocking read.### `read`
Read a byte from the device. Blocking read.### `rxErrors`
RX (receive) errors since last query. An RX error occurs when the internal buffer is completely full. This count is reset to 0 every time this method is called.### `put`
Write a byte to the device. Always blocks.**Arguments:**

| Argument | Description |
|----------|-------------|
| `byte` | An [Integer](../Classes/Integer.md) or [Char](../Classes/Char.md). Only values in the range from 0 to `2**databits - 1` may be written. If a value out of that range is passed to `put`, only the lowest bits will be used. |  
| `timeout` | Unused, deprecated. |  
**Returns:** A [Boolean](../Classes/Boolean.md) indicating whether the write was successful.### `putAll`
Write multiple bytes to the device.**Arguments:**

| Argument | Description |
|----------|-------------|
| `bytes` | Collection may be [Int8Array](../Classes/Int8Array.md) or [String](../Classes/String.md). |  
| `timeout` | Unused, deprecated. |  
### `doneAction`
A [Function](../Classes/Function.md) which will be evaluated if the port gets closed (maybe unexpectedly so, due to hardware failure or accidental disconnection). This allows you to for example to make a backup solution and activate it (like using fake input data for your algorithm, or trying to reopen the device). By default it will post a message reading "SerialPort X was closed".### `close`
Closes the port.
## Examples


```supercollider
(
p = SerialPort(
    "/dev/tty.usbserial-181",
    baudrate: 9600,
    crtscts: true);
)

// read a byte from the device

p.next; // doesn't block
fork { p.read.postln }; // may suspend thisThread - should be called within a routine

// write a byte to the device

fork { p.put(42) }; // may suspend thisThread - should be called within a routine

// write multiple bytes to the device

fork { p.putAll("whaddayawant") };
fork { p.putAll(Int8Array[13, 10]) };

p.doneAction = { "my serial port got closed".postln }

p.close; // close the port

SerialPort.closeAll; // close all ports
```



### Arduino write example
First load the sketch Examples/Communication/Dimmer. See [http://www.arduino.cc/en/Tutorial/Dimmer](http://www.arduino.cc/en/Tutorial/Dimmer).


> **Note:** Always make sure the serial monitor is closed in the Arduino application before opening the port in SuperCollider.



```supercollider
(
p = SerialPort(
    "/dev/tty.usbserial-A800crTT",    // edit to match your port. SerialPort.listDevices
    baudrate: 9600,    // check that baudrate is the same as in arduino sketch
    crtscts: true);
)

// send serial data - slow pulsating
(
r = Routine({
    inf.do{ |i|
        p.put(i.fold(0, 100).linexp(0, 100, 1, 255).asInteger.postln);
        0.02.wait;
    };
}).play;
)

r.stop;
p.close;
```




### Arduino read example
First load the sketch Examples/Communication/Graph. See [http://www.arduino.cc/en/Tutorial/Graph](http://www.arduino.cc/en/Tutorial/Graph).


> **Note:** Always make sure the serial monitor is closed in the Arduino application before opening the port in SuperCollider.



```supercollider
(
p = SerialPort(
    "/dev/tty.usbserial-A800crTT",    // edit to match your port. SerialPort.listDevices
    baudrate: 9600,    // check that baudrate is the same as in arduino sketch
    crtscts: true);
)

// read 10bit serial data sent from Arduino's Serial.println
(
r = Routine({
    var byte, str, res;
    99999.do{ |i|
        if(p.read == 10, {
            str = "";
            while({ byte = p.read; byte != 13 }, {
                str = str++byte.asAscii;
            });
            res = str.asInteger;
            ("read value:"+res).postln;
        });
    };
}).play;
)

r.stop;
p.close;
```






