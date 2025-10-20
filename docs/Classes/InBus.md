# InBus

*Return a range of channels from a bus, irrespective of node order*

**Categories:** UGens>InOut

**Related:** [In](../Classes/In.md), [XIn](../Classes/XIn.md), [InFeedback](../Classes/InFeedback.md), [XInFeedback](../Classes/XInFeedback.md)

## Description

InBus provides a simple interface to the signal on a bus, crossfading between adjacent values.

```
(
b = Bus.control(s, 9); // nine channel control rate
b.setn([244, 737, 20, 271, 382, 172, 4, 2399, 251]);
{
    var index = MouseX.kr(0, 30);
    Blip.ar(InBus.ar(b, 2, index, \wrap)) * 0.1
}.play;
)
```




## Class Methods


### `ar`, `kr`
Return a new instance with the respective rate. If the bus rate doesn't match the signal is converted. Multi channel arguments expand.**Arguments:**

| Argument | Description |
|----------|-------------|
| `bus` | An instance of [Bus](../Classes/Bus.md) |  
| `numChannels` | Number of output channels |  
| `offset` | Offset to the starting index in the bus. |  
| `clip` | If clip is set to 'wrap', the indices into the bus will not be clipped to the last bus channel, but will wrap around. |  
**Returns:** A UGen output, usually an array of UGens or, if the arguments are arrays, an array of arrays.

## Instance Methods


## Examples


```
(
s.waitForBoot({
    b = Bus.control(s, 3);
    b.setn([1, 10, 100]);
})
)
{ InBus.kr(b, 1, 0).poll(2, "val"); 0.0 }.play;
{ InBus.kr(b, 1, 1).poll(2, "val"); 0.0 }.play;
{ InBus.kr(b, 1, 2).poll(2, "val"); 0.0 }.play;
{ InBus.kr(b, 1, 3).poll(2, "val"); 0.0 }.play;


{ InBus.kr(b, 2, 0).poll(2, "val"); 0.0 }.play;
{ InBus.kr(b, 3, 0).poll(2, "val"); 0.0 }.play;
{ InBus.kr(b, 4, 0).poll(2, "val"); 0.0 }.play;

{ InBus.kr(b, 3, 5).poll(2, "val"); 0.0 }.play;
{ InBus.kr(b, 3, 5, \wrap).poll(2, "val"); 0.0 }.play;

 InBus.kr(b, 2, [1, 3, 4]); // multi channel expansion

{ InBus.kr(b, 1, MouseX.kr(0, 10).round.poll(2, "index")).poll(2, "val"); 0.0 }.play;
{ InBus.kr(b, 2, MouseX.kr(0, 10).round.poll(2, "index")).postln.poll(2, "val"); 0.0 }.play;
{ InBus.kr(b, 3, MouseX.kr(0, 10).round.poll(2, "index")).postln.poll(2, "val"); 0.0 }.play;
{ InBus.kr(b, 4, MouseX.kr(0, 10).round.poll(2, "index")).postln.poll(2, "val"); 0.0 }.play;

{ InBus.kr(b, 1, MouseX.kr(0, 10).round.poll(2, "index"), \wrap).poll(2, "val"); 0.0 }.play;
{ InBus.kr(b, 2, MouseX.kr(0, 10).round.poll(2, "index"), \wrap).postln.poll(2, "val"); 0.0 }.play;
{ InBus.kr(b, 3, MouseX.kr(0, 10).round.poll(2, "index"), \wrap).postln.poll(2, "val"); 0.0 }.play;
{ InBus.kr(b, 4, MouseX.kr(0, 10).round.poll(2, "index"), \wrap).postln.poll(2, "val"); 0.0 }.play;
```




