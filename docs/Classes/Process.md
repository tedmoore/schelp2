# Process

**Categories:** Core>Kernel

*Runtime environment for the virtual machine and interpreter.*

## Description

A Process is the runtime environment for the virtual machine and interpreter. It has a subclass named [Main](../Classes/Main.md) which is where you should override the methods of Process. There are two methods of interest. One is named `startup` and is called after the class library has been compiled. The other is named `run` and is called when the user chooses the Run menu command.


## Class Methods

### `tailCallOptimize`
Get or set tail call optimization. The default is on. Setting this to `false` can help with debugging by including intermediate levels in an error backtrace.

## Instance Methods

### `nowExecutingPath`
Usage: `thisProcess.nowExecutingPath`Returns the full path to the file containing the code that is currently executing *interactively* in the interpreter. Usually this is the current document. If the code block executes another file on disk, using [String#-load](../Classes/String.md#-load) or [String#-loadPaths](../Classes/String.md#-loadpaths), `nowExecutingPath` will be the location of the executed file.`nowExecutingPath` is valid only for interactive code, i.e., code files with a `.scd` extension. It does not apply to class definitions (`.sc`). For that, use `thisMethod.filenameSymbol` or `this.class.filenameSymbol`.This method is supported in the SuperCollider IDE, the macOS-only SuperCollider.app, and the scel (SuperCollider-Emacs-Lisp) environment. In other editor environments, it will return `nil`.> **⚠️ Warning:** `nowExecutingPath` has a corresponding setter method, `nowExecutingPath_`, for internal use only by the interpreter. Do not call the setter method!### `startup`
called after the class library has been compiled. Override this in class [Main](../Classes/Main.md) to do whatever you want.### `run`
called when the user chooses the Run menu command. Override this in class [Main](../Classes/Main.md) to do whatever you want.### `mainThread`
The top-level [Thread](../Classes/Thread.md), i.e the [parent](../Classes/Thread.md#-parent) of all other Threads. This instance of Thread always exists and is created with the Process when SuperCollider starts.All SuperCollider code initially runs in the context of the main Thread:- Code evaluated in code editor
- Code evaluated on command line
- Tasks scheduled on any [Clock](../Classes/Clock.md)
- Functions evaluated in response to incoming OSC and MIDI messages
This means that [thisThread](../Classes/Thread.md#.thisthread) will always initially point to the main Thread. However, when some code starts a [Routine](../Classes/Routine.md), the Routine becomes the current Thread, with the main Thread as its parent.

