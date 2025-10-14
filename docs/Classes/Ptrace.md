# Ptrace

*Print out the results of a stream*

**Related:** [Stream](../Classes/Stream.md), [FilterPattern](../Classes/FilterPattern.md)

**Categories:** Streams-Patterns-Events>Patterns

## Description

Print out the results of a stream while returning the original values.
Tracing a pattern is most commonly done by using the **.trace** method directly on the pattern like this:

```supercollider
Pbind(\degree, Pwhite(0, 10)).trace.play
```




## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `pattern` | printOn this stream (default: [Post](../Classes/Post.md)). |  
| `key` | when streaming events, post only this key. |  
| `printStream` | (describe argument here) |  
| `prefix` | string added to the printout to separate different streams. |  
**Returns:** Original values

## Instance Methods

### `storeArgs`
### `embedInStream`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `inval` |  |  
### `key`

## Examples


```supercollider
(
// An event pattern playing random scale degrees
p = Pbind(\dur, 0.125, \degree, Pwhite(0, 10));

// Se what the value of the scale degrees are using trace
Ptrace(p, \degree, prefix: "Current scale degree: ").play
)
```




