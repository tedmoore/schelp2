# NdefMixerOld

*mix control for all Ndefs on a given server*

**Categories:** JITLib>GUI

**Related:** [NdefMixer](../Classes/NdefMixer.md)

## Description

For more details see: [ProxyMixer](../Classes/ProxyMixer.md)


## Class Methods


### Creation

### `new`
Return a new window for a given server.
```
// ndef mxers for other servers
n = NdefMixer(\internal);
n = NdefMixer(\localhost);
n = NdefMixer(\trala);        // fails, no such server
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `server` | Server object ([Server](../Classes/Server.md)) or server name ([Symbol](../Classes/Symbol.md)) |  
| `nProxies` | an Integer. |  
| `title` | a String. |  
| `bounds` | a Rect. |  



## Instance Methods


### `proxyspace`
Return the proxyspace.
## Examples


```
n = NdefMixer(s);        // for the default server
// make a new proxy
(
Ndef(\a, {
    Pan2.ar(
        Ringz.ar(
            Impulse.ar(exprand(0.5, 4)),
            exprand(300, 3000),
            0.02
        ),
    1.0.rand2,
    0.2)
})
);



n.proxyspace;

Ndef(\duster, { Dust.kr(4) });

Ndef(\a).ar;
Ndef(\a).fadeTime = 2;
Ndef(\a).end;
```




