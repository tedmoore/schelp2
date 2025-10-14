# News in 3.11

*A summary of news in SC 3.11*

**Categories:** News

**New feature** - Ableton Link support. See [#sclang: Added](#sclang:-added)
Documentation improvements (#4759, #4732, #4744, #4697, #4326, #4673, #4610, #4515, #4389, #4355, #4333, #4222, #4198, #4144, #4123, #4148, #4140, #4080, #4078, #4057, #4016, #4027, #3925, #3953, #3954, #3912, #3929)

## General: Added
Added NOVA_SIMD build option for cookiecutter based plugin development (#4354)



## General: Changed
Moved RPi and BeagleBone README files into the main repository. (#4639)

The way version numbering is handled in the build system has been reformed. This primarily affects building, but also required changes to the class library (see class library: deprecated) (#4706)

scel has been updated (#4712, #4700)

scvim has been updated (#4197)

`CONTRIBUTING.md` and `DEVELOPING.md` have been updated and moved to the wiki (#4503, #4297, #4028)

`README_LINUX.md` has been updated (#4397, #4159)

Templates for issues have been updated (#4271)

Templates for pull requests have been updated (#4272)

macOS builds now require >= 10.10. Documentation and travis builds are updated to reflect this (#4068)



## General: Fixed
Fixed linking issues for supernova on macOS (#4764)

Fixed build issues when using system boost or yaml-cpp (#4185)



## scsynth and supernova: Added
macOS: Added cocoa event loop to scsynth and supernova to allow future work on VST integration (#4499)

Added a missing flag for no buffer aliasing to the plugin interface (#4356)



## scsynth and supernova: Changed
Replaced a magic number used by the clock (#4714)

supernova now has more deterministic ordering of OSC messages in asynchronous requests (#4460)



## scsynth and supernova: Fixed
Fixed an issue with scsynth and supernova pre-processor directives (fixes issue raised in (#4504)) (#4784)

Fixed issues with clock jitter when using JACK (#4599)

Fixed a bug where Windows would not guard against denormals, which would cause large CPU utilisation (#4504)

Prevented coreaudio from resampling audio stream when using portaudio on macOS (#4477)

Fixed an erroneous include that stopped supernova from compiling in some cases (#4018)



## UGens: Fixed
Fixed an issue with the Done flags on EnvGen (#4789)

Fixed an issue with EnvGen gating non-gated envelopes (#4436)



## sclang: Added
Ableton Link support is here! Check the LinkClock class for more information. (#4331, #4340, #4337)

Add PortAudio bindings to allow listing audio devices on Windows (#4742).



## sclang: Fixed
Fixed an issue where TCP connections were not closed properly when recompiling the class library (#4518)

Fixed `LanguageConfig` sometimes storing in the wrong location (#4680)

Fixed an number of garbage collection related issues that would sometimes render the interpreter unstable (#4192)



## Class library: Added
Added `Platform.architecture` to allow detection of system architecture (#4524)

Added `File.deleteAll` to facilitate the deletion of all files within a given path - to be used for good, not evil (#3921)

Added more flexible ways to modify ControlSpecs related to SynthDef args (#3814)

Added support for listing audio devices on Windows from `ServerOptions.inDevices`, `ServerOptions.outDevices` and `ServerOptions.devices` (#4742)

Added 'composite' event type to default Event prototype (#4441)

Added `SequenceableCollection:unixCmdGetStdOut` to capture std output from external programs (#3539)

Added `String.parseJSON` and `String.parseJSONFile` as an alias around `parseYAML` (#3956)

Added `debug` method to `UnitTest`(#3623)



## Class library: Changed
Improvements to drag functionality with Ndef params (#4093)

`Collection:==` optimised to exit early for identity, inherited by subclasses (#3962)

As part of version reforming, `Main.versionAtMost` and `Main.versionAtLeast` now accept a third argument for the tweak level (e.g. checking for 3.10.4 is now possible) (#4706)

Some UnitTests now print fewer newline characters, and inline warnings have been fixed (#4716)

`NodeProxy:set` can now be used with arbitrary objects (#4090)

UnitTest methods are now isolated from each other (#3836)

Increased the maximum number of attempts for TCP connection to server (#4481)



## Class library: Deprecated
`String.scDir` is deprecated (#4374). Please use `Platform.resourceDir` instead.

`PlotView.plotColors` is deprecated (#4678). Please use `plotColor` instead.

As part of version reforming, `Main.scVersionPostfix` has been deprecated (#4706). Please use `Main.scVersionTweak` instead

`Object.asInt` is deprecated (#4089). Please use `Object.asInteger` instead.



## Class library: Fixed
**Breaking change**: Fixed an issue with `Signal:hammingWindow` using incorrect coefficients. `Signal:hammingWindow_old` can be used for previous behaviour (#4324)

**Breaking change**: `Color:asHSV` could sometimes return NaN -- grayscale colors returned NaN hue, and black returned NaN hue and saturation. Zero values are now returned in these cases, as is the standard (#4369)

Fixed an issue where NamedControl would erroneously convert `name` to a String in some cases (#4761).

Fixed an issue with copying Ndef (#4690)

Fixed an issue where `Document.initAction` would fail to run in some cases (#4582)

Fixed an issue with NodeProxy bundling (#4461)

Fixed a bug in `Ndef:asCode` to correctly handle the default `fadeTime` (#4721, #4695)

Fixed a bug involving fadeTime and `Ndef:copy` (#4701)

Fixed issues with resampling in `Plotter` (#4223)

Fixed a duplicate node ID error in `NodeProxy:xset` (#4512)

Fixed an issue where changing the number of channels or rate of a `NodeProxy` would not free the old bus in time (#4493)

Fixed an issue with `Plotter` resampling of domain given fixed `Array:series` method (#4510)

Fixed a UnitTest for `TestTempoClock` (#4334)

Fixed an issue where `typeView` wasn't updated in NdefGUI (#4056)

Fixed an issue where `findRegexp` would return incorrectly when given an empty string (#4241)

Fix for Score examples and `Platform.defaultTempDir` on OSX (#4221)

Fixed `Plotter` domain and superpose behavior (#4082)

Fix `FunctionDef:argumentString` handling of varArgs (#4085)

Fixed several issues with `SoundFile:cue` behaviour (#3728)

Fixed an issue where `Image` would not support a filename as an argument (#3949)

Fixed UnitTests for `Event` to reset between tests (#3961)

Fixed an issue where `NodeProxy` would use the wrong release shape in some cases (#3776)

Fixed an issue with `Menu.insertAction` not invoking properly (#3871)

Fixed an issue with `UnitTest` where `runAll` could be inherited by individual tests (#4722)



## IDE & SCDoc: Added
Help Browser now supports executing code regions (#3904)



## IDE & SCDoc: Changed
sc-ide is now built as a static library (#4628)

Improved a number of style issues in the Help Browser (#3881)



## IDE & SCDoc: Fixed
Fixed an issue where SCDoc might segfault on deep node trees during tests (#4713)

Fix for an issue on Windows where the IDE would appear to lock during launch in some cases due to an IPC issue between IDE and sclang (#4646)

Fixed an issue with code execution in the Help Browser where comments contained brackets (#4548)

Fixed an issue where copying a theme would crash the IDE if the new theme was not yet saved (#4146)

Fixed a number of deprecations in Qt (#4649)

Fixed a number of rendering warnings from SCDoc (#4265)



