# MIDIClient

*Basic access to MIDI on your computer*

**Categories:** External Control>MIDI

**Related:** [MIDIIn](../Classes/MIDIIn.md), [MIDIOut](../Classes/MIDIOut.md), [MIDIFunc](../Classes/MIDIFunc.md), [MIDIdef](../Classes/MIDIdef.md), [MIDI](../Guides/MIDI.md), [UsingMIDI](../Guides/UsingMIDI.md), [MIDIEndPoint](../Classes/MIDIEndPoint.md)

## Description

MIDIClient is the core class that provides access to the MIDI subsystem on your computer.
See the [UsingMIDI](../Guides/UsingMIDI.md) helpfile for practical considerations and techniques for using MIDI in SC.


## Class Methods



### `init`
Initializes the MIDIClient, checks which available MIDI sources and destinations there are, and opens as many connections as desired.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inports` | the number of MIDI input connections to open; if `nil` then opens as many inports as there are MIDI sources. |  
| `outports` | the number of MIDI output connections to open; if `nil` then opens as many outports as there are MIDI destinations. |  
| `verbose` | A flag whether or not to post the MIDI sources and destinations that were found. Default is true. |  


### `initialized`
A flag that tells whether of not the MIDIClient has been initialized.

### `disposeClient`
Cleans up the MIDIClient. After using this method, you will have to reinitialize the MIDIClient before you can use MIDI again.

### `list`
Refresh the list of available sources and destinations. If you have connected a MIDI device after MIDIClient initialization, you won't see it until this method is run.

### `sources`
The list of available MIDI sources, including SuperCollider's own sources.**Returns:** A `List` of `MIDIEndPoints`

### `externalSources`
The list of available MIDI sources, excluding SuperCollider's own sources. Only on Linux the list of `sources` and `externalSources` differs.**Returns:** A `List` of `MIDIEndPoints`

### `destinations`
The list of available MIDI destinations, including SuperCollider's own destinations.**Returns:** A `List` of `MIDIEndPoints`

### `externalDestinations`
The list of available MIDI destinations, excluding SuperCollider's own destinations. Only on Linux the list of `destinations` and `externalDestinations` differs.**Returns:** A `List` of `MIDIEndPoints`

### `restart`
Restart the MIDIClient.

### `myinports`
The number of input ports that SuperCollider created. This is mainly useful to know on the Linux platform.

### `myoutports`
The number of output ports that SuperCollider created. This is mainly useful to know on the Linux platform.

### `getClientID`
Linux only. This gets the client ID by which the MIDIClient is defined in the ALSA subsystem. It can be used to identify whether a port is belonging to this client or another one.On non-linux systems, it posts a warning and returns nil.
## Examples

This is Linux specific code. The function takes care of initializing MIDIClient, detects a MIDI device named SE25 and connects it to port 0 of SuperCollider.

```
(
~connect_midi_devices = { |device, name|
    // init or refresh MIDIClient end points
    if(MIDIClient.initialized == false) {
        MIDIClient.init;
    } {
        MIDIClient.list;
    };

    MIDIClient.sources.do({ |endPoint|
        if(device.notNil and: { name.notNil } and: { endPoint.device == device } and: { endPoint.name == name }) {
            // catch exception thrown when already connected
            try {
                // connect SuperCollider out port 0 to MIDI device
                MIDIOut.connect(0, endPoint.uid);
            };
            try {
                // connect MIDI device to SuperCollider in port 0
                MIDIIn.connect(0, endPoint.uid);
            }
        }
    })

}
)

~connect_midi_devices.("SE25", "SE25 MIDI 1"); // test it now
```




