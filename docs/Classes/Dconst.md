# Dconst

*Constrain a demand-rate stream to a given sum*

**Categories:** UGens>Demand

## Description

A demand-rate analog to [Pconst](../Classes/Pconst.md). It outputs values from the child demand stream until the sum of those values reaches or exceeds a given total. The last value will be truncated so that the sum of Dconst's output values will match the total exactly.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `sum` | The sum to reach. This may be a number, demand UGen or any other UGen. When a Dconst instance resets, one value will be taken for the sum, and it can't be modulated until the next reset. |  
| `in` | A demand-rate stream, providing the output values. |  
| `tolerance` | Because of floating point rounding error, it isn't safe to stop only when the output's running sum is equal to the desired total. `tolerance` is how close the running sum can get to stop the output: `abs(runningsum - sum) <= tolerance`. |  
**Returns:** A demand-rate stream.
## Examples


```supercollider
// fast notes of random duration for 0.5 seconds
// then a single note for 0.5 seconds
(
a = {
    var freq = Duty.kr(
        Dseq([
            Dconst(0.5, Dwhite(0.05, 0.08, inf)),
            0.5
        ], inf),
        0,
        // workaround for the lack of Dexprand
        Dwhite(0, 1, inf).linexp(0, 1, 200, 600)
    );
    VarSaw.ar(Lag.kr(freq, 0.02), 0, 0.3, 0.1).dup
}.play;
)

a.free;
```




