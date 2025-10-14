# EventStreamCleanup

*Helper class that collects information about internal state of streams that needs to be released*

**Categories:** Streams-Patterns-Events

## Description

Event streams created by objects like [Pmono](../Classes/Pmono.md) or [Pfx](../Classes/Pfx.md) are special: when they start, they create some state (like a new synth) that is present over the whole period of the stream, or at least over several events. When such a stream ends, it releases this state. There are other streams, however, **that may stop their input stream at any time** (e.g. [Pfindur](../Classes/Pfindur.md) or [Pdef](../Classes/Pdef.md)). Them the state of any stream buried in the hierarchy of input streams must be released by them. EventStreamCleanup collects the cleanup functions and can run them when the stream is cut.

> **Note:** So all event patterns that can end a subpattern (and streams respectively) have to use an EventStreamCleanup.


Some examples of patterns that may stop an input stream and update an EventStreamCleanup:
- [Pbindf](../Classes/Pbindf.md) (stops its event stream if one of its parameter streams ends)
- [Pfin](../Classes/Pfin.md) (stops stream after a number of events)
- [Pfindur](../Classes/Pfindur.md) (stops stream after a certain elapsed time)
- [Pdef](../Classes/Pdef.md) (stops stream when replaced by a new one)
- [Pset](../Classes/Pset.md) (stops its event stream when its parameter streams ends)
- [Pswitch1](../Classes/Pswitch1.md) (stops all input streams after fixed number of items or when one of them ends. Not [Pswitch](../Classes/Pswitch.md), which completely embeds every input stream)

Some examples of patterns that create state that lasts over several events. They also release the state via EventStreamCleanup:
- [Pmono](../Classes/Pmono.md) (starts one synth that it controls over time)
- [Pfx](../Classes/Pfx.md) (starts an effect synth that it feeds through the signals of the substreams)
- [Pproto](../Classes/Pproto.md) (initializes resources and keeps them available)
- [Pspawner](../Classes/Pspawner.md) (schedules streams and releases them after some time)


```supercollider
// wrap a pattern in a stop condition
(
f = { |pat, condition|
    Prout { |inval|
        var stream = pat.asStream;
        var cleanup = EventStreamCleanup.new;
        var outval;
        while {
            outval = stream.next(inval);
            outval.notNil and: { condition.value(outval) }
        } {
            cleanup.update(outval);
            inval = outval.yield;
        };
        cleanup.exit(inval);
    }

};
p = Plazy { Pmono(\default, \note, Pgeom(rrand(1, 1.5), rrand(1.05, 2), inf), \harmonic, [0.78, 1, 1.2], \dur, 1/rrand(4, 7), \amp, 0.4) };
x = f.(p, { |outval| outval[\note] < 20 }); // always stop at 20
Pn(x).play; // loop it.
);
```




## Class Methods

### `new`
Create a new instance.

## Instance Methods

### `addFunction`
Add a new cleanup function which will be called when the stream is made to end somewhere downstreams. This is called only in patterns that create resources that need to be released (e.g. [Pmono](../Classes/Pmono.md) or [Pfx](../Classes/Pfx.md)).**Arguments:**

| Argument | Description |
|----------|-------------|
| `event` | The outevent that is passed on downstreams and which communicates to any stream-ending pattern what needs to be done to release the resources. **It must be yielded after update!** |  
| `function` | The function that is called for cleanup. E.g. `{ group.free }`. |  
**Returns:** a [CallOnce](../Classes/CallOnce.md) that executes the cleanup `function` at most once. Should it be necessary to execute the cleanup outside of the control of `EventStreamCleanup`, the CallOnce returned should be used instead of the original `function`, so that other referents are informed of the execution of the cleanup.### `update`
For every new event, the cleanup must be updated to receive information from any input stream further up. This method is called from all streams that may stop early (e.g. [Pmono](../Classes/Pmono.md) or [Pfindur](../Classes/Pfindur.md)).**Arguments:**

