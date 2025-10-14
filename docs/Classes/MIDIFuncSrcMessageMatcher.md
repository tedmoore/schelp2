# MIDIFuncSrcMessageMatcher

*Matches incoming MIDI messages to responder funcs based on message source*

**Categories:** External Control>MIDI>Matchers

**Related:** [AbstractMessageMatcher](../Classes/AbstractMessageMatcher.md), [MIDIFuncChanMessageMatcher](../Classes/MIDIFuncChanMessageMatcher.md), [MIDIFuncChanArrayMessageMatcher](../Classes/MIDIFuncChanArrayMessageMatcher.md), [MIDIFuncSrcMessageMatcherNV](../Classes/MIDIFuncSrcMessageMatcherNV.md), [MIDIFuncBothMessageMatcher](../Classes/MIDIFuncBothMessageMatcher.md), [MIDIFuncBothCAMessageMatcher](../Classes/MIDIFuncBothCAMessageMatcher.md)

## Description

This is used by [MIDIMessageDispatcher](../Classes/MIDIMessageDispatcher.md) to match incoming MIDI messages to instances of [MIDIFunc](../Classes/MIDIFunc.md) or [MIDIdef](../Classes/MIDIdef.md) using message source. This class is private, and generally users should not need to address instances directly.


## Class Methods

### `new`
Make a new instance.**Arguments:**

| Argument | Description |
|----------|-------------|
| `srcID` | The UID of the MIDI source to test against as an [Integer](../Classes/Integer.md). |  
| `func` | The [Function](../Classes/Function.md) to evaluate if a match is found. |  
**Returns:** An MIDIFuncSrcMessageMatcher.

## Instance Methods

### `value`
Check to see if a message matches, and evaluate func if it does.**Arguments:**

| Argument | Description |
|----------|-------------|
| `value` | The message value (e.g. velocity, etc.) of the MIDI message as an [Integer](../Classes/Integer.md). Note this should be in the range 0-127. |  
| `num` | The message number (e.g. note number, etc.) of the MIDI message as an [Integer](../Classes/Integer.md). Note this should be in the range 0-127. |  
| `chan` | The channel number of the MIDI message as an [Integer](../Classes/Integer.md). Note this should be in the range 0-15. |  
| `testSrc` | The UID of the source of the MIDI message as an [Integer](../Classes/Integer.md). |  


