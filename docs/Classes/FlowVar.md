# FlowVar

*A place holder, which when accessed pauses a thread until the place holder has a value*

**Categories:** Scheduling

**Related:** [Ref](../Classes/Ref.md), [Thunk](../Classes/Thunk.md), [Condition](../Classes/Condition.md), [Routine](../Classes/Routine.md)

## Description


```supercollider
(
a = FlowVar.new;
fork {
    "I am waiting, please enter a value ...".postln;
    a.value.postln;
    "...... ok, done.".postln;
}
)

// later, set the value. Then we can continue ...
a.value = 2;
```




## Class Methods

### `new`
Return a new instance,**Arguments:**

| Argument | Description |
|----------|-------------|
| `inVal` | If a value is given here, the FlowVar will not block execution. |  


## Instance Methods

### `value`
Set the value bound to the FlowVar.The getter returns the value bound to the FlowVar. If the value is not yet available, hold execution (this requires the method to be called from within a [Routine](../Classes/Routine.md) or similar thread.).**Arguments:**

| Argument | Description |
|----------|-------------|
| `inVal` | Any object. |  


