# News in 3.9

*A summary of news in SC 3.9*

**Categories:** News

**Related:** [News-3_8](../Guides/News-3_8.md), [News-3_7](../Guides/News-3_7.md)

We are proud to announce the arrival of SuperCollider 3.9.0! Apologies for being so far behind schedule; we hope the improvements you'll find here will more than make up for it. In 3.9.0, determined contributors have fixed some of SuperCollider's major cross-platform compatibility demons, addressed longstanding issues in the IDE and language, and added new features and bugfixes across the board.
Many thanks to all who contributed to this release: adcxyz, awson, bagong, brianlheim, cappelnord, carlocapocasa, crucialfelix, danstowell, defaultxr, dyfer, elifieldsteel, gagnonlg, ghost, gusano, jamshark70, jd-m, jleben, jmckernon, joshpar, jreus, LFSaw, llloret, LucaDanieli, Magicking, miguel-negrao, muellmusik, patrickdupuis, porres, privong, redFrik, samaaron, scztt, simdax, smoge, smrg-lm, snappizz, telephon, thormagnusson, tiagomoraismorgado88, timsutton, vivid-synth, vividsnow, yurivict, and many more in the SC community who helped in ways other than participation on GitHub.

## Known Issues
The IDE server status display turns yellow after a few seconds when opening `s.makeGui`. This does not cause any usability issues.

Only the first pages of the HTML files produced by SCDoc are printed in web browsers.

The help browser does not remember the last position open in a document when navigating through history, and just jumps to the top of the file.

Supernova loads plugins from "Extensions/plugins" rather than "Extensions".

`LevelIndicator.style()` is broken, which leads to confusing warning messages.

`File.copy` crashes the interpreter if the destination file exists.

On Windows, SerialPort is not available.

On Windows, Supernova is not available.

On Windows, the command-line sclang interpreter is not available.



## General: Added
scvim has seen numerous enhancements now that an actively maintained fork has been merged in.

SuperCollider can now be built on Windows using the MSYS2 toolchain, thanks in particular to @awson and @bagong.

SuperCollider can now be built on FreeBSD, thanks to @shamazmazum and @yurivict.

Detailed documentation on creating macOS standalone applications with SuperCollider has been added, thanks to @adcxyz.

Support for multiple sclang clients connecting to the same server is greatly improved, thanks to @adcxyz.

A CODE_OF_CONDUCT.md and CONTRIBUTING.md have been added to the repository.

Higher-resolution raster versions of the SC cube logo have been added to the top-level `icons/` directory, and a retina-friendly `.icns` file.



## General: Changed
**Breaking change:** `sc_gcd` in the plugin interface now conforms to `gcd(n, 0) == n` instead of `gcd(n, 0) == abs(n)`. This also affects the method `SimpleNumber:gcd`.

The macOS plist file now shows the full version number for both the Version String and Shortened Version String.



## General: Fixed
A typo in the build system prevented the `-msse` compiler flag from being properly set for gcc and clang. This *may* fix subnormal number issues in scsynth that some users have been experiencing.

Fixed a fontification break in scel when too many classes are defined.

Fixed build failures on FreeBSD, GCC 7, and newer versions of Boost.



## scsynth and supernova: Added
scsynth and supernova now support a `/version` command, which responds with a message of the form `/version.reply program major minor patch branch commit`. See the Server Command Reference for full details.



## scsynth and supernova: Changed
On macOS, if scsynth's input and output devices have mismatched sample rates, an error is thrown and the server does not boot. Setting the number of input channels to 0 (`-i 0` on the command line and `s.options.numInputBusChannels = 0` in sclang) now bypasses this error.

Disabled Nagle's algorithm for TCP communication in scsynth. Nagle's algorithm increases bandwidth at the cost of delay, which is undesirable in the context of SuperCollider. Both supernova and sclang have it turned off.



## scsynth and supernova: Fixed
The `/b_read` and `/b_readChannel` messages experienced intermittent failures to read sound files, most notably affecting `Buffer.cueSoundFile`. This has been fixed.



## UGens: Added
A new UGen, `Sanitize`, replaces infinities, NaNs, and subnormals with another signal, zero by default.

The `doneAction` argument to DetectSilence can now be modulated.

UnaryOpUGen now supports the bitwise not operator `bitNot`. It used to simply fail silently.



