# Filter

*Base class for filter UGens*

**Categories:** UGens>Filters

## Description

"Filter" is an abstract class - in other words, a class that you do not use directly. Instead, use one of its subclasses. Many common filters inherit from this abstract class, including LPF, HPF, MoogFF, Ringz, Integrator, Median, LeakDC... and many more.
The Filter class also provides a simple way to visualise the frequency-wise effect of applying a filter, see `scopeResponse` below.


## Class Methods



### `scopeResponse`
Provides a simple way to visualise the frequency-wise effect of applying a filter
```
s.boot // boot the server 
MoogFF.scopeResponse
HPF.scopeResponse
BRF.scopeResponse
Median.scopeResponse
```



## Instance Methods



