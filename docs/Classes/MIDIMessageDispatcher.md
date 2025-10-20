# MIDIMessageDispatcher

*The default dispatcher for MIDIFunc's and MIDIdef's set to respond to noteOn, noteOff, control, and polytouch messages.*

**Categories:** External Control>MIDI>Dispatchers

**Related:** [MIDIFunc](../Classes/MIDIFunc.md), [MIDIdef](../Classes/MIDIdef.md), [AbstractWrappingDispatcher](../Classes/AbstractWrappingDispatcher.md), [AbstractDispatcher](../Classes/AbstractDispatcher.md), [MIDIMessageDispatcherNV](../Classes/MIDIMessageDispatcherNV.md), [AbstractMessageMatcher](../Classes/AbstractMessageMatcher.md), [MIDIFuncSrcMessageMatcher](../Classes/MIDIFuncSrcMessageMatcher.md), [MIDIFuncChanMessageMatcher](../Classes/MIDIFuncChanMessageMatcher.md), [MIDIFuncChanArrayMessageMatcher](../Classes/MIDIFuncChanArrayMessageMatcher.md), [MIDIFuncSrcMessageMatcherNV](../Classes/MIDIFuncSrcMessageMatcherNV.md), [MIDIFuncBothMessageMatcher](../Classes/MIDIFuncBothMessageMatcher.md), [MIDIFuncBothCAMessageMatcher](../Classes/MIDIFuncBothCAMessageMatcher.md), [MIDI](../Guides/MIDI.md)

## Description

MIDIMessageDispatcher is used to dispatch incoming MIDI noteOn, noteOff, control, and polytouch messages to matching functions. Normally users should not have to create or message instances of this class directly.


## Class Methods


### `new`
Create a new instance.**Arguments:**

| Argument | Description |
|----------|-------------|
| `messageType` | A [Symbol](../Classes/Symbol.md) indicating the message type, one of `\noteOn`, `\noteOff`, `\control`, or `\polytouch`. |  
**Returns:** A new MIDIMessageDispatcher.

## Instance Methods


### `messageType`
Get this dispatcher's message type, one of `\noteOn`, `\noteOff`, `\control`, or `\polytouch`.**Returns:** A [Symbol](../Classes/Symbol.md).
### `getKeysForFuncProxy`
Get the keys at which a responder func's functions are stored in this dispatcher's active dictionary. The keys will be MIDI message numbers.**Arguments:**

| Argument | Description |
|----------|-------------|
| `funcProxy` | The [MIDIFunc](../Classes/MIDIFunc.md) or [MIDIdef](../Classes/MIDIdef.md) whose keys should be returned. |  
**Returns:** An [Array](../Classes/Array.md) containing the funcProxy's message number as an [Integer](../Classes/Integer.md).
### `value`
Attempt to match an incoming MIDI message with this dispatcher's responder funcs, and evaluate their functions for all matches found.**Arguments:**

| Argument | Description |
|----------|-------------|
| `src` | The UID of the source of the MIDI message as an [Integer](../Classes/Integer.md). |  
| `chan` | The channel number of the MIDI message as an [Integer](../Classes/Integer.md). Note this should be in the range 0-15. |  
| `num` | The message number (e.g. note number, etc.) of the MIDI message as an [Integer](../Classes/Integer.md). Note this should be in the range 0-127. |  
| `val` | The message value (e.g. velocity, etc.) of the MIDI message as an [Integer](../Classes/Integer.md). Note this should be in the range 0-127. |  

### `register`
Adds this dispatcher to the appropriate receive hook in [MIDIIn](../Classes/MIDIIn.md).
### `unregister`
Removes this dispatcher from the appropriate receive hook in [MIDIIn](../Classes/MIDIIn.md).
### `wrapFunc`
Called internally to wrap functions in message matcher objects, if needed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `funcProxy` | An instance of [MIDIFunc](../Classes/MIDIFunc.md) or [MIDIdef](../Classes/MIDIdef.md) whose function(s) are to be wrapped. |  

### `typeKey`
Gets a key indicating the type of message this dispatcher responds to, in the form: `('MIDI ' ++ messageType).asSymbol`.**Returns:** A [Symbol](../Classes/Symbol.md).