## UGens: Changed
**Breaking change:** The application binary interface (ABI) for server plugins has changed. This has an important impact: **plugin binaries compiled for SuperCollider 3.8 will not work with SuperCollider 3.9** and vice versa. Please recompile your plugins.

**Breaking change:** `FOS.ar` with control-rate coefficient inputs incorrectly initialized its coefficients at 0 and ramped to the correct values over the first control period. This has been fixed. To restore old behavior, multiply each coefficient by `Line.ar(0, 1, ControlDur.ir)`.



## UGens: Deprecated
`Donce`, a demand-rate UGen with no identifiable purpose, is deprecated. It was most likely used in the production of electronic donce music.



## UGens: Fixed
A number of UGens were discovered to have serious initialization bugs where the UGen would output an initial sample of garbage memory. This can create audio explosions if the buggy UGen's output is fed into certain filter UGens like LPF or Delay1. These bugs have been fixed, affecting BeatTrack, BeatTrack2, CoinGate, Convolution, Convolution2, Convolution2L, Convolution3, DetectSilence, DiskIn, DiskOut, IFFT, KeyTrack, LFGauss, PartConv, PV_JensenAndersen, PV_HainsworthFoote, RunningSum, StereoConvolution2L, and Unpack1FFT.

Fixed a bug with `TGrains` ignoring the `amp` parameter.

`Dibrown` no longer ignores the `length` argument.

`Pitch` no longer ignores the `median` argument.

Fixed a build error in DiskIOUGens on Windows.

Fixed `AudioControl` outputting garbage data if a bus is mapped to it but nothing is playing to the bus.

Fixed incorrect math in `PanAz.ar` with audio-rate input signal and position.



## sclang: Added
Regression tests for the sclang lexer, parser, and compiler have been added. This will make it easier to make fixes to these components in the future.



## sclang: Changed
**Breaking change:** sclang's nestable multiline comments had some mistakes. In particular, sometimes sclang's lexer would incorrectly process overlapping combinations of `/*` and `*/`, so e.g. `*/*/` would be interpreted like `*/ /* */`. This has been fixed.

The maximum number of MIDI ports has been increased from 16 to 128.

The startup post "NumPrimitives = #" is reworded to "Found # primitives".



## sclang: Removed
Removed some unhelpful memory addresses from call stack output in error printing.

Removed some accidentally retained debug posts when the language starts up.



## sclang: Fixed
Fixed help files failing to open on Windows if the user's name contains a non-ASCII character.

Fixed non-ASCII characters breaking the Visual Studio debugger.

Fixed a crash in `Object:perform` when the selector is an Array whose first element is not a Symbol, e.g. `0.perform([0])`.

`thisProcess.nowExecutingPath` is no longer corrupted by `Routine:stop`.

`TextView:selectedString_` now works when the selection size is zero.

Fixed a crash when a method or class/instance variable is named "`none`".

Exceptions occurring in primitives no longer print unavoidable error messages even when wrapped in try-catch.

Fixed a crash when `Dictionary:keysValuesArrayDo` is called with `nil` as an argument.

Fixed `WebView:onLinkActivated` handler failing to fire.

Fixed GUI objects failing to display when launched from the `action` of `unixCmd`. You will still need `{ }.defer`, however.

Fixed `QImage:getColor` always returning zero for the green channel.



## Class library: Added
The UnitTest quark has been incorporated into the main repository.

Added a `rewind` method to `CollStream`.

Added four new class methods to `File` for convenience: `readAllString`, `readAllSignal`, `readAllStringHTML`, `readAllStringRTF`.

`Pstep` accepts an array as a duration argument.

Help files originating from extensions now display a plaque for visibility.

For consistency with other `Platform` class methods, `Platform.recordingsDir` may be used instead of `thisProcess.platform.recordingsDir`.

`SequenceableCollection` has two new instance methods: `flatten2` and `flatBelow`. Additionally, `flatten` is faster now.

The `~callback` function is now available for all `Event` types instead of just "on" events.

Event types now include a `parentEvent`, which provides default values..

New aliases for done actions, e.g. `Done.freeSelf == 2`, are introduced for better readability. See the `Done` helpfile for details.

A new class, `Recorder`, allows recording independently of the `Server` object.

`SequenceableCollection:reduce` supports an adverb argument.

A `recordingsDir` method has been added directly to `Platform`, which transparently calls `thisProcess.platform.recordingsDir`.

