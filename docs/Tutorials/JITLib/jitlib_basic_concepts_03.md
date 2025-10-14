# jitlib_basic_concepts_03

*proxyspace - basic concepts*

**Categories:** JITLib>Tutorials, Tutorials>JITLib

**Related:** [Overviews/JITLib](../../Overviews/JITLib.md), [JITLib/jitlib_basic_concepts_02](../../Tutorials/JITLib/jitlib_basic_concepts_02.md), [JITLib/jitlib_basic_concepts_04](../../Tutorials/JITLib/jitlib_basic_concepts_04.md)

internal structure of the node proxy, node order and the parameter context
- [a) slots](#a)-nodeproxy-slots)
- [b) fadeTime](#b)-fade-time)
- [c) play/stop, send/release, pause/resume, clear](#c)-play/stop,-send/free,-pause/resume)
- [d) the parameter context](#d)-the-parameter-context)

A NodeProxy has two internal contexts in which the objects are inserted: The group, which is on the server, and the nodeMap, which is a client side parameter context. As the group can contain an order of synths, there is a client side representation, in which the source objects are stored (see [Order](../../Classes/Order.md)).

```supercollider
// make new space
p = ProxySpace.push(s.boot);
~z.play; ~y.ar; // explicitly initialize proxies
```


## a) NodeProxy slots
One node proxy can hold several objects in an execution order. The index can be any positive integer.


```supercollider
// the initial slot (0) is used when assigning directly.
// ~y is still unused, we will add it later.

~z = (~y * pi).sin * 0.1 * { LFSaw.kr(LFNoise1.kr(0.1 ! 3).sum * -18).max(0.2) };

// other slot numbers are accessed by positive integers:

~y[1] = { Saw.ar([400, 401.3], 0.4) };
~y[0] = { Saw.ar([300, 301], 0.4) };

// to remove one of them, nil is used:

~y[0] = nil;

// what is to be found at index 1?
~y.objects[1] // a playing interface
~y.objects[1].source.postcs // the function that was put in.
~y.objects.postcs     // this returns objects in the slots.
~y.source.postcs    // this returns the function in slot 0 only.
```


multiple assignment


```supercollider
// the function is assigned to the slots from 1 to 4
~z[1..4] = { SinOsc.ar(exprand(300, 600), 0, LFTri.kr({exprand(1, 3)} ! 3).sum.max(0)) * 0.1 };


// the function is assigned to the slots 1, 2 and 3 (subsequent)
~z[1..] = [ {SinOsc.ar(440) * 0.1 }, { SinOsc.ar(870) * 0.08 }, { SinOsc.ar(770) * 0.04 }];

// if no slot is given, all other slots are emptied
~z = { OnePole.ar(Saw.ar([400, 401.3], 0.3), 0.95) };

~z.end;
~y.end;
```




## b) fade time

```supercollider
// setting the fadeTime will allow cross fades.
// in case of an audio rate proxy the fade is pseudo-gaussian
// in case of a control rate proxy it is linear.

~z.play;

~z.fadeTime = 5.0; // 5 seconds
~z = { max(SinOsc.ar([300, 301]), Saw.ar([304, 304.3])) * 0.1 };
~z = { max(SinOsc.ar(ExpRand(300, 600)), Saw.ar([304, 304.3])) * 0.1 };

// the fadeTime can be set effectively at any time
~z.fadeTime = 0.2;
~z = { max(SinOsc.ar(ExpRand(3, 160)), Saw.ar([304, 304.3])) * 0.1 };
```



> **Note:** the fadeTime is also used for the operations xset and xmap. (see below)




## c) play/stop, send/free, pause/resume
there are a couple of messages a NodeProxy understands that are related to play, stop etc. Here is what they do.


### play/stop
this pair of messages is related to the monitoring function of the proxy. play starts monitoring, stop ends the monitoring. *if the proxy group is playing* (this can be tested with .isPlaying), play will not affect the proxie's internal behaviour in any way. Only if it is not playing (e.g because one has freed the group by cmd-period) it starts the synths/objects in the proxy. Stop never affects the internal state of the proxy.


```supercollider
// first hit cmd-period.
~z = { max(SinOsc.ar(ExpRand(3, 160)), Saw.ar([304, 304.3])) * 0.1 };
~z.play;        // monitor the proxy
~z.stop;        // note that now the proxy is still playing, but only in private
~z.isPlaying;        // is the group playing? yes.
~z.monitor.isPlaying;    // is the monitor playing? no.
```


You can pass a vol argument to play to adjust the monitor volume without affecting the proxy internal bus volume.


```supercollider
~z.play(vol:0.3);
// while playing you can set the volume also:
~z.vol = 0.8;
```





### send / release
this pair of messages controls the synths within the proxy. It does not affect the monitoring (see above). send starts a new synth, release releases the synth. **send** by default releases the last synth. if the synth frees itself (doneAction 2) **spawn** can be used.


```supercollider
// first hit cmd-period.
~z.play; // monitor. this starts also the synth, if the group wasn't playing.

~z = { SinOsc.ar(ExpRand(20, 660) ! 2) * Saw.ar(ExpRand(200, 960) ! 2) * 0.1 };

~z.release; // release the synth. the current fadeTime is used for fade out

~z.send; // send a new synth. the current fadeTime is used for fade in

~z.send; // send another synth, release the old

~z.release;

~z.stop;

~z.play; // monitor. as the group was still playing, this does _not_ start the proxy.
```


in order to free the synths and the group together, **free** is used:


```supercollider
~z.free; // this does also not affect the monitoring.
~z.play; // monitor. as the group was not playing, this starts the proxy.
```


in order to free the synths and the group, stop playback, **end** is used.


```supercollider
~z.end(3); // end in 3 sec
```


in order to rebuild the synthdef on the server, use **rebuild**. this is of course far less efficient than *send*, but it can make sense; e.g. the synthdef has random elements. UGens like Rand(300, 400) create new random values on every send, while client-side random functions like exprand(1, 1.3) only get built once; to force new decisions with these, one can use **rebuild**.


```supercollider
(
~z = {
    Splay.ar(
        SinOsc.ar(Rand(300,400) + ({exprand(1, 1.3)} ! rrand(1, 9)))
        * LFCub.ar({exprand(30, 900)} ! rrand(1, 9))
        * LFSaw.kr({exprand(1.0, 8.0)} ! rrand(1, 9)).max(0)
        * 0.1
    )
};
)

~z.play;
~z.rebuild;
~z.send;    // send just creates a new synth - new freq, all else remains the same
~z.rebuild;    // rebuild the synthdef, re-decide numbers of oscs
~z.end;
```





### pause / resume
when paused, a node proxy still stays active, but every synth that is started is paused until the proxy is resumed again.


```supercollider
~z.play;

~z.pause; // pause the synth.

~z = { SinOsc.ar({ExpRand(300, 660)} ! 2) * 0.1 };    // you can add a new function,
                            // which is paused.

~z.resume; // resume playing.
```


Note that pause/resume causes clicks with audio rate proxies, which do not happen when pauseing control rate proxies.




### clear
clear removes all synths, the group, the monitor and releases the bus number.


```supercollider
~z.clear;
~z.bus;        // no bus
~z.isNeutral;    // not initialized.
```


note that when other processes use the nodeproxy these are not notified. So clearing has to be done with regard to this.





## d) The parameter context
what happens to function arguments?


```supercollider
~y.play;
~y = { arg freq=500; SinOsc.ar(freq * [1, 1.1]) * 0.1 };
```


now the argument 'freq' is a control in the synth (just like in SynthDef) which you can change by the **'set'** message.


```supercollider
~y.set(\freq, 440);

// unlike in synths, this context is kept and applied to every new synth:

~y = { arg freq=500; Formant.ar(50, freq * [1, 1.1], 70) * 0.1 };
```


the message **xset** is a variant of set, to crossfade the change using the current fadeTime:


```supercollider
~y.fadeTime = 3;
~y.xset(\freq, 600);

// the same context is applied to all slots:

~y[2] = { arg freq=500; SinOsc.ar(freq * [1, 1.1]) * LFPulse.kr(Rand(1, 3)) * 0.1 };
~y.xset(\freq, 300);
```


the parameter context also can keep bus mappings. a control can be mapped to any *control proxy* :


```supercollider
~c = { MouseX.kr(300, 800, 1) };
~y.map(\freq, ~c);

// also here the context is kept:

~y = { arg freq=500; Formant.ar(4, freq * [1, 1.1], 70) * 0.1 };
```


the message **xmap** is a variant of map, to crossfade the change using the current fadeTime:


```supercollider
~y.set(\freq, 440);
~y.xmap(\freq, ~c);
```


to remove a setting or a mapping, use unmap / unset.


```supercollider
~y.unmap;
```


also multichannel controls can be mapped to a multichannel proxy using **map** :


```supercollider
~c2 = { [MouseX.kr(300, 800, 1), MouseY.kr(300, 800, 1)] };
~y = { arg freq=#[440, 550]; SinOsc.ar(freq) * SinOsc.ar(freq + 3) * 0.05 };
~y.map(\freq, ~c2);
```


the parameter context can be examined:


```supercollider
~y.nodeMap;

// apart from the parameters explicitly set,
// it contains the bus index and the fadeTime

// for more information, see NodeMap


p.clear(8); // clear the whole proxy space, in 8 secs.
```


previous: [JITLib/jitlib_basic_concepts_02](../../Tutorials/JITLib/jitlib_basic_concepts_02.md) next: [JITLib/jitlib_basic_concepts_04](../../Tutorials/JITLib/jitlib_basic_concepts_04.md)



