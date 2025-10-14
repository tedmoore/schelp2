# 07_SynthDefs

*Mark Polishook tutorial*

**Categories:** Tutorials>Mark_Polishook_tutorial

**Related:** [Mark_Polishook_tutorial/00_Introductory_tutorial](../../Tutorials/Mark_Polishook_tutorial/00_Introductory_tutorial.md)


## SynthDefs
Use the SynthDef class to build the engines for synths that will run on the server. The engines, which can be saved to disk and reused, are analogous to presets on commercial hardware and software synthesizers.

When notated as code in client programs, the engines have two essential parts: a name and a function. In the jargon of SuperCollider, the function is called a ugenGraphFunc.

The term ugenGraphFunc derives from the notion of a graph, which is the data structure that SuperCollider uses to organize unit generators. SuperCollider constructs the graph for you from the code it finds in your function which means that don't have to know how a graph works or that it even exists.

If you wish to know more about graphs, visit the Wikipedia at

[http://en.wikipedia.org/wiki/Graph_(data_structure)](http://en.wikipedia.org/wiki/Graph_(data_structure))

Or, go to

[http://www.nist.gov/dads/HTML/graph.html](http://www.nist.gov/dads/HTML/graph.html)



## Template
Here's a template for a synthdef showing that it consists of a name and a ugenGraphFunc


```supercollider
SynthDef(
    "aSynthDef",                // the 1st argument is the name
    { .... i am a ugenGraphFunc ... }    // the 2nd argument is the ugenGraphFunc
)
```


To make the template functional

1. put code into the ugenGraphFunc
2. send a .load message to the synthdef



```supercollider
(
SynthDef(
    "aSynthDef",                 // the name of the synthdef
    {                     // the ugenGraphFunc with actual code
        arg freq;
        Out.ar(
            0,
            SinOsc.ar(freq, 0, 0.1)
        )
    }
).load(s);
)
```




## The .load message and the variable 's'
The .load message writes synthdefs to disk and also sends them to the default server. The default server is defined by SuperCollider at startup time (as the localhost server) at which point it's also assigned to the variable 's'.



## The .send message and a remote server
On the other hand, .send message,


```supercollider
SynthDef( .... ).send(s);
```


instead of a .load message


```supercollider
SynthDef( .... ).load(s);
```


is another way to get a synthdef to a server. The .send message, unlike the .load message, doesn't first write the synthdef to disk; instead it just transmits the synthdef directly to the server. This is therefore the message to use to define a synthdef on one computer but send it to another.


```supercollider
(
var aServer;
aServer =
    Server(
        "aRemoteServerOnAnotherMachine",
        NetAddr("... an ip # ...", 57110)    // a server on another computer
    );
SynthDef( .... ).send(aServer);
)
```



> **Note:** Since this tutorial was written, another general purpose method was added to SynthDef. It is called **.add** and will be the new recommended standard instead of .load and .send.




## SynthDef browsers
Use the synthdef browser to examine synthdefs that have been written to disk.


```supercollider
(
// a synthdef browser
SynthDescLib.global.read;
SynthDescLib.global.browse;
)
```


The middle box (in the top row) shows the names of synthdefs. Each name, when selected, causes the other boxes to display the ugens, controls, and inputs and outputs for a particular synthdef.

The box labeled "SynthDef controls" is useful because it shows the arguments that can be passed to a given synthdef.

The browser shows that the synthdef defined above - "aSynthDef" - is composed from four ugens, one control, no inputs, and one output. The four ugens include instances of Control, SinOsc, BinaryOpUGen, and Out classes.

The one control is "freq". A control is an argument that a synth can use when it is created or at any time while it (the synth) exists on the server. The browser also shows that "aSynth" has no inputs (which means that it doesn't use data from audio or control buses) and that it sends one channel of audio out to an audio Bus.

////////////////////////////////////////////////////////////////////////////////////////////////////

For further context, see the [SynthDef](../../Classes/SynthDef.md), [In](../../Classes/In.md), [Out](../../Classes/Out.md), [SinOsc](../../Classes/SinOsc.md), [Control](../../Classes/Control.md), [BinaryOpUGen](../../Classes/BinaryOpUGen.md) files in the SuperCollider help system.

////////////////////////////////////////////////////////////////////////////////////////////////////

go to [Mark_Polishook_tutorial/08_Rates](../../Tutorials/Mark_Polishook_tutorial/08_Rates.md)