`View:-resizeToBounds`, `View:-resizeToHint`, and `Window:-resizeToHint` were added to make it easier to force Views and Windows to automatically resize.

`Maybe` now supports collection methods `at`, `atAll`, `put`, `putAll`, `add`, `addAll`.

`BusPlug:-play` can now accept a `Bus` object.

Breadcrumb links in helpfiles now have separate links for each node in the hierarchy, and pages with multiple categories have separators between the categories.

`SoundFile:*openWrite` now takes additional parameters.

Two new instance methods were added to Symbol: `isBinaryOp` and `isIdentifier`.

Added three convenience methods: `View:resizeToBounds`, `View:resizeToHint`, and `Window:resizeToHint`.

Added `Collection:asEvent` for easy conversion to an `Event`.

`DeprecatedError` now shows you the file path of the deprecated method.

Added two new methods to `SimpleNumber`: `snap` and `softRound`.

`ReadableNodeIDAllocator` offers a new optional replacement for `PowerOfTwoAllocator` that assigns node IDs in a way more readable to humans when working with multiclient setups.

A new "booted" stage has been added to Server objects that have been booted but may not be running yet, accessible via `Server:hasBooted` and `Server.allBootedServers`.



## Class library: Changed
**Breaking change:** Rests in the patterns system have been restructured. Instead of using the `isRest` event property, events are considered rests if one of their properties is a `Rest` object. You must use instances of `Rest` rather than the rest class itself -- use of `Rest` instead of `Rest()` is now deprecated.

**Breaking change:** Fixed `Dictionary:==` only comparing the values of the two dictionaries, not the keys.

**Breaking change:** Fixed a mistake where `Pen.quadCurveTo` used the primitive for a cubic Bézier instead of quadratic. To restore the old behavior, change `Pen.quadCurveTo` to `Pen.curveTo`.

**Breaking change:** The convenience instance methods `Env:kr` and `Env:ar` had the arguments `mul` and `add` renamed to `levelScale` and `levelBias`, since they don't behave like typical `mul` and `add` arguments.

`Collection:processRest` returns the processed collection rather than the original.

The maximum number of MIDI ports has been increased.

Attempting to use a control-rate signal as an input to `Hasher.ar` now results in an error.

The "Cleaning up temp synthdefs..." post message is suppressed if there is nothing to clean up.

To match `Out` and `ReplaceOut`, `LocalOut` and `XOut` now correctly validate their input, checking for a non-zero number of channels.

The argument to `Pattern:fin` has a default of 1 for consistency with `Object:fin`.

`Complex:reciprocal` is faster now.

`Buffer:write` takes floating point arguments, truncating them to integers.

Conversion methods among collection types has been improved and documented.

`clientID` is now protected from being changed while the server is running.



## Class library: Deprecated
`OSCresponder`, `OSCresponderNode`, and `OSCpathResponder` now emit deprecation messages, and will be removed after at least a year. Use `OSCFunc` or `OSCdef` instead.

`Speech` is deprecated, and will be removed in 3.10. The rationale is that its audio output is independent of the server (severely limiting use in compositions), it depends on a proprietary macOS API with no prospect of cross-platform compatibility, and it is too niche to justify inclusion in the core library.

The WiiMote classes (`WiiMote`, `WiiMoteIRObject`, `WiiCalibrationInfo`, `WiiMoteGUI`, `WiiRemoteGUI`, `WiiNunchukGUI`) are deprecated. They never reached a stable state and have gone unmaintained and unused for years.

`AudioIn` is deprecated and will be removed in some future version. It was provided only for backward compatibility with SC2, so its deprecation is long overdue. Use `SoundIn` instead.

`SplayZ` has been deprecated for a long time, but it's finally on the "official" deprecation track and will be removed in 3.10. Use `SplayAz` instead.

`TDuty_old` has been deprecated for a long time, but it now emits a warning and will be removed in 3.10. Use `TDuty` instead.

`Watcher` is an old alias for `SkipJack` provided for backward compatibility. It is officially deprecated and will be removed in 3.10.

`Server:recordNode` is deprecated. Use `Recorder:recordNode` instead (e.g. `s.recorder.recordNode`).

The `Server.set` class variable is deprecated. Use `Server.all` instead.

`SimpleNumber:quantize` is deprecated. Use `SimpleNumber:snap` instead.

`Server:userSpecifiedClientID` is deprecated. Use `Server:clientID` instead.



