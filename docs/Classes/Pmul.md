# Pmul

*multiply with value of a key in event stream*

**Related:** [Padd](../Classes/Padd.md), [Pmulp](../Classes/Pmulp.md)

**Categories:** Streams-Patterns-Events>Patterns>Math


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | the key |  
| `value` | can be a pattern or a stream. The resulting stream ends when that incoming stream ends. |  
| `pattern` | the pattern |  

## Examples


```supercollider
(
var a, b;
a = Pmul(\freq, 801, Pbind(\freq, 100));
x = a.asStream;
9.do({ x.next(Event.new).postln });
)
```



```supercollider
(
var a, b;
a = Pmul(\freq, Pseq([3, 4, 6], 2), Pbind(\freq, 100));
x = a.asStream;
9.do({ x.next(Event.new).postln });
)
```



```supercollider
// sound example
(
SynthDef(\sinegrain,
    { |out = 0, freq = 440, gate = 1|
        var env;
        env = EnvGen.kr(Env.asr(0.001, 1, 0.2), gate, doneAction: Done.freeSelf);
        Out.ar(out, SinOsc.ar(freq, 0, env * 0.1))
    }).add;
)

(
a = Pbind(\dur, 0.5, \instrument, \sinegrain, \freq, 440);
b = Pmul(\freq, Pseq([1, 2, 3, 4, 5, 6, 7], inf), a);
b.play;
)
```




