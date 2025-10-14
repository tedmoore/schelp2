# Message

*A message to an object*

**Categories:** Language

**Related:** [MethodQuote](../Classes/MethodQuote.md)

## Description

A message to an object, to be evaluated later.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `receiver` | the receiver of the message |  
| `selector` | the method to be called |  
| `args` | arguments to the call |  


## Instance Methods

### `receiver`
the object to which the message is relayed### `selector`
the method to be called### `args`
the arguments to the call### `value`
send the message to the receiver and call the selector with the arguments**Arguments:**

| Argument | Description |
|----------|-------------|
| `... moreArgs` |  |  

## Examples


```supercollider
// an object
a = 36


// a message to the object
m = Message(a, \sqrt)

// deliver the message
m.value
// -> 6

// a message that lacks an argument
m = Message(a, '+')

// evaluate with the argument
m.value(6)
// -> 42

m.value(-13)
// -> 23
```




