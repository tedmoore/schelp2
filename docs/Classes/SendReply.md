# SendReply

*Send an array of values from the server to all notified clients*

**Categories:** UGens>Triggers

**Related:** [SendTrig](../Classes/SendTrig.md), [OSCFunc](../Classes/OSCFunc.md)

## Description

A message is sent to all notified clients. See [Server](../Classes/Server.md).
- **cmdName**- int - node ID
- int - reply ID
- ... floats - values.




## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `trig` | a non-positive to positive transition triggers a message. |  
| `cmdName` | a string or symbol, as a message name. |  
| `values` | array of ugens, or valid ugen inputs. |  
| `replyID` | integer id (similar to [SendTrig](../Classes/SendTrig.md)). |  

## Examples


```
(
{
    SendReply.kr(Impulse.kr(3), '/the_answer', [40, 41, 42, 43] + MouseX.kr, 1905);
}.play(s);
)

o = OSCFunc({ |msg| msg.postln }, '/the_answer');


// multichannel expansion
(
{
    SendReply.kr(Impulse.kr(3),
        '/the_answer',
        values: [[40, 80], [41, 56], 42, [43, 100, 200]],
        replyID: [1905, 1906, 1907, 1908]
    );
}.play(s);
)

o.free;

// Sending audio parameters over a network via OSC
// Since SendReply can only respond to the host, this shows how
// to send data to a separate target through sclang.
(
SynthDef(\amplitudeAnalysis, { |in = 0, rate = 60|
    var input = SoundIn.ar(in);
    var amp = Amplitude.kr(input);
    var freq = Pitch.kr(input);
    var trig = Impulse.kr(rate);
    SendReply.kr(trig, '/analysis', [amp, freq[0], freq[1]]);
}).add;
)

// example target address - insert your target host & port here
~testNetAddr = NetAddr("127.0.0.1", 5000);
~mySynth = Synth(\amplitudeAnalysis);

(
OSCdef(\listener, { |msg|
    var data = msg[3..];
    data.postln;
    ~testNetAddr.sendMsg("data", data);
}, '/analysis');
)

~mySynth.set(\rate, 10); // slow it down...
```



### Identitying the time a message was sent
Sometimes, we need to know when a message was sent. Because `SendReply` can send only messages (which have no timestamp) and no bundles (which have), we can't use the `time` argument of the [OSCdef](../Classes/OSCdef.md)'s function. Instead, you can send a time stamp with the data, by using the [Sweep](../Classes/Sweep.md) UGen.


```
(
{ SendReply.ar(Impulse.ar(4), "/reply", [Sweep.ar, SinOsc.ar(0.3)]); 0 }.play;
OSCdef(\x, { |msg|
    var time, value;
    time = msg[3];
    value = msg[4];
    "value % occurred at time %".format(value, time).postln;
}, "/reply");
)
```






