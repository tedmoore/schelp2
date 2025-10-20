# AbstractMessageMatcher

*Matches incoming messages to Functions*

**Categories:** External Control>Abstract Classes

**Related:** [AbstractResponderFunc](../Classes/AbstractResponderFunc.md), [AbstractWrappingDispatcher](../Classes/AbstractWrappingDispatcher.md)

## Description

Instances of subclasses of AbstractMessageMatcher are used by subclasses of [AbstractWrappingDispatcher](../Classes/AbstractWrappingDispatcher.md) to match multiple parameters of incoming messages (i.e. OSC or MIDI) to instances of subclasses of [AbstractResponderFunc](../Classes/AbstractResponderFunc.md). This class and its subclasses are private and generally users should not need to address them directly.


## Class Methods


## Instance Methods


### `func`
Get or set this object's response [Function](../Classes/Function.md).**Returns:** A [Function](../Classes/Function.md) or similar object.
### `value`
Evaluate an incoming message to see if it matches. Subclasses should override this message to take appropriate arguments. If a match is found, this method should call value on this object's func, passing the message as appropriate arguments.
### `valueArray`
As [#-value](#-value) above, but with the arguments passed as a single [Array](../Classes/Array.md). This method is needed so that subclasses can work in FunctionLists.**Arguments:**

| Argument | Description |
|----------|-------------|
| `args` | An [Array](../Classes/Array.md) containing the message and appropriate arguments. |  


