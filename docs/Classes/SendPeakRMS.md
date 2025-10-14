# SendPeakRMS

*Track peak and power of a signal for GUI applications.*

**Related:** [Peak](../Classes/Peak.md), [PeakFollower](../Classes/PeakFollower.md), [OSCFunc](../Classes/OSCFunc.md)

**Categories:** UGens>Analysis>Amplitude

## Description

The SendPeakRMS unit generator computes peak and power of a signal and sends the computed values back to the clients. It does not produce any output.


## Class Methods


### `ar`, `kr`
Unlike with other unit generators, the `ar` and `kr` methods do not specify the rate of the computation, but the granularity. When the SendPeakRMS ugen is instantiated with `kr`, the reply rate is quantized to control-rate blocks.**Arguments:**

| Argument | Description |
|----------|-------------|
| `sig` | The input signal. |  
| `replyRate` | Float or Integer. Specifies the number of replies that are sent to the clients per second. |  
| `peakLag` | Float or Integer. Lag time, which is applied to the peak values. This option is commonly used for GUI VU meters. |  
| `cmdName` | Symbol or String. Address pattern for reply message. |  
| `replyID` | Integer ID (similar to [SendTrig](../Classes/SendTrig.md)). |  


## Instance Methods


## Examples


```supercollider
(
{
    SendPeakRMS.kr(Dust.ar(20), 20, 3, "/replyAddress")
}.play;
)

(
o = OSCFunc({ |msg|
    "peak: %, rms: %".format(msg[3], msg[4]).postln
}, '/replyAddress');
)
o.free;
```




