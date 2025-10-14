# News in 3.5

*A summary of news in SC 3.5*

**Categories:** News


## Language-side news

### Qt GUI
A new cross-platform GUI kit intended to replace Cocoa and an alternative to SwingOSC. See [News-Qt-GUI](../Guides/News-Qt-GUI.md) for more.




### SCDoc
A new help-system provides consistent documentation with good introspection and easy [searching](../Search.md) and [browsing](../Browse.md).

The help-files are written in a markup language which is then parsed and used to generate HTML files, which are displayed with the new [WebView](../Classes/WebView.md) widget inside the [HelpBrowser](../Classes/HelpBrowser.md).

See [SCDoc](../Classes/SCDoc.md), [SCDocSyntax](../Reference/SCDocSyntax.md), [WritingHelp](../Guides/WritingHelp.md).

Also a new method [Help#*methodArgs](../Classes/Help.md#*methodargs) returns a human-readable string of arguments and default values for a method. Example: `Help.methodArgs("SinOsc.ar")`

In SuperCollider version 3.5.2, SCDoc has been rewritten and the parser is now implemented in C++ for speed and stability. The syntax has gotten stricter, and it will throw errors or warnings if there are faults in the documentation. See [WritingHelp / News in SC 3.5.2 ](../Guides/WritingHelp.md#news-in-sc-3.5.2) for some important changes to keep in mind.




### OSC and MIDI responders
The new [OSCFunc](../Classes/OSCFunc.md) and [MIDIFunc](../Classes/MIDIFunc.md) provides better alternatives to the old [OSCresponderNode](../Classes/OSCresponderNode.md) and [NoteOnResponder](../Classes/NoteOnResponder.md), etc.

OSCFunc can receive on any port, not only the main `NetAddr.langPort`.




### New Location of Startup file
The [sclang startup file](../Reference/StartupFile.md) has moved to `Platform.userConfigDir +/+ "startup.scd"`. Old platform-specific startup file locations have been deprecated. The new startup file is plain-text, rtf is not supported.




### Language configuration files
The Linux-only library configuration file has been deprecated. It is replaced by a cross-platform language configuration file, which is located at `Platform.userConfigDir +/+ "sclang_conf.yaml"` . It can be configured via the [LanguageConfig](../Classes/LanguageConfig.md) class.




### Sced3
The GEdit plugin sced has been updated to support GEdit version 3.




### WiiMote
`WiiMote.discover` now returns the device object, or nil if it failed.




### Bus-asMap in patterns
Bus-asMap symbols are now allowed in `\freq` and friends in patterns.




### Warn on classlib overwrites
Warnings are posted when extensions overwrites methods in main class lib, unless the extensions are put in a subfolder named "SystemOverwrites".




### Filesystem utils
New cross-platform filesystem utilities: [File#*copy](../Classes/File.md#*copy), [File#*mtime](../Classes/File.md#*mtime), [File#*mkdir](../Classes/File.md#*mkdir), [File#*realpath](../Classes/File.md#*realpath), [File#*type](../Classes/File.md#*type), [File#*fileSize](../Classes/File.md#*filesize)




### String-openTextFile
[String#-openTextFile](../Classes/String.md#-opentextfile) now works also on frontends without [Document](../Classes/Document.md) support. It falls back to [String#-openOS](../Classes/String.md#-openos) to open the file with the default application for that file type.




### Optional trailing comma
It was already allowed to have a trailing comma in arrays: `[1,2,3,]`, but now it's also allowed in Event construction and message arguments:


```supercollider
(a:1, b:2, c:3,);

Pbind(
    \foo, 1,
    \bar, 2,
);

myFunc.value(1, 2, 3,);
```





### Various bugfixes
A lot of bugs has been fixed, for example: String regexp primitives, multichannel wrappers of SequenceableCollection, CoinGate.ar, T2K, WiiMote, SynthDesc.




### Interpreter Performance Improvements
The sclang now uses token threading> *[http://www.complang.tuwien.ac.at/forth/threaded-code.html](http://www.complang.tuwien.ac.at/forth/threaded-code.html)* instead of one huge switch statement for bytecode dispatching.




### PriorityQueue stable order
The [PriorityQueue](../Classes/PriorityQueue.md) now provides a stable heap order: items of the same time value will have a FIFO order.




### plot improvements
[plot](../Reference/plot.md) has been changed to use the [Plotter](../Classes/Plotter.md) class, which was formerly used by the `plot2` methods. `plot2` has been deprecated, the old behavior is still available via the `plotOld` methods, which have also been deprecated.




### UI deprecated
The UI class has been deprecated. Its functionality is now provided by the [ShutDown](../Classes/ShutDown.md) and [OnError](../Classes/OnError.md) classes.




### Panner and XFade classes deprecated
The Panner and XFade classes that been used internally are now deprecated. UGens are better off, implementing the `checkInputs` explicitly.




### Quark files outside DIRECTORY
`*.quark` files are now allowed to be within the quark itself rather than in the DIRECTORY. This allows manually installed quarks to be easily managed by [Quarks#*gui](../Classes/Quarks.md#*gui)




### New error marker
Instead of the non-cross-platform bullet-character (•), the error token in error messages are now underlined with `^^^` characters instead.

For example, the code `[a, %%&&**, b]` results in:






## Server-side news

### Bitwise ops
The bitwise operators `&` (and), `|` (or), `xor:` (xor), `<<` (left shift) and `>>` (right shift) are now supported server-side on audio and control signals. Example:


```supercollider
// 8-bit magic
(
play {
    var t = PulseCount.ar(Impulse.ar(8e3));
    HPF.ar(
        (
            ((t * 15) & (t >> 5)) |
            ((t * 5)  & (t >> [3, 4])) |
            ((t * 2)  & (t >> 9)) |
            ((t * 8)  & (t >> 11))
            - 3 % 256
        ) / 127-1 * 3
        , 20
    ).tanh
}
)
```





### VarLag UGen
The new [VarLag](../Classes/VarLag.md) UGen provides the same functionality as Lag but with linear and other curves.




### DelTapWr/DelTapRd UGens
The new [DelTapRd](../Classes/DelTapRd.md) and [DelTapWr](../Classes/DelTapWr.md) UGen can be used to easily implement multitap delays.




### Node-onFree
A new method [Node#-onFree](../Classes/Node.md#-onfree) runs a function when node finished playing.




### LocalIn initial value
[LocalIn](../Classes/LocalIn.md) now has an input for initial value.




### Close buffers on free
`/b_free` also free's soundfile if open (like `/b_close`)




### More done flags
[Demand](../Classes/Demand.md), [VDiskIn](../Classes/VDiskIn.md) and [DiskIn](../Classes/DiskIn.md) now sets done flag (to be used by [Done](../Classes/Done.md) or [FreeSelfWhenDone](../Classes/FreeSelfWhenDone.md))




### Shared Memory Server Interface
A shared-memory interface to the server has been introduced. This allows scoping and synchronous control bus access for local clients.




### HPF/RHPF internal precision
The recursive filter loop for [HPF](../Classes/HPF.md) and [RHPF](../Classes/RHPF.md) has been changed to double-precision in order to avoid quantization noise. Pieces that depend on the quantization noise can make use of the GlitchUGens provided in sc3-plugins, which implement the old behavior.




### Plugin entry point
Plugins should use the `PluginLoad` macro as entry point instead of implementing a `load` funcion. This allows ABI version checks and ensures that the entry point function is correctly exported from the shared library. See [WritingUGens](../Guides/WritingUGens.md) for details.




### New FFT Plugin API
A new FFT API for server plugins has been introduced: this simplifies writing FFT ugens in a cross-platform manner, since no external FFT libraries are required.




### Supernova
A new multi-processor implementation of scsynth. Parallelism of the synthesis graph is exposed to the user via the  [ParGroup](../Classes/ParGroup.md) class. Supernova is currently Linux-only. It is not provided in the macOS/Windows binaries. In order to play patterns inside a ParGroup, the [PparGroup](../Classes/PparGroup.md) can be used. Scsynth emulates parallel groups with groups.

Plugins have to be adapted by acquiring spinlocks when accessing busses or buffers. See [WritingUGens](../Guides/WritingUGens.md) for details.





