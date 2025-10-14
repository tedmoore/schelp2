# 09_Buses

*Mark Polishook tutorial*

**Categories:** Tutorials>Mark_Polishook_tutorial

**Related:** [Mark_Polishook_tutorial/00_Introductory_tutorial](../../Tutorials/Mark_Polishook_tutorial/00_Introductory_tutorial.md)

By default, SuperCollider has 1024 buses for audio signals and 16,384 for control signals. The buses, which are items in an array, are what SuperCollider uses to represent audio and control rate data.
////////////////////////////////////////////////////////////////////////////////////////////////////

```supercollider
// the array of audio buses (channels)
[ channel0, channel1, channel2, channel3, channel4, ... , ..., ..., etc., ... channel127 ]

// the array of control buses (channels)
[ channel0, channel1, channel2, channel3, channel4, ... , ..., ..., etc., ... channel4095 ]
```


## Placing audio into a bus
Use an Out ugen at the audio rate to put data into an audio bus.


```supercollider
(
SynthDef("dataForABus", {
    Out.ar(
        0,        // write 1 channel of audio into bus 0
        Saw.ar(100, 0.1)
    )
}).add;
)

Synth("dataForABus");
```


A SynthDef browser


```supercollider
(
SynthDescLib.global.read;
SynthDescLib.global.browse;
)
```


shows 1 channel of output on channel 0.



## Getting audio from a bus
Send an .ar message to an In ugen to get data from an audio bus.


```supercollider
(
SynthDef("dataFromABus", {
    Out.ar(
        0,
        [    // the left channel gets input from an audio bus
            In.ar(0, 1),
            SinOsc.ar(440, 0.2)
        ]
    )
}).add;
)

(
Synth("dataForABus");    // synthesize a sawtooth wave on channel 0
Synth("dataFromABus");    // pair it with a sine wave on channel 1
)
```




## Control rate buses
Use `In.kr` and `Out.kr` to read from or write to control buses.

////////////////////////////////////////////////////////////////////////////////////////////////////

For additional information, see the [Out](../../Classes/Out.md), [In](../../Classes/In.md), and [Bus](../../Classes/Bus.md) files in the SuperCollider help system.

////////////////////////////////////////////////////////////////////////////////////////////////////

go to [Mark_Polishook_tutorial/10_Controls](../../Tutorials/Mark_Polishook_tutorial/10_Controls.md)



