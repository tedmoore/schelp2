# MIDIMessageDispatcherNV

*The default dispatcher for MIDIFunc's and MIDIdef's set to respond to touch, program, and bend messages.*

**Categories:** External Control>MIDI>Dispatchers

**Related:** [MIDIFunc](../Classes/MIDIFunc.md), [MIDIdef](../Classes/MIDIdef.md), [AbstractWrappingDispatcher](../Classes/AbstractWrappingDispatcher.md), [AbstractDispatcher](../Classes/AbstractDispatcher.md), [MIDIMessageDispatcher](../Classes/MIDIMessageDispatcher.md), [AbstractMessageMatcher](../Classes/AbstractMessageMatcher.md), [MIDIFuncSrcMessageMatcher](../Classes/MIDIFuncSrcMessageMatcher.md), [MIDIFuncChanMessageMatcher](../Classes/MIDIFuncChanMessageMatcher.md), [MIDIFuncChanArrayMessageMatcher](../Classes/MIDIFuncChanArrayMessageMatcher.md), [MIDIFuncSrcMessageMatcherNV](../Classes/MIDIFuncSrcMessageMatcherNV.md), [MIDIFuncBothMessageMatcher](../Classes/MIDIFuncBothMessageMatcher.md), [MIDIFuncBothCAMessageMatcher](../Classes/MIDIFuncBothCAMessageMatcher.md), [MIDI](../Guides/MIDI.md)

## Description

MIDIMessageDispatcherNV is used to dispatch incoming MIDI touch, program, and bend messages to matching functions. Normally users should not have to create or message instances of this class directly.


## Class Methods


## Instance Methods

### `getKeysForFuncProxy`
Get the keys at which a responder func's functions are stored in this dispatcher's active dictionary. The keys will be MIDI channels.**Arguments:**

| Argument | Description |
|----------|-------------|
| `funcProxy` | The [MIDIFunc](../Classes/MIDIFunc.md) or [MIDIdef](../Classes/MIDIdef.md) whose keys should be returned. |  
**Returns:** An [Array](../Classes/Array.md) containing the funcProxy's channel number as an [Integer](../Classes/Integer.md).### `value`
Attempt to match an incoming MIDI message with this dispatcher's responder funcs, and evaluate their functions for all matches found.**Arguments:**

| Argument | Description |
|----------|-------------|
| `src` | The UID of the source of the MIDI message as an [Integer](../Classes/Integer.md). |  
| `chan` | The channel number of the MIDI message as an [Integer](../Classes/Integer.md). Note this should be in the range 0-15. |  
| `val` | The message value (e.g. velocity, etc.) of the MIDI message as an [Integer](../Classes/Integer.md). Note this should be in the range 0-127. |  
### `wrapFunc`
Called internally to wrap functions in message matcher objects, if needed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `funcProxy` | An instance of [MIDIFunc](../Classes/MIDIFunc.md) or [MIDIdef](../Classes/MIDIdef.md) whose function(s) are to be wrapped. |  


