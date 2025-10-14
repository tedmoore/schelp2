# Routine

**Categories:** Core>Kernel

*Functions that can return in the middle and then resume where they left off*

**Related:** [Stream](../Classes/Stream.md)

## Description

A Routine runs a [Function](../Classes/Function.md) and allows it to be suspended in the middle and be resumed again where it left off. This functionality is supported by the Routine's superclass [Thread](../Classes/Thread.md). Effectively, Routines can be used to implement co-routines as found in Scheme and some other languages.
A Routine is **started** the first time [#-next](#-next) is called, which will run the Function from the beginning. It is **suspended** when it "yields" (using [Object#-yield](../Classes/Object.md#-yield) within the Function), and then **resumed** using [#-next](#-next) again. When the Function returns, the Routine is considered **stopped**, and calling [#-next](#-next) will have no effect - unless the Routine is **reset** using [#-reset](#-reset), which will rewind the Function to the beginning. You can stop a Routine before its Function returns using [#-stop](#-stop).
When a Routine is **scheduled** on a [Clock](../Classes/Clock.md) (e.g. using [#-play](#-play)), it will be started or resumed at the scheduled time. The value yielded by the Routine will be used as the time difference for rescheduling the Routine. (See [#-awake](#-awake)).
Since Routine inherits from [Thread](../Classes/Thread.md), it has its own associated [logical time](../Classes/Thread.md#-beats), etc. When a Routine is started or resumed, it becomes the [current thread](../Classes/Thread.md#.thisthread).
Routine also inherits from [Stream](../Classes/Stream.md), and thus shares its ability to be combined using math operations and "filtered".


## Class Methods

### `new`
Creates an instance of Routine, passing it the Function with code to run.**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A Function with code for the Thread to run. |  
| `stackSize` | Call stack size (an Integer). |  

```supercollider
a = Routine.new({ 1.yield; 2.yield });
a.next.postln;
a.next.postln;
a.next.postln;
```

The Function class provides its own shortcut method `r` that calls `Routine.new`, thus one can also write:
```supercollider
a = r { 1.yield; 2.yield };
```



## Instance Methods

### `next`
This method performs differently according to the Routine's state:- Starts the Routine, if it has not been started yet or it has been [reset](#-reset); i.e runs its Function from the beginning, passing on the `inval` argument.
- Resumes the Routine, if it has been suspended (it has yielded); i.e. resumes its Function from the point where [yield](../Classes/Object.md#-yield) was called on an Object, passing the `inval` argument as the return value of `yield`.
- Does nothing if the Routine has stopped (because its Function has returned, or [#-stop](#-stop) has been called).
`thisThread` : Since Routine inherits from [Thread](../Classes/Thread.md), it will become the *current thread* when it is started or resumed; i.e. [thisThread](../Classes/Thread.md#.thisthread) used in the Routine Function will return the Routine.Time: Just before `next` is called, `thisThread` points either to another Routine, or the top-level Thread. During the `next` call, this becomes the parent thread (see [Thread#-parent](../Classes/Thread.md#-parent)). `next` then evaluates on the parent's clock, at the parent's logical time.Synonyms for `next` are [#-value](#-value) and [#-resume](#-resume).**Returns:** - Either the value that the Routine yields (the Object on which [yield](../Classes/Object.md#-yield) is called within the Routine Function),
- ...or `nil`, if the Routine has stopped.
When a Routine is started by a call to this method (or one of its synonyms), the method's argument is passed on as the argument to the Routine Function:
```supercollider
Routine { |inval|
    inval.postln;
}.value("hello routine");
```

After the Routine has yielded (it has been suspended at the point in its Function where `yield` is called on an Object), a call to this method (or its synonyms) resumes executing the Function and the argument to this method becomes the return value of `yield`. To access that value within the Function, you have to assign it to a variable - typically, the argument of the Function is reused:
```supercollider
(
r = Routine { |inval|
    inval.postln;
    inval = 123.yield;
    inval.postln;
}
)

r.value("hello routine");
r.value("goodbye routine");
```

Typically, a Routine yields multiple times, and each time the result of the yield is reassigning to the argument of its Function.
```supercollider
(
r = Routine { |inval|
    inval.postln; // Post the value passed in when started.
    5.do { |i|
        inval = (i + 10).yield;
        inval.postln; // Post the value passed in when resumed.
    }
}
)
(
5.do {
    r.value("hello routine").postln; // Post the value that the Routine yields.
}
)
```

### `value`
Equivalent to [#-next](#-next).### `resume`
Equivalent to [#-next](#-next).### `stop`
Equivalent to the Routine Function reaching its end or returning: after this, the Routine will never run again (the [#-next](#-next) method has no effect and returns `nil`), unless [#-reset](#-reset) is called.### `reset`
Causes the Routine to start from the beginning next time [#-next](#-next) is called.If a Routine is stopped (its Function has returned or [#-stop](#-stop) has been called), it will never run again (the [#-next](#-next) method has no effect and returns `nil`), unless this method is called.A Routine cannot reset itself, except by calling [Object#-yieldAndReset](../Classes/Object.md#-yieldandreset).See also: [Object#-yield](../Classes/Object.md#-yield), [Object#-alwaysYield](../Classes/Object.md#-alwaysyield)### `play`
Schedules the Routine on the given [Clock](../Classes/Clock.md), at a time specified by `quant`. At that time, the Routine will wake up (by calling [Routine#-awake](../Classes/Routine.md#-awake)), setting the clock and time and evaluating the Routine. If the Routine yields a number, this number of beats will be added to the current time and the Routine will be rescheduled. (This behavior is compatible with scheduling a [Stream](../Classes/Stream.md) or a [Function](../Classes/Function.md).)**Arguments:**

| Argument | Description |
|----------|-------------|
| `clock` | a Clock, TempoClock by default |  
| `quant` | see the [Quant](../Classes/Quant.md) helpfile |  
using [Object#-idle](../Classes/Object.md#-idle) within a routine, return values until this time is over. Time is measured relative to the thread's clock.
```supercollider
// for 6 seconds, return 200, then continue
(
r = Routine {
        199.yield;
        189.yield;
        200.idle(6);
        199.yield;
        189.yield;
};

fork {
    loop {
        r.value.postln;
        1.wait;
    }
}
);

// the value can also be a stream or a function
(
r = Routine {
        199.yield;
        189.yield;
        Routine { 100.do { |i| i.yield } }.idle(6);
        199.yield;
        189.yield;
};

fork {
    loop {
        r.value.postln;
        1.wait;
    }
}
);
```

### `reschedule`
If a Routine is currently scheduled on a clock, it will be expected to "awake" at a specific time, on a specific clock. `reschedule` allows you to change to a different clock or to a later time.**Arguments:**

| Argument | Description |
|----------|-------------|
| `argClock` | The new clock on which to run the Routine. If `nil`, the routine's clock will not be changed. (Note: Currently incompatible with [AppClock](../Classes/AppClock.md); rescheduling depends upon the method `schedAbs`, which AppClock does not implement.) |  
| `quant` | A quantization specifier, identifying a time *later* than the next-scheduled time. If `nil`, the current value of `nextBeat` will be used. |  
- Rescheduling to a different clock will be continuous in terms of seconds, but not necessarily continuous in terms of beats. Time-based patterns such as [Pseg](../Classes/Pseg.md), or the use of [Env](../Classes/Env.md) as a stream, may not follow the envelope shape continuously. (Pseg and Env-as-stream measure time in beats on the clock that is playing. In normal use, the clock never changes, so time advances monotonically through the envelope's breakpoints. If a thread is rescheduled to a different clock, the beats values are very unlikely to be the same on the new clock. So the envelope would jump forward or backward in time.)When switching the clock, `reschedule` will first calculate the new "awake" time, in beats, based on the given `quant`. Then it converts that `beats` value into the new clock's `beats` for the same instant in time. If the old clock's tempo is 1 and the Routine is waiting for 1 beat, the next "awake" should happen after one second. When rescheduling without a `quant`, the next "awake" will *still* happen after one second -- but the `beats` value will adjust for the new clock.
- Currently `quant` will resolve to a time *later* than the Routine's current `nextBeat`. If you try to force it earlier, there is likely to be some discontinuity. This is because the Routine cannot reschedule until it wakes up normally. The workaround is to switch the Routine into a different [Task](../Classes/Task.md) wrapper.
- Currently the routine must be playing (already scheduled on a clock). This is because the handoff to the new clock or time occurs during the thread's "awake" process. If the routine is not playing, then it will not awake, and nothing will happen.

```supercollider
// Rescheduling to a different clock, same time
c = TempoClock.new;

(
t = Routine {
    var lastSeconds = thisThread.seconds;
    loop {
        1.0.wait;
        [thisThread.beats, thisThread.seconds - lastSeconds].postln;
        lastSeconds = thisThread.seconds;
    }
}.play;
)

t.reschedule(c);  // seconds delta = 1.0 throughout

t.stop;

// Rescheduling to a later time, same clock
(
t = Routine {
    var lastSeconds = thisThread.seconds;
    loop {
        1.0.wait;
        [thisThread.beats, thisThread.seconds - lastSeconds].postln;
        lastSeconds = thisThread.seconds;
    }
}.play;
)

t.reschedule(quant: 1);

t.stop;

// Rescheduling to an earlier time (workaround, only possible way)
// Requires you to start with a PauseStream!
// This does not work if 't' is a Routine initially.
(
t = PauseStream(Routine {
    var lastSeconds = thisThread.seconds;
    loop {
        1.0.wait;
        [thisThread.beats, thisThread.seconds - lastSeconds].postln;
        lastSeconds = thisThread.seconds;
    }
}).play;
)

// shorter than 1 beat later
(
u = PauseStream(t.stream);
TempoClock.schedAbs(t.nextBeat.trunc, u.refresh);
t.stop;
)

u.stop;
```

### `awake`
This method is called by a [Clock](../Classes/Clock.md) on which the Routine was scheduled when its scheduling time is up. It calls [#-next](#-next), passing on the scheduling time in beats as an argument. The value returned by `next` (the value yielded by the Routine) will in turn be returned by this method, thus determining the time which the Routine will be rescheduled for.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inBeats` | The scheduling time in beats. This is equal to the current logical time ([Thread#-beats](../Classes/Thread.md#-beats)). |  
| `inSeconds` | The scheduling time in seconds. This is equal to the current logical time ([Thread#-seconds](../Classes/Thread.md#-seconds)). |  
| `inClock` | The clock which awoke the Routine. |  
### `p`
Convert the routine to a (subclass of) [Pattern](../Classes/Pattern.md).**Returns:** A [Prout](../Classes/Prout.md) that (in response to `asStream`) acts as a generator of independent copies of the original routine (the receiver of `p`).Any subclass of Pattern returns a Stream in response to `asStream`. However, the exact subclass of Stream returned depends on the class of the Pattern. In particular, a Prout returns a Routine in response to `asStream`. Thus, a way to make an independent copy of a Routine is to make a Prout from it with the method `p`, and then create a new Routine from this Prout. In the example immediately below, this second step is done explicitly by calling `asStream`, but in the context of passing arguments to other Patterns, this latter step usually happens automatically, as shown in later examples.
```supercollider
(
r = Routine { "hi".yield; "bye".yield };
r.next.postln;    // "hi" posted

q = r.p.asStream; // or just: r.p.iter
q.next.postln;    // "hi" again

r.next.postln;    // "bye" because r kept its own state, separate from q
)
```


> **Note:** New routines produced by `.p.asStream` run the original routine's function from the beginning. There is no copy of the internal state of the original routine, only its function is copied. On a related note, `Routine.copy` (inherited from `Thread`) does not create a new, separate Routine; it just returns the receiver.

The Routine method `p` is mostly useful in the context of using the result of Routine-returning expressions as arguments to Patterns, when the intent is to use the Routine's result as a pattern, i.e. multiple occurrences acting independently of each other.
```supercollider
(
r = (:2..5); // a seriesIter Routine
Ptuple([r, r]).asStream.all.postln; // posts [[2, 3], [4, 5]]
r.next.postln; // nil

p = r.p; // make a Pattern from r; it doesn't matter that r has ended
Ptuple([p, p]).asStream.all.postln;
// posts [[2, 2], [3, 3], [4, 4], [5, 5]]

// Obviously, explicitly writing the same Routine-valued subexpression twice
// also creates separate Routines.
Ptuple([(:2..5), (:2..5)]).asStream.all.postln;
// posts [[2, 2], [3, 3], [4, 4], [5, 5]]
)
```

In the following example, directly reusing the same Routine object twice in a `Pseq` fails to duplicate its output, because the first embedding fully consumes the routine's (non-nil) output.
```supercollider
(
r = (:2..6);
Pseq([r, r]).asStream.all.postln;
// [2, 3, 4, 5, 6]

p = r.p;
Pseq([p, p]).asStream.all.postln;
// [2, 3, 4, 5, 6, 2, 3, 4, 5, 6]

Pseq([(:2..6), (:2..6)]).asStream.all.postln;
// [2, 3, 4, 5, 6, 2, 3, 4, 5, 6]
)
```


### Accessible instance variables
Routine inherits from [Thread](../Classes/Thread.md), which allows access to some of its state:


```supercollider
(
r = Routine { |inval|
    loop {
        // thisThread refers to the routine.
        postf("beats: % seconds: % time: % \n",
            thisThread.beats, thisThread.seconds, Main.elapsedTime
        );
        1.0.yield;

    }
}.play;
)

r.stop;
r.beats;
r.seconds;
r.clock;
```


### `beats`
**Returns:** The elapsed beats (logical time) of the routine. The beats do not proceed when the routine is not playing.
### `seconds`
**Returns:** The elapsed seconds (logical time) of the routine. The seconds do not proceed when the routine is not playing, it is the converted beat value.
### `clock`
**Returns:** The thread's clock. If it has not played, it is the SystemClock.

## Examples


```supercollider
(
var r, outval;
r = Routine.new({ |inval|
    ("->inval was " ++ inval).postln;
    inval = 1.yield;
    ("->inval was " ++ inval).postln;
    inval = 2.yield;
    ("->inval was " ++ inval).postln;
    inval = 99.yield;
});

outval = r.next('a');
("<-outval was " ++ outval).postln;
outval = r.next('b');
("<-outval was " ++ outval).postln;
r.reset; "reset".postln;
outval = r.next('c');
("<-outval was " ++ outval).postln;
outval = r.next('d');
("<-outval was " ++ outval).postln;
outval = r.next('e');
("<-outval was " ++ outval).postln;
outval = r.next('f');
("<-outval was " ++ outval).postln;
)
```



```supercollider
// wait

(
var r;
r = Routine {
    10.do({ |a|
        a.postln;
        // Often you might see Wait being used to pause a routine
        // This waits for one second between each number
        1.wait;
    });
    // Wait half second before saying we're done
    0.5.wait;
    "done".postln;
}.play;
)
```



```supercollider
// waitUntil

(
var r;
r = Routine {
    var times = { rrand(1.0, 10.0) }.dup(10) + thisThread.beats;
    times = times.sort;
    times.do({ |a|
        waitUntil(a);
        a.postln;
    });
    // Wait half second before saying we're done
    0.5.wait;
    "done".postln;
}.play;
)
```



```supercollider
// Using Routine to set button states on the fly.
(
var update, w, b;
w = Window.new("State Window", Rect(150, Window.screenBounds.height - 140, 380, 60));

// a convenient way to set the button label
update = {
    |but, string| but.states = [[string.asString, Color.black, Color.red]];
    but.refresh;
};

b = Button(w, Rect(10, 10, 360, 40));
b.font_(Font("Impact", 24));

update.value(b, "there is only one state");

// if an action should do something different each time it is called, a routine is the
// right thing to use. This is better than creating variables outside and setting them
// from the action function to keep state from one action to the next

b.action_(Routine { |butt|
    rrand(15, 45).do { |i|
        update.value(butt, "%. there is still only 1 state".format(i + 2));
        0.yield; // stop here
    };
    w.close;
});

w.front;
)
```



```supercollider
// drawing in a window dynamically with Pen
(
var w, much = 0.02, string, synth;

w = Window.new("swing", Rect(100, 100, 300, 500)).front;
w.view.background_(Color.new255(153, 255, 102).vary);

string = "swing ".dup(24).join;

w.drawFunc = Routine {
    var i = 0;
    var size = 40;
    var func = { |i, j| sin(i * 0.07 + (j * 0.0023) + 1.5pi) * much + 1 };
    var scale;
    Pen.font = Font("Helvetica-Bold", 40);
    loop {
        i = i + 1;
        string.do {    |char, j|

            scale = func.value(i, j).dup(6);

            Pen.fillColor = Color.new255(0, 120, 120).vary;
            Pen.matrix = scale * #[1, 0, 0, 1, 1, 0];
            Pen.stringAtPoint(char.asString,
                ((size * (j % 9)) - 10) @ (size * (j div: 9))
            );
        };
        0.yield // stop here, return something unimportant
    }
};

fork { while { w.isClosed.not } { defer { w.refresh }; 0.04.wait } };

w.front;

)
```




