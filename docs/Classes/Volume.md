# Volume

*Model for the global volume of the synthesis server*

**Categories:** Server

## Description

Internally used by Server. When volume value != 0 dB or muted, a server's volume object will create a synth for controlling the volume on the main outputs for the number of channels given. For shared use of this volume synth with remote clients on this server, volume has its own group with fixed nodeID 2, and the synth (when present) uses the fixed nodeID 3.


## Class Methods


### `new`
Create and return a new instance of Volume for a given server, ranging from `startBus` over `numChans` (usually the server's number of output bus channels).**Arguments:**

| Argument | Description |
|----------|-------------|
| `server` | a server |  
| `startBus` | start bus |  
| `numChannels` | number of channels |  
| `min` | minimum volume in decibel |  
| `max` | minimum volume in decibel |  
| `persist` | whether to persist a reset |  


## Instance Methods


### `mute`
mute output
### `unmute`
unmute output
### `volume`
set the volume (in db)
### `lag`
set the lag time that dampens volume changes
### `setVolumeRange`
set the volume range
### `gui`
create a volume gui.
## Examples


```
v = s.volume;

v.min;
v.max;
v.volume = rrand(-50, 5);
v.setVolumeRange(-90, 8);
v.mute;
v.unmute;

// separate window
v.gui;
```