## Class library: Removed
Removed non-functional stub methods and classes related to Image: the classes ImageFilter and ImageKernel, and the Image instance methods lockFocus, unlockFocus, applyFilters, filters, filteredWith, addFilter, removeFilter, flatten, invert, crop, applyKernel.

`Module`, an unmaintained and unused class for serialization of Synths, has been moved to a quark.

Removed the `openHelpFile` instance methods of `Object`, `String`, `Method`, and `Quark`. These methods have been deprecated since 3.8.

Removed `String:openTextFile` and `Symbol:openTextFile`. Use `String:openDocument` and `Symbol:openTextFile` instead. These methods have been deprecated since 3.8.



## Class library: Fixed
A number of instance methods in `Buffer` and `Bus` did not properly check to see if the object has already been freed, and would act on buffer #0 or bus #0 (which is especially dangerous for the `free` instance method). They now safeguard against this case and throw errors.

The `useRanger` option in `EnvirGui` broke in 3.7. This has been fixed.

`IdentityDictionary` methods `collect`, `select`, and `reject` retain references to the `parent` and `proto` objects.

On Linux, some MIDI methods created method override warnings. These have been silenced.

The "key" argument to `Pn` was not properly set on the first repeat. This has been fixed.

Fixed errors when using a DragSource inside a CompositeView object.

Fixed an interpreter crash when defining a SynthDef whose name is too long. More specifically, the inputs to `UnixFILE:putPascalString` and `CollStream:putPascalString` are now validated.

Server crashes are better handled by the interpreter.

The time display and the "start recording", "pause recording", and "stop recording" menu items now cooperate better with running `Server:record`, `Server:pauseRecording`, and `Server:stopRecording`.

`Server:makeGui` and `Server:makeWindow` broke in 3.8 — the fields in the windows went blank. They are working again.

A timing error with `NodeProxy:-clear` was fixed.

`SoundFileView` correctly displays its grid and does not draw the grid on top of the selection box.

The macOS plist file now shows the full version number for both the Version String and Shortened Version String.

Fixed instances of accidentally silencing error messages caused by neglecting to call `Object:primitiveFailed`.

Patched the possibility of inconsistent `TempoClock` state when the tempo is set via `setTempoAtSec`.

Fixed memory spikes when using `MIDIFunc.sysex` with a large `srcID`.

Fixed spaces sometimes being rendered as `%20` in links in SCDoc.

Fixed `Function:plot` showing an empty graph if the server wasn't booted when the method was invoked.

Fixed blatant errors in `Collection:asAssociations` and `Collection:asPairs` where elements were dropped.

Fixed bugs in `NodeProxy` when using external servers.

`History` now outputs a correct timestamp on Windows.

Fixed Volume control failing to be persistent when rebooting the server.

Fixed `SimpleNumber:asTimeString` producing nonsensical results with the "precision" argument.

`Server:clientID` can now be changed, allowing multiple clients connect to the same server.

History and HistoryGui have been cleaned up.

Fixed duplicate node IDs involving `Server.initTree`.

Fixed supernova crashing when too many controls are used.

`Volume` now respects lag time when it is instantiated or destroyed.



## IDE & SCDoc: Added
Entries in the Documents docklet can be reordered, and document tabs will automatically reorder to reflect this.

"Edit > Preferences > Editor > Display" has a new option that allows replacing tabs with a dropdown whose items are alphabetically ordered. This makes navigation easier in some performance contexts.



## IDE & SCDoc: Changed
Server actions, which were previously in the "Language" menu, have been moved out to their own "Server" menu.

Changed "occurrences" to "matches" in the status bar in the Find and Replace features.

Many minor improvements were made to the look and feel of the documentation.



## IDE & SCDoc: Fixed
Fixed SCDoc refusing to index any further documents if one document has a malformed `copymethod` command.

Some Linux systems had unreadable font colors in the autocomplete tooltips. This has been (finally) fixed.

Fixed a bug where `Document:selectedString_` had no effect.

New tabs are now inserted to the right of the current tab instead of all the way at the end.

The help browser now has keyboard shortcuts for navigating back and forward. These shortcuts are OS-dependent and given to us by Qt.

Fixed the "Find in page..." feature in the help viewer skipping every other occurrence.

Fixed HTML checkboxes appearing in the upper left of the help viewer.

Fixed the right-click menu for the tabs appearing in the wrong place in macOS.



