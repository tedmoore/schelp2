# Unit Generators and Synths

*Introduction to some fundamental concepts*

**Categories:** Server>Nodes

A unit generator is an object that processes or generates sound. There are many classes of unit generators, all of which derive from the class [UGen](../Classes/UGen.md).
Unit generators in SuperCollider can have many inputs, but always have a single output. Unit generator classes which would naturally have several outputs such as a panner, return an array of unit generators when instantiated. The convention of having only a single output per unit generator allows the implementation of multiple channels by using arrays of unit generators. (See [Multichannel-Expansion](../Guides/Multichannel-Expansion.md) for more details.)

## Instantiation. Audio Rate, Control Rate
A unit generator is created by sending the 'ar' or 'kr' message to the unit generator's class object. The 'ar' message creates a unit generator that runs at audio rate. The 'kr' message creates a unit generator that runs at control rate. Control rate unit generators are used for low frequency or slowly changing control signals. Control rate unit generators produce only a single sample per control cycle and therefore use less processing power than audio rate unit generators.

The input parameters for a unit generator are given in the documentation for that class.


```
FSinOsc.ar(800, 0.0, 0.2); // create a sine oscillator at 800 Hz, phase 0.0, amplitude 0.2
```


A unit generator's signal inputs can be other unit generators, scalars, or arrays of unit generators and scalars.



## SynthDefs and Synths
In order to play a unit generator one needs to compile it in a [SynthDef](../Classes/SynthDef.md) and play it on the server in a [Synth](../Classes/Synth.md). A synth node is a container for one or more unit generators that execute together. A SynthDef is like a kind of pattern for creating synth nodes on the server.


```
s.boot; // boot the server

// compile and send this def
SynthDef.new("FSinOsc-test", { Out.ar(0, FSinOsc.ar(800, 0, 0.2)) }).send(s); // out channel 0

// now create a Synth object which represents a synth node on the server
x = Synth.new("FSinOsc-test");

// free the synth
x.free;
```


The synth node created above could also be created using 'messaging style', thus saving the overhead of a clientside Synth object:


```
n = s.nextNodeID;
s.sendMsg("/s_new", "FSinOsc-test", n);
s.sendMsg("/n_free", n);
```


Because any expression returns its value, we can nest the first two lines above for convenience. (See [Expression-Sequence](../Reference/Expression-Sequence.md) for more detail.)


```
s.sendMsg("/s_new", "FSinOsc-test", n = s.nextNodeID;);
s.sendMsg("/n_free", n);
```


It is VERY important and useful to understand the messaging structure which underlies the clientside Synth, Group, Buffer, and Bus objects. See [NodeMessaging](../Guides/NodeMessaging.md), [Server_Tutorial](../Tutorials/Server_Tutorial.md), and [ClientVsServer](../Guides/ClientVsServer.md) for more detail.

As a convenience the 'play' method of class [Function](../Classes/Function.md) will compile a SynthDef and create and play a synth using the function for you. With this method an [Out](../Classes/Out.md) ugen will be created for you if you do not do so explicitly.


```
{ FSinOsc.ar(800, 0, 0.2) }.play; // create and play a sine oscillator at 800 Hz
```




## Building Patches
You can do math operations on unit generators and the result will be another unit generator. Doing math on unit generators is not doing any signal calculation itself - it is building the network of unit generators that will execute once they are played in a Synth. This is the essential thing to understand: Synthesis networks, or in other words signal flow graphs are created by executing expressions of unit generators. The following expression creates a flow graph whose root is an instance of [BinaryOpUGen](../Classes/BinaryOpUGen.md) which performs the '+' operation. Its inputs are the [FSinOsc](../Classes/FSinOsc.md) and [BrownNoise](../Classes/BrownNoise.md) unit generators.


```
FSinOsc.ar(800, 0.0, 0.2) + BrownNoise.ar(0.2); // press enter and look at the post window

{FSinOsc.ar(800, 0.0, 0.2) + BrownNoise.ar(0.2)}.play; // play it
```






