# MIDIFunc

*Fast Responder for incoming MIDI Messages*

**Categories:** External Control>MIDI

**Related:** [MIDI](../Guides/MIDI.md), [MIDIdef](../Classes/MIDIdef.md)

## Description

MIDIFunc (and its subclass [MIDIdef](../Classes/MIDIdef.md)) registers one or more functions to respond to an incoming MIDI message. Many of its methods are inherited from its superclass [AbstractResponderFunc](../Classes/AbstractResponderFunc.md).

### Important note on persistence
MIDIFunc (and its subclass [MIDIdef](../Classes/MIDIdef.md) like all other AbstractResponderFuncs) are removed on pressing Cmd/ctrl-. To override this behavior, use the [AbstractResponderFunc#-permanent](../Classes/AbstractResponderFunc.md#-permanent) method.




## Class Methods


### `defaultDispatchers`
Get or set an [IdentityDictionary](../Classes/IdentityDictionary.md) containing the default dispatcher objects for MIDIFuncs of different types (these are what you get if you pass nil as the dispatcher argument to [#*new](#*new)). These objects will decide if any of their registered MIDIFuncs should respond to an incoming MIDI message. The dictionary should have the keys `[\noteOn, \noteOff, \control, \polytouch, \touch, \program, \bend]` and values of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md) for each message type. By default these will be instances of [MIDIMessageDispatcher](../Classes/MIDIMessageDispatcher.md) for the first four message types, and instances of [MIDIMessageDispatcherNV](../Classes/MIDIMessageDispatcherNV.md) for the last three.**Returns:** The getter returns an [IdentityDictionary](../Classes/IdentityDictionary.md).
### `new`
Create a new, enabled MIDIFunc. Normally one would use one of the message type specific convenience methods below, rather than use this method directly.**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. When evaluated for noteOn, noteOff, control, and polytouch messages it will be passed the arguments val, num, chan, and src, corresponding to the message value (e.g. velocity, control value, etc.), message number (e.g. note number), MIDI channel, and MIDI source uid. For touch, program change and bend messages it will be passed only val, chan, and src. For information on the args passed for the other sorts of `msgType` see the convenience methods below. |  
| `msgNum` | An [Integer](../Classes/Integer.md) indicating the MIDI message number (note number, control number, or program number) for this MIDIFunc. This can be an array. If nil, the MIDIFunc will respond to messages of all possible message numbers. |  
| `chan` | An [Integer](../Classes/Integer.md) indicating the MIDI channel number for this MIDIFunc. This can be an array. If nil, the MIDIFunc will respond to messages received on all channels. |  
| `msgType` | A [Symbol](../Classes/Symbol.md) indicating which kind of MIDI message this MIDIFunc should respond to. One of `\noteOn`, `\noteOff`, `\control`, `\touch`, `\polytouch`, `\bend`, `\program`, `\sysex`, `\mtcQF`, `\smpte`, `\songPosition`, `\songSelect`, `\tuneRequest`, `\midiClock`, `\sysrt`, `\tick`, `\start`, `\continue`, `\stop`, `\activeSense`, or `\reset`. |  
| `srcID` | An [Integer](../Classes/Integer.md) corresponding to the uid of the MIDI input. (See [UsingMIDI#MIDIFunc and MIDIdef: Filtering based on device or message data](../Guides/UsingMIDI.md#midifunc-and-mididef:-filtering-based-on-device-or-message-data).) If nil, the MIDIFunc will respond to messages received from all sources. |  
| `argTemplate` | An optional [Integer](../Classes/Integer.md) or [Function](../Classes/Function.md) (or object which responds to the method [Methods / matchItem ](../Overviews/Methods.md#matchitem)) used to match the value of an incoming MIDI message. (e.g. velocity, control value, program number, etc.). If a Function, it will be evaluated with the message value as an argument, and should return a [Boolean](../Classes/Boolean.md) indicating whether the message matches and this MIDIFunc should respond. |  
| `dispatcher` | An optional instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md). This can be used to allow for customised dispatching. Normally this should not be needed. |  
**Returns:** A new instance of MIDIFunc.
### `cc`
A convenience method to create a new MIDIFunc which responds to MIDI control messages. See [#*new](#*new) for argument descriptions.**Returns:** A new instance of MIDIFunc which responds to MIDI control messages.
### `noteOn`
A convenience method to create a new MIDIFunc which responds to MIDI note on messages. See [#*new](#*new) for argument descriptions.**Returns:** A new instance of MIDIFunc which responds to MIDI note on messages.
### `noteOff`
A convenience method to create a new MIDIFunc which responds to MIDI note off messages. See [#*new](#*new) for argument descriptions.**Returns:** A new instance of MIDIFunc which responds to MIDI note off messages.
### `polytouch`
A convenience method to create a new MIDIFunc which responds to MIDI polytouch messages. See [#*new](#*new) for argument descriptions.**Returns:** A new instance of MIDIFunc which responds to MIDI polytouch messages.
### `touch`
A convenience method to create a new MIDIFunc which responds to MIDI touch messages. See [#*new](#*new) for argument descriptions.**Returns:** A new instance of MIDIFunc which responds to MIDI touch messages.
### `bend`
A convenience method to create a new MIDIFunc which responds to MIDI bend messages. See [#*new](#*new) for argument descriptions.**Returns:** A new instance of MIDIFunc which responds to MIDI bend messages.
### `program`
A convenience method to create a new MIDIFunc which responds to MIDI program change messages. See [#*new](#*new) for argument descriptions.**Returns:** A new instance of MIDIFunc which responds to MIDI program change messages.
### `sysex`
A convenience method to create a new MIDIFunc which responds to MIDI system exclusive messages. See [#*new](#*new) for argument descriptions. The responding `func` will be passed the arguments data (an [Int8Array](../Classes/Int8Array.md)) and srcID.**Returns:** A new instance of MIDIFunc which responds to MIDI system exclusive messages.

### System Common
N.B. Because of SC's underlying low level MIDI implementation, there is no generic `msgType` and convenience method for System Common messages. Instead these are grouped with System Realtime under [#*sysrt](#*sysrt) below.

### `smpte`
A convenience method to create a new MIDIFunc which responds to MIDI smpte messages. See [#*new](#*new) for argument descriptions. The responding `func` will be passed the arguments seconds, framerate, dropframe, and srcID. (dropframe is a [Boolean](../Classes/Boolean.md)).**Returns:** A new instance of MIDIFunc which responds to MIDI smpte messages.
### `mtcQuarterFrame`
A convenience method to create a new MIDIFunc which responds to MIDI Time Code Quarter Frame messages. Note that the [#*smpte](#*smpte) method above automatically assembles quarter frames into time code. See [#*new](#*new) for argument descriptions. The responding `func` will be passed the arguments data, srcID, and pieceNumber. You will need to manually assemble each 8 messages into smpte.**Returns:** A new instance of MIDIFunc which responds to MIDI Time Code Quarter Frame messages.
### `songPosition`
A convenience method to create a new MIDIFunc which responds to MIDI song position messages. See [#*new](#*new) for argument descriptions. The responding `func` will be passed the arguments position and srcID.**Returns:** A new instance of MIDIFunc which responds to MIDI song position messages.
### `songSelect`
A convenience method to create a new MIDIFunc which responds to MIDI song select messages. See [#*new](#*new) for argument descriptions. The responding `func` will be passed the arguments song and srcID.**Returns:** A new instance of MIDIFunc which responds to MIDI song select messages.
### `tuneRequest`
A convenience method to create a new MIDIFunc which responds to MIDI tune request messages. See [#*new](#*new) for argument descriptions. The responding `func` will be passed the argument srcID.**Returns:** A new instance of MIDIFunc which responds to MIDI tune request messages.
### `midiClock`
A convenience method to create a new MIDIFunc which responds to MIDI clock messages. See [#*new](#*new) for argument descriptions. The responding `func` will be passed the argument srcID.**Returns:** A new instance of MIDIFunc which responds to MIDI clock messages.


### System Realtime
### `sysrt`
A convenience method to create a new MIDIFunc which responds generically to MIDI System Realtime and System Common messages. Note that the message specific methods above and below are probably more convenient in most cases. Note that this does not include MIDI Time Code Quarter Frame messages (sysrt index 1). For those see [#*mtcQuarterFrame](#*mtcquarterframe) and [#*smpte](#*smpte). See [#*new](#*new) for argument descriptions. The responding `func` will be passed the arguments data (may be nil), srcID, and index. Index indicates the message type as follows:| MIDI Time Code Quarter Frames | 1 | 
| --- | --- || Song Position | 2 | | Song Select | 3 | | Tune Request | 6 | | MIDI Clock | 8 | | Tick | 9 | | Start | 10 | | Continue | 11 | | Stop | 12 | | Active Sense | 14 | | Reset | 15 | **Returns:** A new instance of MIDIFunc which responds to MIDI System Realtime messages.
### `tick`
A convenience method to create a new MIDIFunc which responds to MIDI tick messages. See [#*new](#*new) for argument descriptions. The responding `func` will be passed the argument srcID.**Returns:** A new instance of MIDIFunc which responds to MIDI tick messages.
### `start`
A convenience method to create a new MIDIFunc which responds to MIDI start messages. See [#*new](#*new) for argument descriptions. The responding `func` will be passed the argument srcID.**Returns:** A new instance of MIDIFunc which responds to MIDI start messages.
### `stop`
A convenience method to create a new MIDIFunc which responds to MIDI stop messages. See [#*new](#*new) for argument descriptions. The responding `func` will be passed the argument srcID.**Returns:** A new instance of MIDIFunc which responds to MIDI stop messages.
### `continue`
A convenience method to create a new MIDIFunc which responds to MIDI continue messages. See [#*new](#*new) for argument descriptions. The responding `func` will be passed the argument srcID.**Returns:** A new instance of MIDIFunc which responds to MIDI continue messages.
### `reset`
A convenience method to create a new MIDIFunc which responds to MIDI reset messages. See [#*new](#*new) for argument descriptions. The responding `func` will be passed the argument srcID.**Returns:** A new instance of MIDIFunc which responds to MIDI reset messages.
### `activeSense`
A convenience method to create a new MIDIFunc which responds to MIDI active sense messages. See [#*new](#*new) for argument descriptions. The responding `func` will be passed the argument srcID.**Returns:** A new instance of MIDIFunc which responds to MIDI active sense messages.


### Debugging
### `trace`
A convenience method which dumps all incoming MIDI messages.**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | A [Boolean](../Classes/Boolean.md) indicating whether dumping is on or off. |  



## Instance Methods

### `chan`
Get this MIDIFunc's MIDI channel number.**Returns:** An [Integer](../Classes/Integer.md).### `msgNum`
Get this MIDIFunc's MIDI message number.**Returns:** An [Integer](../Classes/Integer.md).### `msgType`
Get this MIDIFunc's message type.**Returns:** A [Symbol](../Classes/Symbol.md); one of `\noteOn`, `\noteOff`, `\control`, `\touch`, `\polytouch`, `\bend`, `\program`, `\sysex`, `\mtcQF`, `\smpte`, `\songPosition`, `\songSelect`, `\tuneRequest`, `\midiClock`, `\sysrt`, `\tick`, `\start`, `\continue`, `\stop`, `\activeSense`, or `\reset`.### `argTemplate`
Get this MIDIFunc's argTemplate.**Returns:** A [Integer](../Classes/Integer.md) or [Function](../Classes/Function.md) (or object which responds to the method [Methods / matchItem ](../Overviews/Methods.md#matchitem)) used to match the value of an incoming MIDI message. (e.g. velocity, control value, program number, etc.).### `learn`
Train this MIDIFunc to respond to the next message of its type. Arguments passed at creation (e.g. chan, srcID, msgNum, etc.) will filter the training to the next matching message received.**Arguments:**

| Argument | Description |
|----------|-------------|
| `learnVal` | A [Boolean](../Classes/Boolean.md) indicating whether the responder should learn the specific value. For example, if used with a control change MIDIFunc, the object would learn to match the next specific control change value. If used with a note on MIDIFunc, it would match only a specific velocity. The default is false. |  

## Examples


```supercollider
MIDIIn.connectAll

a = MIDIFunc.cc({ |...args| args.postln }, 1); // match cc 1
a.free; // cleanup

b = MIDIFunc.cc({ |...args| args.postln }, 1, 1); // match cc1, chan 1
b.free; // cleanup

c = MIDIFunc.cc({ |...args| args.postln }, (1..10)); // match cc 1-10
c.free; // cleanup

n = MIDIFunc.noteOn({ |...args| args.postln }); // match any noteOn
n.free; // cleanup

MIDIIn.doNoteOnAction(1, 1, 64, 64); // spoof a note on
MIDIIn.doControlAction(1, 1, 1, 64); // spoof a cc
MIDIIn.doControlAction(1, 1, 9, 64);
MIDIIn.doControlAction(1, 10, 1, 64);
```




