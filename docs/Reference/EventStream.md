# Event Stream

**Categories:** Streams-Patterns-Events

**Related:** [Stream](../Classes/Stream.md), [Event](../Classes/Event.md)

*A Stream that returns Events when called*

An event stream is a normal [Stream](../Classes/Stream.md) that returns events when called. (see class [Event](../Classes/Event.md)). Usually, an event stream requires an event to be passed in, often the default event is used:

```
t = Pbind(\x, Pseq([1, 2, 3])).asStream; // Pbind, e.g. creates a stream
t.next(Event.default);
t.next(Event.default);
```

An event stream cannot be played directly with a clock, as it returns events and not time values. Therefore, an [EventStreamPlayer](../Classes/EventStreamPlayer.md) is used, which replaces the event by according time value.
A [Pevent](../Classes/Pevent.md) can be used to wrap a stream in an event:

```
t = Pevent(Pbind(\x, Pseq([1,2,3])), Event.default).asStream;
t.next;
t.next;
```



