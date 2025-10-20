# softVol_

*set a nodeproxy's vol conditionally*

**Categories:** JITLib>GUI

**Related:** [softSet](../Reference/softSet.md), [softPut](../Reference/softPut.md)

## Description

Extension method to [NodeProxy](../Classes/NodeProxy.md) to set vol conditionally.

### `softVol`
setter.**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | the volume value to set to |  
| `within` | the normalized range within which the set is accepted |  
| `pause` | a flag whether to pause the nodeproxy when volume is 0. waits for 0.2 seconds for volume to go down first. |  
| `lastVal` | the previous value that the controller has set - can be |  
| `spec` | a [ControlSpec](../Classes/ControlSpec.md) can be passed in. if nil, `\amp.asSpec` is used. |  


## Examples


```
Ndef(\test, { |freq=200| Splay.ar(SinOsc.ar(freq * Array.rand(12, 0.95, 1.05))) });
Ndef(\test).play(vol: 0.1);

    // example of softSet, softSet which knows lastVal,
    // softVol_ and softVol_ which knows lastVol:
(
w = Window("softVol", Rect(500, 200, 400, 240)).front;
w.view.addFlowLayout;
NdefGui(Ndef(\test), 2, w);

    // same for volume - not too safe
EZSlider(w, 340@30, \softVol, \amp, { |sl|
    Ndef(\test).softVol_(sl.value, 0.05)
});
    // safer
EZSlider(w, 340@30, \knowLastV, \amp, Routine { |sl|
    var newVal, lastVal;
    loop {
        newVal = sl.value;
        Ndef(\test).softVol_(sl.value, 0.05, lastVal: lastVal);
        lastVal = newVal;
        \dummy.yield;
    }
});
)
```




