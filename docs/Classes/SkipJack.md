# SkipJack

*A utility for background tasks that survive cmd-period*

**Categories:** Scheduling, JITLib>GUI

**Related:** [CmdPeriod](../Classes/CmdPeriod.md)

## Description

SkipJack is a utility to run a function in the background repeatedly, that survive cmd-period.
A typical use is with a window displaying the state of some objects every now and then. (This is better in some cases than updating the GUI at every change. If the changes happen fast, you don't choke your CPU on gui updating.)
But SkipJack is useful whenever you need a periodic function to run in the background and not go away if the user hits cmd-period.


## Class Methods



### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `updateFunc` | A [Function](../Classes/Function.md) to repeat in the background. |  
| `dt` | The time interval at which to repeat. It can also be a stream or a function that returns a number. |  
| `stopTest` | A test whether to stop the task now. Usually a Function. |  
| `name` | A name for this skipjack. Used for posting information and in the [#*stop](#*stop) classmethod. |  
| `clock` | The clock that plays the task. Default is [AppClock](../Classes/AppClock.md), so SkipJack can call GUI primitives. If you need more precise timing, you can supply your own clock, and use defer only where necessary. |  
| `autostart` | When true (default) SkipJack starts automatically as it is created. |  


### `stop`
Stop a skipjack by name.

### `stopAll`
Stop all skipjacks.

### `defaultClock`
The default clock (AppClock)

### `verbose`
When true, SkipJack posts messages when it starts, stops or restarts.

### `all`
The global set of all skipjacks.

## Instance Methods


### `dt`
Get or set the time interval.
### `task`
The internal Routine that wraps updateFunc.
### `name`
The name of this skipjack.
### `stopTest`
The current stopTest. (see argument in [#*new](#*new))
### `start`
Start this skipjack.
### `play`
Same as `start`
### `stop`
Stop this skipjack.
### `clock`
Get or set the clock used. This will only be updated when the skipjack restarts.
### `updateFunc`
The updateFunc set by the argument to [#*new](#*new)
## Examples

Simple example:

```
w = SkipJack({ "watch...".postln }, 0.5, name: "test");
SkipJack.verbose = true;    // post stop/wakeup logs

w.stop;
w.start;

//     now try to stop with cmd-. : SkipJack always restarts itself.
thisProcess.stop;

w.stop;
```


Using stopTest:

```
a = 5;
w = SkipJack({ "watch...".postln }, 0.5, { a == 10 }, "test");
a = 10;    // fulfill stopTest
```


Typical use: SkipJack updates a window displaying the state of some objects every now and then.

```
(
d = (a: 12, b: 24);
d.win = Window("dict", Rect(0, 0, 200, 60)).front;
d.views = [\a, \b].collect { |name, i|
    StaticText(d.win, Rect(i * 100, 0, 96, 20))
        .background_(Color.yellow).align_(0).string_(name);
};
w = SkipJack({
        "...".postln;
        [\a, \b].do { |name, i|
            d.views[i].string_(name ++ ":" + d[name])
        }
    },
    0.5,
    { d.win.isClosed },
    "showdict"
);
)

d.a = 123;      // updates should be displayed
d.b = \otto;
d.win.close;    // when window closes, SkipJack stops.
```


If you need to get rid of an unreachable skipjack:

```
SkipJack({ "unreachable, unkillable...".postln }, name: "jack");

SkipJack.stopAll        // do this to stop all;

SkipJack.stop("jack");  // reach it by name and stop
```




