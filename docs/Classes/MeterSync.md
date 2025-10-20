# MeterSync

*Synchronize barlines of SuperCollider LinkClock peers*

**Categories:** Scheduling>Clocks

**Related:** [LinkClock](../Classes/LinkClock.md)

## Description

This class implements additional network messaging, beyond the Ableton Link protocol, to ensure that SuperCollider [LinkClock](../Classes/LinkClock.md) peers follow the same meter (beatsPerBar) and barlines as other LinkClock peers.
This class, or the associated methods [LinkClock#-enableMeterSync](../Classes/LinkClock.md#-enablemetersync) and [LinkClock#-disableMeterSync](../Classes/LinkClock.md#-disablemetersync), should be used for performances where all linked machines should follow the same meter *and* the meter will change during the performance.
If the meter will not change (typical use case being 4/4 time throughout), then it is necessary only to set `myLinkClock.quantum = beatsPerBar` on all peers. (See [LinkClock#-quantum](../Classes/LinkClock.md#-quantum).)
In theory, MeterSync may be used with any SuperCollider clock that answers the methods `beatsPerBar`, `beatInBar` and `baseBarBeats`. It is currently tested only with [LinkClock](../Classes/LinkClock.md). It is not meaningful to use with [TempoClock](../Classes/TempoClock.md), because TempoClock does nothing to synchronize its beats with any other machines.

> **Note:** This class considers only the barline positions of SuperCollider LinkClock peers! Other Link-capable applications do not implement this protocol.



### Background
SuperCollider defines *meter* using two numbers:


**[TempoClock#-beatsPerBar](../Classes/TempoClock.md#-beatsperbar)**
: How many beats comprise one bar (4 = 4/4 time, 3 = 3/4 time).

**[TempoClock#-baseBarBeat](../Classes/TempoClock.md#-basebarbeat)**
: The beat value at which the meter last changed.



For example, if a clock runs four bars of 4/4 time, and then switches to 3/4 time, the barlines are *not* multiples of 3. The meter changed at beat 16, so the new barlines will be `16 + (3 * n)` (`n` is an integer). At this point, then, beatsPerBar = 3 and baseBarBeat = 16.

Ableton Link maintains a *quantum*, which is analogous to [TempoClock#-beatsPerBar](../Classes/TempoClock.md#-beatsperbar). If all peers are following the same meter and have the same quantum, then Link itself will synchronize the barlines. (Thus, in the normal use case of a consistent meter throughout, it is not necessary to use `MeterSync` at all.)

However, when changing the Link quantum, Link does not guarantee that beat values will increment consistently. Setting the quantum is meant to be done before the performance begins, not during.

SuperCollider can change its `beatsPerBar` independently of the Link quantum. But, in that case, barlines across peers may not be synchronized.

`MeterSync` resolves this by querying other SuperCollider Link peers for their current metrical position. If the local machine differs from the other peers, then the local machine adjusts its `baseBarBeat` to be in metrical sync with the others. (Beats proceed as normal; only the barline position is adjusted.)




## Class Methods


### `new`
Returns a new instance, associated with a specific clock object.**Arguments:**

| Argument | Description |
|----------|-------------|
| `clock` | The clock which this instance controls. |  
| `id` | Optional. An integer, uniquely identifying this instance. If not provided, a random integer will be chosen. |  
| `ports` | Optional. An array of port numbers to which sync messages will be sent. (sclang instances normally use port 57120, but if that port is in use, they will try 57121 and so on, successively. The default here is to try all of 57120-57127.) |  


## Instance Methods


### `free`
Release this instance, disabling metric sync for the associated clock.
### `resyncMeter`
Adjust the clock's barline position to match other SuperCollider peers on the network.**Arguments:**

| Argument | Description |
|----------|-------------|
| `round` | Optional. Force a specific subdivision: round = 1 assumes quarter-notes as the metric base; round = 0.5 assumes eighth-notes (e.g. 5/8 time). If not provided, it will be calculated based on the incoming beatsPerBar values from other peers. |  
| `verbose` | Boolean. If false, suppress information messages. |  
**Returns:** The instance.
### `queryMeter`
Query metrical information from other peers, and collect the results. Normally, you should not need to call this method. It is provided in case you want to verify sync, or implement a custom behavior.**Arguments:**

| Argument | Description |
|----------|-------------|
| `action` | A function to evaluate, after the results have been obtained. Results are passed to this function as an argument: a List of Events containing:- id: The remote peer's ID (integer).
- beats: The remote clock's beats, at the time of answering.
- beatsPerBar: The remote clock's meter.
- baseBarBeat: The remote clock's metrical base.
- beatInBar: The remote clock's metrical position within the bar.
- queriedAtBeat: The *querying* clock's query time, in beats.
- syncMeter: Boolean. If true, the remote clock is syncing barlines. If false, the remote clock has an answering MeterSync object, but it is disabled. |  
| `timeout` | Float. A number of seconds to wait for replies. (It will always wait for the entire timeout period. LinkClock knows its [LinkClock#-numPeers](../Classes/LinkClock.md#-numpeers), but only SuperCollider peers will answer queries, and there is no way to know how many of the peers are SuperCollider.) |  
**Returns:** The instance. Replies are asynchronous; use the `action` function to respond.
### `id`
Get the integer ID uniquely identifying this instance. The ID is set at initialization time ([LinkClock#-enableMeterSync](../Classes/LinkClock.md#-enablemetersync) or [#*new](#*new)). To change it, free the current instance and create a new one.
### `ports`
Get the array of ports to which sync messages will be sent. The ports are set at initialization time ([LinkClock#-enableMeterSync](../Classes/LinkClock.md#-enablemetersync) or [#*new](#*new)). To change them, free the current instance and create a new one.**Returns:** An array of integer port numbers.
### `adjustMeterBase`
A convenience method to adjust the clock's baseBarBeat, given the local metrical position and the remote metrical position. Normally, you do not need to call this method. It is provided in case you do your own analysis of [MeterSync#-queryMeter](../Classes/MeterSync.md#-querymeter) results and you want to adjust barlines in your own way.**Arguments:**

| Argument | Description |
|----------|-------------|
| `localBeats` | The local clock's beats. Usually this should be derived from `result[index][\queriedAtBeat]` (where `result` comes from [MeterSync#-queryMeter](../Classes/MeterSync.md#-querymeter)). Strongly recommended to use this instead of `clock.beats`, because the query time does not add the timeout. |  
| `remoteBeats` | The local clock's beats. Usually this should be derived from `result[index][\beats]`. |  
| `round` | Optional. Force a specific subdivision: round = 1 (the default) assumes quarter-notes as the metric base; round = 0.5 assumes eighth-notes (e.g. 5/8 time). |  
**Returns:** The instance.
```
// You *may* do something like this optionally,
// if something went wrong.
// Normally you should just call 'resyncMeter'
// and it's all done for you.

l = LinkClock.new.latency_(s.latency);
m = MeterSync(l);

(
m.queryMeter({ |result|
    result.postln;
    m.adjustMeterBase(result[0][\queriedAtBeat], result[0][\beatInBar]);
});
)

l.stop;  // cleans up 'm' automatically
```


### `enabled`
Enable or disable meter sync. If disabled, this instance will no longer respond to meter changes from peers. It will still answer queryMeter, with `'syncMeter': false` in the reply (so you can filter the queryMeter results accordingly).**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | True = enabled, false = disabled. |  
**Returns:** Boolean.
### `clock`
Answers with the clock being controlled by this instance.
> **Note:** You cannot change the associated clock object. You should instead [MeterSync#-free](../Classes/MeterSync.md#-free) this instance, and create a new instance for the other clock.


### `repeats`
Get or set the number of repeats for OSC messaging.UDP does not detect failure to deliver messages; therefore, messages may be lost. If that happens, LinkClock peers may fail to synchronize properly and [#-resyncMeter](#-resyncmeter) may be unable to recover. To prevent this, sync messages are sent 'repeats' times. The default is 4.
### `delta`
Get or set the number of seconds between OSC messaging repeats.
## Examples


```
l = LinkClock.new.latency_(s.latency).enableMeterSync;

// If meter gets off, try to resync:
l.getMeterSync.resyncMeter;

// What are other clocks' timebases?
l.getMeterSync.queryMeter({ |result|
    result.do { |row| row.postln };
});

// I want a different ID and/or ports: free, then recreate
l.disableMeterSync;
l.enableMeterSync(1000, (57120..57135));
```