| Argument | Description |
|----------|-------------|
| `event` | The outevent from the input stream. **It must be yielded after update!** |  
### `exit`
Run all functions that have been collected over time, adding appropriate information to the event, in case it is passed on as an inevent.**Arguments:**

| Argument | Description |
|----------|-------------|
| `event` | The inevent that is passed through to the outer stream |  
| `freeNodes` | Used internally. |  
**Returns:** An event. In embedInStream, this event must be returned (`^cleanup.exit(inevent)`)### `functions`
A collections of cleanup functions.### `clear`
Empty the cleanup functions, without evaluating them.### `terminate`
Run all functions that have been collected over time without adding information to an event.**Arguments:**

| Argument | Description |
|----------|-------------|
| `freeNodes` | Used internally. |  

## Examples


```supercollider
// some code from the class library

// here is a pattern that can end the stream externally after a number of steps
Pfin : FilterPattern {
    var <>count;
    *new { |count, pattern|
        ^super.new(pattern).count_(count)
    }
    storeArgs { ^[count, pattern] }

    embedInStream { |event|
        var inevent;
        var stream = pattern.asStream;
        var cleanup = EventStreamCleanup.new;
        count.value(event).do({
            inevent = stream.next(event) ?? { ^event };
            cleanup.update(inevent);
            event = inevent.yield;
        });
        ^cleanup.exit(event)
    }
}

// and here is a pattern that adds a resource: a bus in which the events play

Pbus : FilterPattern {
    var <>numChannels, <>rate, <>dur = 2.0, <>fadeTime;

    *new { |pattern, dur = 2.0, fadeTime = 0.02, numChannels = 2, rate = \audio|
        ^super.new(pattern).dur_(dur).numChannels_(numChannels).rate_(rate).fadeTime_(fadeTime)
    }

    storeArgs { ^[pattern, dur, fadeTime, numChannels, rate] }

    embedInStream { |inevent|
        var server, groupID, linkID, bus, ingroup, cleanup;
        var patterns, event, freeBus, stream, cleanupEvent;

        cleanup = EventStreamCleanup.new;
        server = inevent[\server] ?? { Server.default };
        groupID = server.nextNodeID;
        linkID = server.nextNodeID;
        ingroup = inevent[\group];

        // could use a special event type for this:
        if(rate == \audio) {
            bus = server.audioBusAllocator.alloc(numChannels);
            freeBus = { server.audioBusAllocator.free(bus) };
        } {
            bus = server.controlBusAllocator.alloc(numChannels);
            freeBus = { server.controlBusAllocator.free(bus) };
        };

        CmdPeriod.doOnce(freeBus);

        event = inevent.copy;
        event[\addAction] = 0; // \addToHead
        event[\type] = \group;
        event[\delta] = 0;
        event[\id] = groupID;
        event[\group] = ingroup;
        event.yield;

        inevent = event = inevent.copy;

        event[\type] = \on;
        event[\group] = groupID;
        event[\addAction] = 3; // \addBefore
        event[\delta] = 0;
        event[\id] = linkID;
        event[\fadeTime] = fadeTime;
        event[\instrument] = format("system_link_%_%", rate, numChannels);
        event[\in] = bus;
        event[\msgFunc] = #{ |out, in, fadeTime, gate = 1|
            [\out, out, \in, in, \fadeTime, fadeTime, \gate, gate, \doneAction, 3]
        };

        cleanupEvent = (type: \off, parent: event, fadeTime: fadeTime.abs, hasGate: true, gate: 0);

        cleanup.addFunction(event, { |flag|
            if(flag) { defer ({ cleanupEvent.play }, dur) };
        });

        cleanup.addFunction(event, { defer({ freeBus.value }, fadeTime.abs + dur) });

        // doneAction = 3;
        // remove and deallocate both this synth and the preceding node
        // (which is the group).
        inevent = event.yield;

        // now embed the pattern
        stream = Pchain(pattern, (group: groupID, out: bus)).asStream;
        loop {
            event = stream.next(inevent) ?? { ^cleanup.exit(inevent) };
            cleanup.update(event);
            inevent = event.yield;
        }
    }
}
```




