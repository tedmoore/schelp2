# Spawner

*A Spawner*

**Categories:** Streams-Patterns-Events>Composition

**Related:** [Pspawner](../Classes/Pspawner.md)

## Description

Can start subpatterns. Used as an argument inside [Pspawner](../Classes/Pspawner.md). Tracks subpatterns in a [PriorityQueue](../Classes/PriorityQueue.md).


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` |  |  
| `stackSize` |  |  


## Instance Methods


### `par`
Begin an event stream in parallel to the routine. If delta is non-zero, the pattern will begin that many beats after **now**, provided that **now + delta** is later than the next event that the Spawner will generate.**Arguments:**

| Argument | Description |
|----------|-------------|
| `pattern` | A [Pattern](../Classes/Pattern.md). |  
| `delta` | A number of beats. |  
**Returns:** The stream from **pattern**.
### `seq`
Begin an event stream. Do not return until the event is finished.**Arguments:**

| Argument | Description |
|----------|-------------|
| `pattern` | A [Pattern](../Classes/Pattern.md). |  

### `wait`
Wait a number of seconds, then return.**Arguments:**

| Argument | Description |
|----------|-------------|
| `dur` | A number of seconds. |  

### `suspend`
Stops a stream.**Arguments:**

| Argument | Description |
|----------|-------------|
| `stream` | An index of the underlying [PriorityQueue](../Classes/PriorityQueue.md). |  
**Returns:** The stopped stream, or nil if the stream is not found.
### `suspendAll`
Stop all substreams.
## Examples

See [Pspawner](../Classes/Pspawner.md)

