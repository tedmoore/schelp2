# Warp

*specification of a shape for a mapping of numerical input*

**Related:** [ControlSpec](../Classes/ControlSpec.md), [Spec](../Classes/Spec.md)

**Categories:** Control, Spec

## Description

The subclasses of Warp specify translations from input (a number) to an output (another number). This is an abstract class - already available shapes are *linear, exponential, sine, cosine, decibel, curve* (this is similar to the curves in envelopes, see also [Env](../Classes/Env.md)).
Warps are internally created by [ControlSpec](../Classes/ControlSpec.md). Usually they are created by the message **asWarp**, understood by symbols and numbers. A warp has a [Spec](../Classes/Spec.md) to specify a certain range of input and output values.

```supercollider
// create a new warp:
a = \exp.asWarp;
a = -4.asWarp; // a curve warp;
```




## Class Methods



## Instance Methods

### `map`
Maps and constrains a **value** between 0 and 1 to the output domain.### `unmap`
in the output domain to a value in the range between 0 and 1.
```supercollider
g = -3.asWarp;
g.map(0.5);
g.unmap(0.9);

// fore and back translation should be identical:
g.unmap(g.map(0.5));
```



