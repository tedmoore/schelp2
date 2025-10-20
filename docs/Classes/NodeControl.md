# NodeControl

*Encapsulates in an object a node and an index.*

**Categories:** Server>Nodes

## Description

This object can be held by a client and have its value set without otherwise having to store the details about where the node's input is.


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `node` | The node to encapsulate |  
| `index` | The index to encapsulate |  


## Instance Methods


### `value`
set the value
## Examples


```
d = SynthDef("help-NodeControl", { |out = 0, freq = 400|
    Out.ar(out,
         SinOsc.ar(freq, 0, 0.5)
    )
});
y = d.play; // the synth

c = NodeControl(y, 1);

c.value = 500;

c.value = 300;
```




