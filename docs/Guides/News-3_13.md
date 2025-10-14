# News in 3.13

*A summary of news in SC 3.13*

**Categories:** News

Welcome to the SuperCollider 3.13 release! 

> **Note:** In this version numerous UGens have been fixes so that they calculate their initial value as originally intended. In some cases this may create a different result than previously. See below for details


We now also provide a universal build for both x86_64 and arm64 Apple machines.
Below you can find a more complete list of changes in this version. A big thank you to all developers for your contributions!

## General
Countless improvements to help files and documentation (@elifieldsteel, @JaimeClover, @DoHITB, @jamshark70, @heretogo, @capital-G, @alexhughk, @chris75vie, @forrcaho, @paum3, @avdrd, @wolfgangschaltung, @telephon, @redFrik, @madskjeldgaard, @mxw, @dyfer, @tdug, @mtmccrea, @prko, @mjsyts, @grirgz, @chkworks, @balzss, @hectorgonzalezo, @michelestew, @mttvn, @pearcemerritt, @mlang)

Updates and fixes for the test suite: @telephon in [https://github.com/supercollider/supercollider/pull/5304](https://github.com/supercollider/supercollider/pull/5304),  @telephon in [https://github.com/supercollider/supercollider/pull/5676](https://github.com/supercollider/supercollider/pull/5676),  @jamshark70 in [https://github.com/supercollider/supercollider/pull/5666](https://github.com/supercollider/supercollider/pull/5666),  @elgiano in [https://github.com/supercollider/supercollider/pull/5717](https://github.com/supercollider/supercollider/pull/5717),  @dyfer in [https://github.com/supercollider/supercollider/pull/5702](https://github.com/supercollider/supercollider/pull/5702),  @dyfer in [https://github.com/supercollider/supercollider/pull/5738](https://github.com/supercollider/supercollider/pull/5738),  @dyfer in [https://github.com/supercollider/supercollider/pull/5792](https://github.com/supercollider/supercollider/pull/5792),  @telephon in [https://github.com/supercollider/supercollider/pull/5801](https://github.com/supercollider/supercollider/pull/5801),  @dyfer in [https://github.com/supercollider/supercollider/pull/5867](https://github.com/supercollider/supercollider/pull/5867),  @telephon in [https://github.com/supercollider/supercollider/pull/5677](https://github.com/supercollider/supercollider/pull/5677),  @nuss in [https://github.com/supercollider/supercollider/pull/5687](https://github.com/supercollider/supercollider/pull/5687)  @elgiano in [https://github.com/supercollider/supercollider/pull/5716.](https://github.com/supercollider/supercollider/pull/5716.)

Updates and fixes for the automated build system (GitHub Actions): @dyfer in [https://github.com/supercollider/supercollider/pull/5845](https://github.com/supercollider/supercollider/pull/5845),  @dyfer in [https://github.com/supercollider/supercollider/pull/5783](https://github.com/supercollider/supercollider/pull/5783),  @dyfer in [https://github.com/supercollider/supercollider/pull/5847](https://github.com/supercollider/supercollider/pull/5847),  @dyfer in [https://github.com/supercollider/supercollider/pull/5875](https://github.com/supercollider/supercollider/pull/5875),  @dyfer in [https://github.com/supercollider/supercollider/pull/5889](https://github.com/supercollider/supercollider/pull/5889),  @dyfer in [https://github.com/supercollider/supercollider/pull/5776.](https://github.com/supercollider/supercollider/pull/5776.)



## General: Added
Universal macOS build for both Intel x86_64 and Apple arm64 CPUs by @dyfer in [https://github.com/supercollider/supercollider/pull/5953](https://github.com/supercollider/supercollider/pull/5953)

Better description in the about dialog for tagged builds by @dyfer in [https://github.com/supercollider/supercollider/pull/5697](https://github.com/supercollider/supercollider/pull/5697) and [https://github.com/supercollider/supercollider/pull/5739](https://github.com/supercollider/supercollider/pull/5739)



## General: Changed
Update sc-el submodule to latest version by @jxa in [https://github.com/supercollider/supercollider/pull/5600](https://github.com/supercollider/supercollider/pull/5600)

The regular release macOS build now supports macOS 10.14 and up (previously supported 10.13). The legacy build is still provided supporting macOS 10.10 and up.



## General: Fixed
Remove spurious Qt dependencies by @marcan in [https://github.com/supercollider/supercollider/pull/4991](https://github.com/supercollider/supercollider/pull/4991)

Update urls in git submodules to use https by @dyfer in [https://github.com/supercollider/supercollider/pull/5694](https://github.com/supercollider/supercollider/pull/5694)

Fix building on Apple M1 by adding ad hoc code signing by @dyfer in [https://github.com/supercollider/supercollider/pull/5650](https://github.com/supercollider/supercollider/pull/5650)

Build on OpenBSD by @ibz in [https://github.com/supercollider/supercollider/pull/5822](https://github.com/supercollider/supercollider/pull/5822)

Find JACK using cmake's FindPkgConfig by @dvzrv in [https://github.com/supercollider/supercollider/pull/5680](https://github.com/supercollider/supercollider/pull/5680)



## sclang: Added
Ability to set scrollPosition of QWebView by @paum3 in [https://github.com/supercollider/supercollider/pull/5483](https://github.com/supercollider/supercollider/pull/5483)

Interactive Command line interface on Windows using Readline by @dyfer in [https://github.com/supercollider/supercollider/pull/5712](https://github.com/supercollider/supercollider/pull/5712)

Support for MPEG formats by @dyfer in [https://github.com/supercollider/supercollider/pull/5786](https://github.com/supercollider/supercollider/pull/5786)



## sclang: Changed
`Signal -thresh` by @elgiano in [https://github.com/supercollider/supercollider/pull/5432](https://github.com/supercollider/supercollider/pull/5432)



## sclang: Fixed
Stretch behaviour in QcRangeSlider by @miriamvoth in [https://github.com/supercollider/supercollider/pull/5595](https://github.com/supercollider/supercollider/pull/5595)

`Symbol -isPrefix` by @Brandon-Yip2 in [https://github.com/supercollider/supercollider/pull/5708](https://github.com/supercollider/supercollider/pull/5708)

MIDI realtime message type codes on Linux by @jamshark70 in [https://github.com/supercollider/supercollider/pull/5846](https://github.com/supercollider/supercollider/pull/5846)

RF64 and W64 format recognition by @dyfer in [https://github.com/supercollider/supercollider/pull/5877](https://github.com/supercollider/supercollider/pull/5877)

UdpInPort error reporting by @jamshark70 in [https://github.com/supercollider/supercollider/pull/5850](https://github.com/supercollider/supercollider/pull/5850)

Parsing block arguments by @nilninull in [https://github.com/supercollider/supercollider/pull/5522](https://github.com/supercollider/supercollider/pull/5522)

3.13.1 fixes an allocation bug when using an HID on Linux by @dyfer, @bgola and @xunil-cloud in [https://github.com/supercollider/hidapi/pull/17](https://github.com/supercollider/hidapi/pull/17) 



## Class library: Added
Support for `kitty` and `alacritty` Linux terminals by @madskjeldgaard in [https://github.com/supercollider/supercollider/pull/5548](https://github.com/supercollider/supercollider/pull/5548)

`NodeProxy -seti` by @nuss in [https://github.com/supercollider/supercollider/pull/5640](https://github.com/supercollider/supercollider/pull/5640)

Converting mixed outputs in `NodeProxy` instead of failing by @telephon in [https://github.com/supercollider/supercollider/pull/5699](https://github.com/supercollider/supercollider/pull/5699)

Posthook `\synthDefReady` after synthdef is built by @avdrd in [https://github.com/supercollider/supercollider/pull/5657](https://github.com/supercollider/supercollider/pull/5657)

Setting the number of decimal places to `SimpleNumber -asTimeString` by @dyfer in [https://github.com/supercollider/supercollider/pull/4709](https://github.com/supercollider/supercollider/pull/4709)

Make it possible to reschedule a Routine, Task or EventStreamPlayer transparently by @jamshark70 in [https://github.com/supercollider/supercollider/pull/5038](https://github.com/supercollider/supercollider/pull/5038)

Handle `langPort` startup error descriptively by @jamshark70 in [https://github.com/supercollider/supercollider/pull/5158](https://github.com/supercollider/supercollider/pull/5158)

`AppClock -schedAbs` by @telephon in [https://github.com/supercollider/supercollider/pull/5851](https://github.com/supercollider/supercollider/pull/5851)

Vim-like keyshortcuts in HelpBrowser by @paum3 in [https://github.com/supercollider/supercollider/pull/5742](https://github.com/supercollider/supercollider/pull/5742)

Add hooks to the `Quark` class by @capital-G and @telephon in [https://github.com/supercollider/supercollider/pull/5907](https://github.com/supercollider/supercollider/pull/5907)



## Class library: Changed
Refactor functionality: `connectToServerAddr` by @telephon in [https://github.com/supercollider/supercollider/pull/5569](https://github.com/supercollider/supercollider/pull/5569)

Improve efficiency of calling `List -order` by @telephon in [https://github.com/supercollider/supercollider/pull/5561](https://github.com/supercollider/supercollider/pull/5561)

Allow any type of text stream in the FileReader hierarchy by @jamshark70 in [https://github.com/supercollider/supercollider/pull/5611](https://github.com/supercollider/supercollider/pull/5611)

Improve behaviour of error in `loadRelative` by @telephon in [https://github.com/supercollider/supercollider/pull/5744](https://github.com/supercollider/supercollider/pull/5744)

The argument name for `Spawner -seq` was changed to `pattern` by @tdug in [https://github.com/supercollider/supercollider/pull/5767](https://github.com/supercollider/supercollider/pull/5767)

Replace `aiff` with `wav` as the default value for `recHeaderFormat` by @RhnSharma in [https://github.com/supercollider/supercollider/pull/5559](https://github.com/supercollider/supercollider/pull/5559)

Guarantee that `SetBuf` gets an array by @telephon in [https://github.com/supercollider/supercollider/pull/5743](https://github.com/supercollider/supercollider/pull/5743)

Delete unused method `*findMethod` from ScIDE class by @jamshark70 in [https://github.com/supercollider/supercollider/pull/5840](https://github.com/supercollider/supercollider/pull/5840)

HistoryGui: improve display readability by @adcxyz in [https://github.com/supercollider/supercollider/pull/5861](https://github.com/supercollider/supercollider/pull/5861)

Create only a single server meter by default by @telephon in [https://github.com/supercollider/supercollider/pull/5908](https://github.com/supercollider/supercollider/pull/5908)



## Class library: Deprecated
QuartzComposerView by @dyfer in [https://github.com/supercollider/supercollider/pull/5710](https://github.com/supercollider/supercollider/pull/5710)



## Class library: Fixed
Prevent possible infinite recursion in `*initClassTree` by @jamshark70 in [https://github.com/supercollider/supercollider/pull/5575](https://github.com/supercollider/supercollider/pull/5575)

Use named controls in node proxy by @telephon in [https://github.com/supercollider/supercollider/pull/5675](https://github.com/supercollider/supercollider/pull/5675)

Fix implicit specs in synth functions by @adcxyz in [https://github.com/supercollider/supercollider/pull/5681](https://github.com/supercollider/supercollider/pull/5681)

Put `protect` in PauseStreams by @jamshark70 in [https://github.com/supercollider/supercollider/pull/5626](https://github.com/supercollider/supercollider/pull/5626)

Fix some filters with node proxy by @telephon in [https://github.com/supercollider/supercollider/pull/5679](https://github.com/supercollider/supercollider/pull/5679)

Handle buffer instance of `NdefGui` as argument by @redFrik in [https://github.com/supercollider/supercollider/pull/5692](https://github.com/supercollider/supercollider/pull/5692)

Defer GUI updates in `ServerPlusGUI` by @dyfer in [https://github.com/supercollider/supercollider/pull/5491](https://github.com/supercollider/supercollider/pull/5491)

Make envelopes behave like patterns in a pattern proxy by @telephon in [https://github.com/supercollider/supercollider/pull/5287](https://github.com/supercollider/supercollider/pull/5287)

Fix `Server.remote` `-startAliveThread` by @elgiano in [https://github.com/supercollider/supercollider/pull/5715](https://github.com/supercollider/supercollider/pull/5715)

Exclude QQuartzComposer from headless builds by @elgiano in [https://github.com/supercollider/supercollider/pull/5733](https://github.com/supercollider/supercollider/pull/5733)

Prevent double-firing of cleanup functions in `EventStreamCleanup` by @jamshark70 in [https://github.com/supercollider/supercollider/pull/5386](https://github.com/supercollider/supercollider/pull/5386)

Fix cleanup setup for Pmono and PmonoArtic by @eleses in [https://github.com/supercollider/supercollider/pull/5027](https://github.com/supercollider/supercollider/pull/5027)

Escaping of `String:openOS` by @elgiano in [https://github.com/supercollider/supercollider/pull/5322](https://github.com/supercollider/supercollider/pull/5322)

Recording in `Pbind` by @madredeuz in [https://github.com/supercollider/supercollider/pull/5793](https://github.com/supercollider/supercollider/pull/5793)

Cast sampleRate to Integer in `SoundFileView -setData` by @redFrik in [https://github.com/supercollider/supercollider/pull/5812](https://github.com/supercollider/supercollider/pull/5812)

Use embedded specs in Ndef for guis by @adcxyz in [https://github.com/supercollider/supercollider/pull/5686](https://github.com/supercollider/supercollider/pull/5686)

Plotter: update colors, fix grid and axis labels, remove `Plotter -gui` method by @mtmccrea in [https://github.com/supercollider/supercollider/pull/4511](https://github.com/supercollider/supercollider/pull/4511), [https://github.com/supercollider/supercollider/pull/5827](https://github.com/supercollider/supercollider/pull/5827), [https://github.com/supercollider/supercollider/pull/5858.](https://github.com/supercollider/supercollider/pull/5858.) Grid lines and their labels are improved, along with axis labels, which are now settable by their own methods `labelX_` and `labelY_`. The x-axis label inherits the units of a `domainSpec` if it is explicitly set and labelX hasn't already been set

Make sure `Plot` color is not converted to array by @telephon in [https://github.com/supercollider/supercollider/pull/5849](https://github.com/supercollider/supercollider/pull/5849)

`BinaryOpUGen` optimization for `a === b` cases by @smrg-lm in [https://github.com/supercollider/supercollider/pull/5427](https://github.com/supercollider/supercollider/pull/5427)

Remove inline warnings in the class library by @telephon in [https://github.com/supercollider/supercollider/pull/5856](https://github.com/supercollider/supercollider/pull/5856)

Make maxLogins not to exceed 32 in `ServerOptions` by @jamshark70 in [https://github.com/supercollider/supercollider/pull/5149](https://github.com/supercollider/supercollider/pull/5149)

Sample alignment with grid lines in `Function -plot` by @mtmccrea in [https://github.com/supercollider/supercollider/pull/5855](https://github.com/supercollider/supercollider/pull/5855)

Make `subBus` use the same server as receiver by @telephon in [https://github.com/supercollider/supercollider/pull/5887](https://github.com/supercollider/supercollider/pull/5887)

GridLines improvements: fix exponential grids and add spacing control by @dyfer in [https://github.com/supercollider/supercollider/pull/5161](https://github.com/supercollider/supercollider/pull/5161) and @mtmccrea in [https://github.com/supercollider/supercollider/pull/5895](https://github.com/supercollider/supercollider/pull/5895), [https://github.com/supercollider/supercollider/pull/5942](https://github.com/supercollider/supercollider/pull/5942)

Expand tilde to users home directory on Windows by @miriamvoth in [https://github.com/supercollider/supercollider/pull/5431](https://github.com/supercollider/supercollider/pull/5431)

Improve `Function -flop` implementation that works with string ellipsis and keyword arguments by @telephon in [https://github.com/supercollider/supercollider/pull/5499](https://github.com/supercollider/supercollider/pull/5499), [https://github.com/supercollider/supercollider/pull/5900](https://github.com/supercollider/supercollider/pull/5900)

Time precision issues with Psync and EventStreamPlayer by @totalgee in [https://github.com/supercollider/supercollider/pull/5891](https://github.com/supercollider/supercollider/pull/5891)

`Pattern -record` by @jamiehodge in [https://github.com/supercollider/supercollider/pull/5883](https://github.com/supercollider/supercollider/pull/5883)

Make `Rest` accepted by Patterns by @olafklingt in [https://github.com/supercollider/supercollider/pull/5882](https://github.com/supercollider/supercollider/pull/5882)

`Buffer *cueSoundFile`: keep `path` value by @telephon in [https://github.com/supercollider/supercollider/pull/5937](https://github.com/supercollider/supercollider/pull/5937)



## scsynth and supernova: Added
Support for MPEG formats by @dyfer in [https://github.com/supercollider/supercollider/pull/5786](https://github.com/supercollider/supercollider/pull/5786)

Option for LIB_SUFFIX in the CMake build system by @tdug in [https://github.com/supercollider/supercollider/pull/5644](https://github.com/supercollider/supercollider/pull/5644) and @elgiano in [https://github.com/supercollider/supercollider/pull/5728](https://github.com/supercollider/supercollider/pull/5728)

Error warnings and /fail replies to /d_load and /d_loadDir (scsynth) by @muellmusik in [https://github.com/supercollider/supercollider/pull/5244](https://github.com/supercollider/supercollider/pull/5244)



## scsynth and supernova: Fixed
Make `/g_head` always fire an `/n_move` reply (scsynth) by @Sciss in [https://github.com/supercollider/supercollider/pull/5580](https://github.com/supercollider/supercollider/pull/5580)

Non-real-time mode in supernova by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/5616](https://github.com/supercollider/supercollider/pull/5616)

Crash when passing audio/control bus mapping to arrayed Group control in supernova by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/5617](https://github.com/supercollider/supercollider/pull/5617)

Possible crash with unit commands by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/5610](https://github.com/supercollider/supercollider/pull/5610)

Use the `/error` messages to turn on / off the console printing in supernova by @vitreo12 in [https://github.com/supercollider/supercollider/pull/5820](https://github.com/supercollider/supercollider/pull/5820)

Support for `libsndfile` version >= 1.1.0 by @dyfer in [https://github.com/supercollider/supercollider/pull/5761](https://github.com/supercollider/supercollider/pull/5761)

Print plugin API method in supernova by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/5874](https://github.com/supercollider/supercollider/pull/5874)

UdpInPort error reporting by @jamshark70 in [https://github.com/supercollider/supercollider/pull/5850](https://github.com/supercollider/supercollider/pull/5850)

Behavior of .sqrt and .reciprocal operations on the server on Apple M1 CPUs by @dyfer in [https://github.com/supercollider/supercollider/pull/5901](https://github.com/supercollider/supercollider/pull/5901)

OffsetOut_Ctor error in supernova on Windows by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/5902](https://github.com/supercollider/supercollider/pull/5902)



## UGens: Added
Argument `binout` to `SpecPcile` by @woolgathering in [https://github.com/supercollider/supercollider/pull/5097](https://github.com/supercollider/supercollider/pull/5097)



## UGens: Changed
`Impulse` is now initialized correctly such that:

- it will fire on the first sample, given the default phase of 0 (or multiple of 1).
- a frequency of 0 fires once and only once on the first sample (unless the frequency subsequently changes).
- negative frequencies and phases are now supported and phase of any value is wrapped into range.


These are intended and documented behaviors, but which failed previously in certain UGen configurations. Therefore, users may observe changes to the initial state of synth graphs that use Impulse. (Especially triggered UGens.) For details, a list of resolved/changed behavior can be found here.

For more details see [https://github.com/supercollider/supercollider/pull/4150](https://github.com/supercollider/supercollider/pull/4150) by @mtmccrea

Numerous UGens have been updated so that their initialization sample is set correctly by @mtmccrea:  `OscUGens` in [https://github.com/supercollider/supercollider/pull/5787](https://github.com/supercollider/supercollider/pull/5787),  `Klang` and `Klank` in [https://github.com/supercollider/supercollider/pull/5817](https://github.com/supercollider/supercollider/pull/5817),  `TWindex` in [https://github.com/supercollider/supercollider/pull/5815](https://github.com/supercollider/supercollider/pull/5815), `Free` and `PauseSelf` in [https://github.com/supercollider/supercollider/pull/5914](https://github.com/supercollider/supercollider/pull/5914), `Poll` in [https://github.com/supercollider/supercollider/pull/5965](https://github.com/supercollider/supercollider/pull/5965).

`Integrator` Ctor passes through the first sample only by @jamshark70 in [https://github.com/supercollider/supercollider/pull/5352.](https://github.com/supercollider/supercollider/pull/5352.) Prior to v3.13, there was a bug that caused the Integrator to double-count the initial value: the integral of a single 1 followed by endless 0s ends up being 2. Starting with v.3.13, it's 1 as expected.

`PanAz`, due to fixing leaks and imprecisions by @elgiano in [https://github.com/supercollider/supercollider/pull/4971](https://github.com/supercollider/supercollider/pull/4971)



## UGens: Fixed
`Tap` samplerate compensation by @morfant in [https://github.com/supercollider/supercollider/pull/5606](https://github.com/supercollider/supercollider/pull/5606)

Audio rate versions of triggered random ugens by @telephon in [https://github.com/supercollider/supercollider/pull/5344](https://github.com/supercollider/supercollider/pull/5344)

`AudioControl` and `InFeedback` processing for an extra cycle by @vitreo12 in [https://github.com/supercollider/supercollider/pull/5601](https://github.com/supercollider/supercollider/pull/5601)

Remove RTAlloc exceptions, and review all plugins' RTAlloc/RTFree by @elgiano in [https://github.com/supercollider/supercollider/pull/5713](https://github.com/supercollider/supercollider/pull/5713)



