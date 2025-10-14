# News in 3.14

*A summary of news in SC 3.14*

**Categories:** News


## Notable changes and additions
These are the highlights of the changes in SC 3.14. See sections below for details.

- Sclang functions now support collecting arbitrary keyword arguments via `{ |...args, kwargs| kwargs }.`
- The initialization sample of multiple UGens was fixed.
- Documentation can now also be themed like the IDE.
- Due to updated bundled boost libraries, FluCoMa UGens which were working under SuperCollider 3.13 are not compatible anymore with 3.14! Go to [https://github.com/flucoma/flucoma-sc](https://github.com/flucoma/flucoma-sc) to check for a compatible version.
- Even though these are not as much of user-facing changes, there were countless structural upgrades: we migrated to qt6, added and improved tests, updated 3rd-party libraries, updated the build system for most recent build tools, and adapted a new organizational structure for development.


Changes to UGens, potentially affecting their output values, are now documented in detail in a separate document: [UGen-Changelog](../Guides/UGen-Changelog.md).



## Breaking Changes
- Phasor: fix init sample: don't ignore trig on first sample. If code relied on this bug, it may change behavior. by @elgiano in [https://github.com/supercollider/supercollider/pull/6833](https://github.com/supercollider/supercollider/pull/6833)
- fix `mod` for negative integer modulus (only). The method `modSeaside` can be used to restore the original behavior, named this way for reasons not immediately obvious, by @passyur and @telephon [https://github.com/supercollider/supercollider/pull/6699](https://github.com/supercollider/supercollider/pull/6699)
- `Splay` and `SplayAz` level compensation has been fixed and made more flexible, this may change overall level distribution, by @adcxyz [https://github.com/supercollider/supercollider/pull/6804.](https://github.com/supercollider/supercollider/pull/6804.)
- mark `SetResetFF` explicitly as unipolar, this changes output levels when using `range` – e.g. if you have used `.range(0, 1)`, it had assumed bipolar default so far and returned a range of `[0.5, 1]`.) by @capital-G in [https://github.com/supercollider/supercollider/pull/6023](https://github.com/supercollider/supercollider/pull/6023)
- `Set.remove` now returns the item removed by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6409](https://github.com/supercollider/supercollider/pull/6409)
- fix Dictionary `trueAt` by @telephon in [https://github.com/supercollider/supercollider/pull/6001](https://github.com/supercollider/supercollider/pull/6001), and @mtmccrea in [https://github.com/supercollider/supercollider/pull/6335](https://github.com/supercollider/supercollider/pull/6335) This changes behavior as follows:| **trueAt** | **obj** | **nil** | **true** | **false** | 
| --- | --- | --- | --- | --- || previous: | obj | false | true | false | | new: | false | false | true | false | 




## New Contributors
Thanks to new contributors!

@gorenje, @JordanHendersonMusic, @cdbzb, @Xeonacid, @Shu-AFK, @silvanocerza, @alexyuwen, @xunil-cloud, @sadguitarius, @sonata-chen, @frenchy64, @SimonDeplat, @martindupras, @unthingable, @HotwheelsSisyphus, @OzelotVanilla, @juergenrmayer, @lapnitnelav, @tedmoore, @passyur, @tremblap, @carltesta, @djiamnot, @wortsampler



## General

### Added
So far, additional function and method arguments could be captured into an array via the syntax: `f = { |a, b ... args| args }; f.(1,2,3,4) // returns [3, 4]`. It was not possible to use other keywords than those explicitly given (here `a` and `b`) Now we can also capture arbitrary keyword arguments, via the syntax: `f = { |a, b ... args, kwargs| kwargs }; f.(x:3, y:4) // returns [\x, 3, \y, 4]`.

The new keyword argument capture was implemented by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6339](https://github.com/supercollider/supercollider/pull/6339), in collaboration with @telephon and @capital-G.

This change makes a number of new things possible, e.g.

- `performList`, `functionPerformList`, `superPerform`, `tryPerform`, `doesNotUnderstand` take kwargs now. This makes message forwarding more flexible and more complete.
- A new `superPerformArgs` method was necessary to avoid an infinite loop in passing keyword arguments up to the parent class, by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6568](https://github.com/supercollider/supercollider/pull/6568)
- keywords in `*newCopyArgs` allow for cleaner constructors in classes with many instance variables, you can now write expressions like `^super.newCopyArgs(freq:440)` by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6398](https://github.com/supercollider/supercollider/pull/6398)
- keyword arguments now work for composed and higher order functions (`Maybe`, `CallOnce`, `UnaryOpFunction`, `BinaryOpFunction`, `NaryOpFunction`, `FunctionList`, `UnaryOpFunctionProxy`, `BinaryOpFunctionProxy`, `NAryOpFunctionProxy`), so e.g. you can write `f = { |x, y = 1| x + y } * { |x, y = 2| x ** y }; f.(x:2, y:6)` by @telephon in [https://github.com/supercollider/supercollider/pull/6786](https://github.com/supercollider/supercollider/pull/6786)
- a new method for all objects which passes keyword arguments as a list explicitly: `performArgs(selector, args, kwargs)`
- methods on `FunctionDef` for finding out their argument form: `varArgsValue`, `hasVarArgs`, `hasKwArgs`.
- passing arguments to Scale and Tuning selectors works now: `Scale.ionian(tuning:Tuning.kirnberger)` (this was the original problem to be solved).
- Object prototyping: pseudo-methods in `IdentityDictionary` take keyword arguments and pass them on correctly. So you can write now: `u = (dive:{|self, speed, depth| ... }); u.dive(depth: -5)`
- `DoesNotUnderstandError` informs about keyword arguments.
- Make `Pbind` work with kwargs (this syntax works now: `Pbind(note: Pseq([-3, -2, 0, 1, 6, 13]), dur: 0.05, amp: 0.1).play`) by @JordanHendersonMusic and @telephon in [https://github.com/supercollider/supercollider/pull/6530](https://github.com/supercollider/supercollider/pull/6530)






## Class library

### Added
- ScopeView: allow lissajou mode for more than two channels as overlaid pairs by @elgiano in [https://github.com/supercollider/supercollider/pull/6212](https://github.com/supercollider/supercollider/pull/6212)
- Support UGens for math ops: Complex on ugens work for square root, sign methods like isPositive, e.g. (`{ Complex(MouseX.kr, MouseY.kr).sqrt.poll; 0 }.play`) by @telephon in [https://github.com/supercollider/supercollider/pull/6595](https://github.com/supercollider/supercollider/pull/6595)





### New classes
- Add [ExampleFiles](../Classes/ExampleFiles.md) class by @capital-G in [https://github.com/supercollider/supercollider/pull/6685](https://github.com/supercollider/supercollider/pull/6685) and @tedmoore [https://github.com/supercollider/supercollider/pull/6720](https://github.com/supercollider/supercollider/pull/6720)
- [NodeTreeView](../Classes/NodeTreeView.md) class. Server.plotTree creates an instance of it. by @prko, @telephon, and @dyfer in [https://github.com/supercollider/supercollider/pull/6282](https://github.com/supercollider/supercollider/pull/6282), [https://github.com/supercollider/supercollider/pull/6834](https://github.com/supercollider/supercollider/pull/6834), [https://github.com/supercollider/supercollider/pull/6913](https://github.com/supercollider/supercollider/pull/6913), [https://github.com/supercollider/supercollider/pull/6917](https://github.com/supercollider/supercollider/pull/6917), [https://github.com/supercollider/supercollider/pull/6914](https://github.com/supercollider/supercollider/pull/6914), [https://github.com/supercollider/supercollider/pull/6948](https://github.com/supercollider/supercollider/pull/6948)





### New methods
- `SoundFile:writeArray` makes it easier to write multichannel files by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6219](https://github.com/supercollider/supercollider/pull/6219)
- `Buffer.loadChannelDialog` by @prko in [https://github.com/supercollider/supercollider/pull/6122](https://github.com/supercollider/supercollider/pull/6122)
- `wchoosen` implementation by @telephon in [https://github.com/supercollider/supercollider/pull/6601](https://github.com/supercollider/supercollider/pull/6601) (credits to @Asmatzaile and all who discussed on [https://scsynth.org/t/choosing-how-to-choose-with-self-normalising-weights/9557)](https://scsynth.org/t/choosing-how-to-choose-with-self-normalising-weights/9557))
- `isRectangular` for Array. by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6225](https://github.com/supercollider/supercollider/pull/6225)
- `defaultBranchName` method for Git.sc by @cdbzb in [https://github.com/supercollider/supercollider/pull/6072](https://github.com/supercollider/supercollider/pull/6072)
- `.bounds_` setter method for Stethoscope by @prko in [https://github.com/supercollider/supercollider/pull/6281](https://github.com/supercollider/supercollider/pull/6281)
- `parseOSC` method for `Int8Array` by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/6151](https://github.com/supercollider/supercollider/pull/6151)
- `localIP`, `localEndPoint` and `localIPs` class methods for NetAddr by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/6153](https://github.com/supercollider/supercollider/pull/6153)
- `postBugReportInfo` class method for `Platform` by @capital-G in [https://github.com/supercollider/supercollider/pull/6928](https://github.com/supercollider/supercollider/pull/6928)





### New arguments
- `thumbSize` argument for Slider2D by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6270](https://github.com/supercollider/supercollider/pull/6270)
- `parent` argument for all `.plot` and `.plotAudio` methods for placing them in window. by @prko in [https://github.com/supercollider/supercollider/pull/6202](https://github.com/supercollider/supercollider/pull/6202)
- `bounds` argument for `.plotTree` in [https://github.com/supercollider/supercollider/pull/6294](https://github.com/supercollider/supercollider/pull/6294)
- `clock` argument (default: `AppClock`) for waitForBoot and doWhenDone by @prko in [https://github.com/supercollider/supercollider/pull/6198](https://github.com/supercollider/supercollider/pull/6198)
- `position` argument for Server `meter` to set position (width and height are automatically calculated) by @prko in [https://github.com/supercollider/supercollider/pull/6283](https://github.com/supercollider/supercollider/pull/6283)
- Add kwargs for Pbindef and PbindProxy by @telephon in [https://github.com/supercollider/supercollider/pull/6977](https://github.com/supercollider/supercollider/pull/6977)





### Changed
- Too many args passed to certain 'inlined' methods by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6302](https://github.com/supercollider/supercollider/pull/6302)
- Keep SystemSynthDefs in dictionary by @telephon in [https://github.com/supercollider/supercollider/pull/5968](https://github.com/supercollider/supercollider/pull/5968) (This allows to send them to an non-realtime server server)
- JITLib: TaskProxyGui: improve src/env editing by @unthingable in [https://github.com/supercollider/supercollider/pull/6583](https://github.com/supercollider/supercollider/pull/6583)
- Date improvements by @totalgee in [https://github.com/supercollider/supercollider/pull/3259](https://github.com/supercollider/supercollider/pull/3259)
- scsynth tcp: fixes uninitialized ReplyAddress (issue #6647) by @sonoro1234 in [https://github.com/supercollider/supercollider/pull/6652](https://github.com/supercollider/supercollider/pull/6652)
- Ndef: make clear methods more flexible by @adcxyz in [https://github.com/supercollider/supercollider/pull/6588](https://github.com/supercollider/supercollider/pull/6588)
- Add checkSameRateAsFirstInput to InRange and checkValidInputs to AmpComp by @cdbzb in [https://github.com/supercollider/supercollider/pull/6088](https://github.com/supercollider/supercollider/pull/6088)
- PlotView.sc: ArrayedCollection.plot converts wavetables to Signals before passing them to Plotter by @HotwheelsSisyphus in [https://github.com/supercollider/supercollider/pull/6715](https://github.com/supercollider/supercollider/pull/6715)
- Removed white space in brackets printed on the post window. by @prko in [https://github.com/supercollider/supercollider/pull/6106](https://github.com/supercollider/supercollider/pull/6106)





### Deprecated
Nothing




### Fixed
- complete `binaryValue` implementation for AbstractFunction and UGen by @telephon in [https://github.com/supercollider/supercollider/pull/5941](https://github.com/supercollider/supercollider/pull/5941)
- Avoid writing invalid synthdef files by @mlang in [https://github.com/supercollider/supercollider/pull/5927](https://github.com/supercollider/supercollider/pull/5927)
- `*cueSoundFile` sets path of Buffer by @telephon in [https://github.com/supercollider/supercollider/pull/5937](https://github.com/supercollider/supercollider/pull/5937)
- ContiguousBlockAllocator: Fix 'reserve' bug when addrOffset > 0 by @jamshark70 in [https://github.com/supercollider/supercollider/pull/6768](https://github.com/supercollider/supercollider/pull/6768)
- FunctionList has an empty list by default. by @gorenje in [https://github.com/supercollider/supercollider/pull/5945](https://github.com/supercollider/supercollider/pull/5945)
- find server program on Windows by @dyfer in [https://github.com/supercollider/supercollider/pull/5990](https://github.com/supercollider/supercollider/pull/5990)
- Fix `Pwalk` boundary behavior when using directionPattern for folding by @jamshark70 in [https://github.com/supercollider/supercollider/pull/6587](https://github.com/supercollider/supercollider/pull/6587)
- Fix block allocator 'reserve' for start addresses in the middle of a free range by @jamshark70 in [https://github.com/supercollider/supercollider/pull/6586](https://github.com/supercollider/supercollider/pull/6586)
- MIDIClient init cleans up old connections by @telephon in [https://github.com/supercollider/supercollider/pull/6620](https://github.com/supercollider/supercollider/pull/6620)
- scdoc renderer: use forward slash on Windows by @dyfer in [https://github.com/supercollider/supercollider/pull/6865](https://github.com/supercollider/supercollider/pull/6865)
- Fix wrong behaviour of `lastForWhich` and `lastIndexForWhich` of `Collection`, also add synonym method of them by @OzelotVanilla in [https://github.com/supercollider/supercollider/pull/6665](https://github.com/supercollider/supercollider/pull/6665)
- Correct openOS behaviour on Windows by @prko in [https://github.com/supercollider/supercollider/pull/6880](https://github.com/supercollider/supercollider/pull/6880)
- Remove whitespace from .storeOn .printOn by @dyfer in [https://github.com/supercollider/supercollider/pull/6113](https://github.com/supercollider/supercollider/pull/6113)
- `EnvironmentRedirect` and `LazyEnvir` – call dispatch on `removeAt`. The message `localRemoveAt` can be used to removeAt without calling the dospatch. by @telephon in [https://github.com/supercollider/supercollider/pull/5923](https://github.com/supercollider/supercollider/pull/5923)
- Fix unixCmd quoting on Windows by @dyfer in [https://github.com/supercollider/supercollider/pull/6858](https://github.com/supercollider/supercollider/pull/6858)
- Function:-asBuffer restore doneAction via RecordBuf by @mtmccrea in [https://github.com/supercollider/supercollider/pull/6663](https://github.com/supercollider/supercollider/pull/6663)
- Simplify Function:plot 'dur' redundancy by @jamshark70 in [https://github.com/supercollider/supercollider/pull/6200](https://github.com/supercollider/supercollider/pull/6200)
- MultiOutUGen: better error for non-numeric numChannels arg by @sirlensalot in [https://github.com/supercollider/supercollider/pull/6190](https://github.com/supercollider/supercollider/pull/6190)
- Add option to close subprocesses using killProcessByID by @dyfer in [https://github.com/supercollider/supercollider/pull/6849](https://github.com/supercollider/supercollider/pull/6849)
- Add boundedInsert method to ArrayedCollection and List by @prko in [https://github.com/supercollider/supercollider/pull/6394](https://github.com/supercollider/supercollider/pull/6394)
- Function:-asBuffer, -plot: use sampleRate to infer control rate data, clean/update docs by @mtmccrea in [https://github.com/supercollider/supercollider/pull/6217](https://github.com/supercollider/supercollider/pull/6217)
- Pbindef with a Pbind – fix order of new keys by @telephon in [https://github.com/supercollider/supercollider/pull/6897](https://github.com/supercollider/supercollider/pull/6897)
- when NodeProxy is neutral, rest source pattern by @telephon in [https://github.com/supercollider/supercollider/pull/6223](https://github.com/supercollider/supercollider/pull/6223)
- NodeProxy.buildProxy is always nil outside a SynthDef build process by @telephon in [https://github.com/supercollider/supercollider/pull/6032](https://github.com/supercollider/supercollider/pull/6032) ()
- in Ndef, call proxyspace dispatch explicitly by @telephon in [https://github.com/supercollider/supercollider/pull/5930](https://github.com/supercollider/supercollider/pull/5930)
- QtCollider: sunken inset shadows respect alpha by @elgiano in [https://github.com/supercollider/supercollider/pull/6478](https://github.com/supercollider/supercollider/pull/6478)
- Env:-circle adjustment for UGen initialization fixes by @mtmccrea in [https://github.com/supercollider/supercollider/pull/6183](https://github.com/supercollider/supercollider/pull/6183)
- Plotter: add new plot modes by @mtmccrea in [https://github.com/supercollider/supercollider/pull/6201](https://github.com/supercollider/supercollider/pull/6201)






## sclang

### Added
- add isxdigit definition by @dyfer in [https://github.com/supercollider/supercollider/pull/6504](https://github.com/supercollider/supercollider/pull/6504)
- Use boost program options for sclang CLI options by @capital-G in [https://github.com/supercollider/supercollider/pull/6640](https://github.com/supercollider/supercollider/pull/6640)
- Refactor SC_ComPort, add support for receiving raw UDP socket communication by @scztt in [https://github.com/supercollider/supercollider/pull/5747](https://github.com/supercollider/supercollider/pull/5747)





### Changed
- Now, the interpreter continues to work if the library has not been compiled by @dyfer in [https://github.com/supercollider/supercollider/pull/6727](https://github.com/supercollider/supercollider/pull/6727)
- SCLang, UnitTests: standardise nan & inf printing across platforms by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6867](https://github.com/supercollider/supercollider/pull/6867)
- SCLang: tidy duplicated error message by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6299](https://github.com/supercollider/supercollider/pull/6299)
- Use std::string for set and get environment variables - by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6216](https://github.com/supercollider/supercollider/pull/6216)
- Increase UDP socket buffer size and fallback to 1MB by @xunil-cloud in [https://github.com/supercollider/supercollider/pull/6564](https://github.com/supercollider/supercollider/pull/6564) and [https://github.com/supercollider/supercollider/pull/6989](https://github.com/supercollider/supercollider/pull/6989)
- Adjust touchpad and mouse wheel scrolling by @elgiano in [https://github.com/supercollider/supercollider/pull/7030](https://github.com/supercollider/supercollider/pull/7030)





### Fixed
- Unique method regression and rename variables to something useful by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6747](https://github.com/supercollider/supercollider/pull/6747)
- String literal size limit: Documentation and bugfix by @jamshark70 in [https://github.com/supercollider/supercollider/pull/6415](https://github.com/supercollider/supercollider/pull/6415)
- Cli options flags initialization by @elgiano in [https://github.com/supercollider/supercollider/pull/6773](https://github.com/supercollider/supercollider/pull/6773)
- LinkClock beats/secs conversion traps 'inf' by @jamshark70 in [https://github.com/supercollider/supercollider/pull/6356](https://github.com/supercollider/supercollider/pull/6356)
- Fix SequenceableCollection -unixCmd on Windows by @dyfer in [https://github.com/supercollider/supercollider/pull/6837](https://github.com/supercollider/supercollider/pull/6837)
- sclang: PyrSignal, PyrMathOps: implement pow function for Signals (#6558) by @passyur in [https://github.com/supercollider/supercollider/pull/6659](https://github.com/supercollider/supercollider/pull/6659)
- sclang: warn too many vars by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6891](https://github.com/supercollider/supercollider/pull/6891)
- Add atomic bool const to lockLanguageOrQuit in PyrSched.h by @smoge in [https://github.com/supercollider/supercollider/pull/6229](https://github.com/supercollider/supercollider/pull/6229)
- Fix asio post invocation for `SC_TerminalClient` by @capital-G in [https://github.com/supercollider/supercollider/pull/6590](https://github.com/supercollider/supercollider/pull/6590)
- Add helper for reallocstack and correct objectPerformArgsImpl by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6731](https://github.com/supercollider/supercollider/pull/6731)
- Use fix width integers for `long` and `long long` by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6732](https://github.com/supercollider/supercollider/pull/6732)
- PyrGC: Fix GC segfault caused by uncollected temporary function objects by placing an upper limit on un-scanned objects. by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6261](https://github.com/supercollider/supercollider/pull/6261)
- Assert no uninlined functions in class lib. by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6916](https://github.com/supercollider/supercollider/pull/6916), [https://github.com/supercollider/supercollider/pull/6935](https://github.com/supercollider/supercollider/pull/6935) and [https://github.com/supercollider/supercollider/pull/7062](https://github.com/supercollider/supercollider/pull/7062)
- Implement replace regex using boost by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6213](https://github.com/supercollider/supercollider/pull/6213)
- `slotStrVal` implementation is fixed by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/6156](https://github.com/supercollider/supercollider/pull/6156)
- QtCollider: QcTreeWidget: fix instance methods by @sadguitarius in [https://github.com/supercollider/supercollider/pull/6521](https://github.com/supercollider/supercollider/pull/6521)
- Silence more UDP errors by @dyfer in [https://github.com/supercollider/supercollider/pull/6782](https://github.com/supercollider/supercollider/pull/6782)
- Destroy UDP socket explicitly by @capital-G in [https://github.com/supercollider/supercollider/pull/6551](https://github.com/supercollider/supercollider/pull/6551)
- Update hidapi external library checkout to fix HID on Linux by @bgola in [https://github.com/supercollider/supercollider/pull/6399](https://github.com/supercollider/supercollider/pull/6399)
- fix Windows pathname resolution by @sadguitarius in [https://github.com/supercollider/supercollider/pull/6613](https://github.com/supercollider/supercollider/pull/6613)
- Don't try to free a Volume synth that doesn't exist by @jamshark70 in [https://github.com/supercollider/supercollider/pull/6939](https://github.com/supercollider/supercollider/pull/6939)
- Fix View.setBackgroundImage by @elgiano in [https://github.com/supercollider/supercollider/pull/6970](https://github.com/supercollider/supercollider/pull/6970)






## UGens
See also [UGen-Changelog#Version 3.14](../Guides/UGen-Changelog.md#version-3.14) for a more detailed documentation of changes affecting UGens.


### Added and Changed
- `LevelComp` UGen and a Guide to Level Compensation by @adcxyz in [https://github.com/supercollider/supercollider/pull/6804.](https://github.com/supercollider/supercollider/pull/6804.)
- `Delay1` and `Delay2` got additional arguments: `x1` and - only for Delay2
- `x2`, to control predelay values. Part of [https://github.com/supercollider/supercollider/pull/6110](https://github.com/supercollider/supercollider/pull/6110) by @mtmccrea





### Fixed
- IEnvGen initialization refactored by @mtmccrea in [https://github.com/supercollider/supercollider/pull/6187](https://github.com/supercollider/supercollider/pull/6187)
- EnvGen: fix endtime by @mtmccrea in [https://github.com/supercollider/supercollider/pull/6664](https://github.com/supercollider/supercollider/pull/6664)
- PanAz: fix bug when width is small and negative by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6296](https://github.com/supercollider/supercollider/pull/6296)
- Sweep: apply rate increment after writing to output by @elgiano in [https://github.com/supercollider/supercollider/pull/6822](https://github.com/supercollider/supercollider/pull/6822)
- `ToggleFF` supports input rate != unit rate by @elgiano in [https://github.com/supercollider/supercollider/pull/6760](https://github.com/supercollider/supercollider/pull/6760)
- Remove c cast from CALCSCOPE and fix GVerbs roomsize. by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6320](https://github.com/supercollider/supercollider/pull/6320)
- plugins: SpecPcile output zeros on RTAlloc may fail, ensure clear output on such a failure. by @elgiano in [https://github.com/supercollider/supercollider/pull/6454](https://github.com/supercollider/supercollider/pull/6454)
- Plugin code refactoring and small fixes by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/6681](https://github.com/supercollider/supercollider/pull/6681)





### Fix UGen initialization sample
- EnvGen: fix initialization by @mtmccrea in [https://github.com/supercollider/supercollider/pull/6175](https://github.com/supercollider/supercollider/pull/6175)
- TDelay: fix initialization sample by @elgiano in [https://github.com/supercollider/supercollider/pull/6832](https://github.com/supercollider/supercollider/pull/6832)
- Fix UGen initialization: LFUGens pt. 1/3, Trig, Trig1 by @mtmccrea in [https://github.com/supercollider/supercollider/pull/6035](https://github.com/supercollider/supercollider/pull/6035)
- Fix UGen initialization: LFUGens pt. 2/3 by @mtmccrea in [https://github.com/supercollider/supercollider/pull/6172](https://github.com/supercollider/supercollider/pull/6172)
- Fix UGen initialization: Delay1, Delay2 by @mtmccrea in [https://github.com/supercollider/supercollider/pull/6110](https://github.com/supercollider/supercollider/pull/6110)
- Decay, Decay2: fix UGen initialization by @mtmccrea in [https://github.com/supercollider/supercollider/pull/6194](https://github.com/supercollider/supercollider/pull/6194)
- TriggerUGens standardize init sample by @elgiano in [https://github.com/supercollider/supercollider/pull/6810](https://github.com/supercollider/supercollider/pull/6810)
- TriggerUGens: fix initialization sample by @elgiano in [https://github.com/supercollider/supercollider/pull/6816](https://github.com/supercollider/supercollider/pull/6816)
- Phasor: fix init sample: don't ignore trig on first sample by @elgiano in [https://github.com/supercollider/supercollider/pull/6833](https://github.com/supercollider/supercollider/pull/6833)






## scsynth and supernova

### Added
- Buffer: set user-defined sampleRate on alloc, add /b_setSampleRate by @tremblap in [https://github.com/supercollider/supercollider/pull/6800](https://github.com/supercollider/supercollider/pull/6800)
- CoreAudio/macOS: try setting sample rate of output device when input and output sample rates are mismatched by @dyfer in [https://github.com/supercollider/supercollider/pull/6717](https://github.com/supercollider/supercollider/pull/6717)
- Sync server volume between multiple clients by @adcxyz in [https://github.com/supercollider/supercollider/pull/6313](https://github.com/supercollider/supercollider/pull/6313)
- Add a new line after audio device name when booting server by @prko in [https://github.com/supercollider/supercollider/pull/6775](https://github.com/supercollider/supercollider/pull/6775)
- Change the style of path in Windows by updating ScIDE.sc by @prko in [https://github.com/supercollider/supercollider/pull/6683](https://github.com/supercollider/supercollider/pull/6683)
- Add check before installing Quark dependencies by @cdbzb in [https://github.com/supercollider/supercollider/pull/6163](https://github.com/supercollider/supercollider/pull/6163)
- add /rtMemoryStatus cmd for debugging by @elgiano in [https://github.com/supercollider/supercollider/pull/6467](https://github.com/supercollider/supercollider/pull/6467)





### Changed
- Add cmdName to error when /cmd not found by @elgiano in [https://github.com/supercollider/supercollider/pull/6499](https://github.com/supercollider/supercollider/pull/6499)
- registerUnit: make sure that the UGen class is not polymorphic by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/6147](https://github.com/supercollider/supercollider/pull/6147)
- InlineUnaryOp.h: increase precision of constants by @dyfer in [https://github.com/supercollider/supercollider/pull/6711](https://github.com/supercollider/supercollider/pull/6711)
- CoreAudio backend: don't try to query input device when numInputBusChannels = 0 by @dyfer in [https://github.com/supercollider/supercollider/pull/6716](https://github.com/supercollider/supercollider/pull/6716)
- portaudio/WASAPI: enable automatic sample rate conversion by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/6899](https://github.com/supercollider/supercollider/pull/6899) / fix PortAudio hostAPI stream info (Win32) by @dyfer in [https://github.com/supercollider/supercollider/pull/6905](https://github.com/supercollider/supercollider/pull/6905)
- Increase UDP socket buffer size and fallback to 1MB by @xunil-cloud in [https://github.com/supercollider/supercollider/pull/6564](https://github.com/supercollider/supercollider/pull/6564) and [https://github.com/supercollider/supercollider/pull/6989](https://github.com/supercollider/supercollider/pull/6989)
- Use WASAPI as default backend on Windows by @dyfer in [https://github.com/supercollider/supercollider/pull/6994](https://github.com/supercollider/supercollider/pull/6994) and [https://github.com/supercollider/supercollider/pull/7051](https://github.com/supercollider/supercollider/pull/7051)





### Fixed
- Improve/fix plugin unloading by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/6191](https://github.com/supercollider/supercollider/pull/6191)
- Supernova: catch exceptions in NRT synthesis by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/6748](https://github.com/supercollider/supercollider/pull/6748)
- Fix 'incompatible-pointer-types' warning/error for portmidi by @xunil-cloud in [https://github.com/supercollider/supercollider/pull/6556](https://github.com/supercollider/supercollider/pull/6556)
- scsynth/supernova: refactor SC_ServerBootDelayWarning by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/6758](https://github.com/supercollider/supercollider/pull/6758)
- scsynth tcp: fixes uninitialized ReplyAddress (issue #6647) by @sonoro1234 in [https://github.com/supercollider/supercollider/pull/6652](https://github.com/supercollider/supercollider/pull/6652)
- scsynth/supernova: fix thread priorities by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/6043](https://github.com/supercollider/supercollider/pull/6043)
- Supernova: thread affinity fixes/improvements by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/5618](https://github.com/supercollider/supercollider/pull/5618)
- Supernova on windows fixes of error with infamous exit code -1073741676 by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/6402](https://github.com/supercollider/supercollider/pull/6402)
- synthdef load needs binary on windows by @sonoro1234 in [https://github.com/supercollider/supercollider/pull/6612](https://github.com/supercollider/supercollider/pull/6612)






## plugin_interface

### Added
- `PluginUnload` macro exports a function that is called when the library is deinitialized, right before it is unloaded. This is only required in rare cases, typically for resource cleanup that cannot be safely done in a global object destructor. ([https://github.com/supercollider/supercollider/pull/6191](https://github.com/supercollider/supercollider/pull/6191) by @Spacechild1)
- `FULLSAMPLEDUR` macro, and `SC_PlugIn::fullSampleDur()` method: return the reciprocal of server sampleRate. ([https://github.com/supercollider/supercollider/pull/6147](https://github.com/supercollider/supercollider/pull/6147) by @Spacechild1)





### Changed
- increased precision of constants for conversion methods `sc_midicps`, `sc_cpsmidi`, `sc_midiratio`, `sc_cpsoct`, `sc_ampdb` ([https://github.com/supercollider/supercollider/pull/6711](https://github.com/supercollider/supercollider/pull/6711) by @dyfer)
- `registerUnit` now has a static assert that blocks polymorphic classes. That is, calling `registerUnit` with a class that has virtual methods will result in a compile-time error ([https://github.com/supercollider/supercollider/pull/6147](https://github.com/supercollider/supercollider/pull/6147) by @Spacechild1)





### Fixed
- `CALCSLOPE` macro: replaced decltype C cast with static_cast. Fixes undefined behavior when passing array items, e.g `CALCSLOPE(x[0], x[1])` ([https://github.com/supercollider/supercollider/pull/6320](https://github.com/supercollider/supercollider/pull/6320) by @JordanHendersonMusic)
- `ClearUnitOnMemFailed` now correctly clears output buffers before returning. ([https://github.com/supercollider/supercollider/pull/6690](https://github.com/supercollider/supercollider/pull/6690) by @Spacechild1)






## ScIDE

### Added
- Add monokai theme by @capital-G in [https://github.com/supercollider/supercollider/pull/6561](https://github.com/supercollider/supercollider/pull/6561)
- CSS Themes for docs by @capital-G in [https://github.com/supercollider/supercollider/pull/6095](https://github.com/supercollider/supercollider/pull/6095)
- Make status bar themed by @capital-G in [https://github.com/supercollider/supercollider/pull/6838](https://github.com/supercollider/supercollider/pull/6838) and [https://github.com/supercollider/supercollider/pull/7033](https://github.com/supercollider/supercollider/pull/7033)
- replace "Monospace" with system monospace font by @capital-G in [https://github.com/supercollider/supercollider/pull/6329](https://github.com/supercollider/supercollider/pull/6329)
- Document.save method by @muellmusik in [https://github.com/supercollider/supercollider/pull/4696](https://github.com/supercollider/supercollider/pull/4696)
- Use tab to switch between documents by @capital-G in [https://github.com/supercollider/supercollider/pull/6554](https://github.com/supercollider/supercollider/pull/6554)
- Add basic zoom via touchpad gesture by @capital-G in [https://github.com/supercollider/supercollider/pull/6563](https://github.com/supercollider/supercollider/pull/6563)
- Preferences: add a button to restart sclang after config change by @dyfer in [https://github.com/supercollider/supercollider/pull/6924](https://github.com/supercollider/supercollider/pull/6924)
- Preferences panel now warns to reboot language when switching language config by @dyfer in [https://github.com/supercollider/supercollider/pull/6818](https://github.com/supercollider/supercollider/pull/6818)
- Add formula support for SCDoc via kaTeX by @capital-G in [https://github.com/supercollider/supercollider/pull/6317](https://github.com/supercollider/supercollider/pull/6317)
- Help browser: add copy icons in schelp examples by @paum3 in [https://github.com/supercollider/supercollider/pull/6870](https://github.com/supercollider/supercollider/pull/6870)
- Help browser: now shows correct position when clicking on generic method name in table of content by @prko in [https://github.com/supercollider/supercollider/pull/6280](https://github.com/supercollider/supercollider/pull/6280)
- Add line number switch to SCDoc theme settings by @capital-G in [https://github.com/supercollider/supercollider/pull/6854](https://github.com/supercollider/supercollider/pull/6854)





### Changed
- Disable IDE menu bar icons on macOS by @capital-G in [https://github.com/supercollider/supercollider/pull/6540](https://github.com/supercollider/supercollider/pull/6540)
- Post Window: clear button by @SimonDeplat in [https://github.com/supercollider/supercollider/pull/6123](https://github.com/supercollider/supercollider/pull/6123)
- Do not display setting menu icons on macOS by @capital-G in [https://github.com/supercollider/supercollider/pull/6809](https://github.com/supercollider/supercollider/pull/6809)
- Minor improvements for monokai theme by @capital-G in [https://github.com/supercollider/supercollider/pull/6808](https://github.com/supercollider/supercollider/pull/6808)
- Make doc themes persistent by @capital-G in [https://github.com/supercollider/supercollider/pull/6812](https://github.com/supercollider/supercollider/pull/6812)
- Automatic indentation: do not change indentation within multiline comments by @capital-G in [https://github.com/supercollider/supercollider/pull/6546](https://github.com/supercollider/supercollider/pull/6546)





### Fixed
- Fix failing to open recent files if mnemonic is enabled by @sonata-chen in [https://github.com/supercollider/supercollider/pull/6450](https://github.com/supercollider/supercollider/pull/6450)
- Document.string_ : fix default args by @adcxyz in [https://github.com/supercollider/supercollider/pull/6756](https://github.com/supercollider/supercollider/pull/6756)
- Fix double invocation of unsaved documents dialog upon quitting by @capital-G in [https://github.com/supercollider/supercollider/pull/6609](https://github.com/supercollider/supercollider/pull/6609)
- IDE: fix sclang config file dialog behavior by @dyfer in [https://github.com/supercollider/supercollider/pull/6817](https://github.com/supercollider/supercollider/pull/6817)
- Help browser: fix navigation by @paum3 in [https://github.com/supercollider/supercollider/pull/6158](https://github.com/supercollider/supercollider/pull/6158)
- Fix SCDocs assets caching by @capital-G in [https://github.com/supercollider/supercollider/pull/6627](https://github.com/supercollider/supercollider/pull/6627)
- Add `scroll-margin-top` to fix scrolling to anchor by @capital-G in [https://github.com/supercollider/supercollider/pull/6847](https://github.com/supercollider/supercollider/pull/6847)
- Fix classtree image path by @capital-G in [https://github.com/supercollider/supercollider/pull/6868](https://github.com/supercollider/supercollider/pull/6868)
- Fix docmap link for classes overview by @capital-G in [https://github.com/supercollider/supercollider/pull/6866](https://github.com/supercollider/supercollider/pull/6866)
- Fix the `custom.css` path in search.html by @prko in [https://github.com/supercollider/supercollider/pull/6875](https://github.com/supercollider/supercollider/pull/6875)
- Disable redrawing lang status box on theme change by @capital-G in [https://github.com/supercollider/supercollider/pull/6873](https://github.com/supercollider/supercollider/pull/6873)
- redraw status bar on applySettings by @elgiano in [https://github.com/supercollider/supercollider/pull/6878](https://github.com/supercollider/supercollider/pull/6878)
- IDE<->sclang Document fixes by @dyfer in [https://github.com/supercollider/supercollider/pull/6827](https://github.com/supercollider/supercollider/pull/6827)
- HelpBrowser fix ambiguous shortcuts by @elgiano in [https://github.com/supercollider/supercollider/pull/6762](https://github.com/supercollider/supercollider/pull/6762)
- scide: audio_status_box: init colors before widgets by @elgiano in [https://github.com/supercollider/supercollider/pull/6892](https://github.com/supercollider/supercollider/pull/6892)
- scide style.cpp: fix icon sizes on tab bar and help toolbar by @sadguitarius in [https://github.com/supercollider/supercollider/pull/6519](https://github.com/supercollider/supercollider/pull/6519)
- Fix doc icon position by @capital-G in [https://github.com/supercollider/supercollider/pull/6348](https://github.com/supercollider/supercollider/pull/6348)
- QtCollider: Fix touchpad mousewheel event scaling by @jpburstrom in [https://github.com/supercollider/supercollider/pull/6575](https://github.com/supercollider/supercollider/pull/6575)
- IDE Document should set path before autorun by @jamshark70 in [https://github.com/supercollider/supercollider/pull/6137](https://github.com/supercollider/supercollider/pull/6137)
- Fix crash on some Wayland configurations by @dyfer in [https://github.com/supercollider/supercollider/pull/7036](https://github.com/supercollider/supercollider/pull/7036)






## Examples
- "séminaire musical" improved, added "intonation" and "counts" comprehension tests by @telephon in [https://github.com/supercollider/supercollider/pull/6908](https://github.com/supercollider/supercollider/pull/6908)




## Other changes
- Fix boost thread on clang17 by @capital-G in [https://github.com/supercollider/supercollider/pull/6733](https://github.com/supercollider/supercollider/pull/6733)
- Include cassert import for clang 15 by @capital-G in [https://github.com/supercollider/supercollider/pull/6487](https://github.com/supercollider/supercollider/pull/6487)
- Update hidapi by @xunil-cloud in [https://github.com/supercollider/supercollider/pull/6542](https://github.com/supercollider/supercollider/pull/6542)
- Add VS Code IDE settings by @capital-G in [https://github.com/supercollider/supercollider/pull/6351](https://github.com/supercollider/supercollider/pull/6351)
- Update Ableton Link submodule to version 3.0.6 by @dyfer in [https://github.com/supercollider/supercollider/pull/5416](https://github.com/supercollider/supercollider/pull/5416)
- Find jack using cmake's FindPkgConfig by @dvzrv in [https://github.com/supercollider/supercollider/pull/5680](https://github.com/supercollider/supercollider/pull/5680)
- Update CMakeLists.txt replace deprecated commands by @smoge in [https://github.com/supercollider/supercollider/pull/6326](https://github.com/supercollider/supercollider/pull/6326)
- Patch yaml-cpp for cmake 4 by @dyfer in [https://github.com/supercollider/supercollider/pull/6700](https://github.com/supercollider/supercollider/pull/6700)
- Update hidapi by @dyfer in [https://github.com/supercollider/supercollider/pull/6708](https://github.com/supercollider/supercollider/pull/6708)
- Convert emacs and vim to an opt-in build flag on linux by @capital-G in [https://github.com/supercollider/supercollider/pull/6835](https://github.com/supercollider/supercollider/pull/6835)
- CMakeLists: only enable SSE on x86 variants by @Xeonacid in [https://github.com/supercollider/supercollider/pull/6116](https://github.com/supercollider/supercollider/pull/6116)
- Upgrade to boost 1.86 by @capital-G in [https://github.com/supercollider/supercollider/pull/6477](https://github.com/supercollider/supercollider/pull/6477)
- Boost 1.87 support by @capital-G in [https://github.com/supercollider/supercollider/pull/6576](https://github.com/supercollider/supercollider/pull/6576)
- Switch Linux Clang to use libstdc++ by @dyfer in [https://github.com/supercollider/supercollider/pull/6133](https://github.com/supercollider/supercollider/pull/6133)
- Remove qt5compat by @dyfer in [https://github.com/supercollider/supercollider/pull/6524](https://github.com/supercollider/supercollider/pull/6524)
- QT: remove deprecations for QT 5.15 by @dyfer in [https://github.com/supercollider/supercollider/pull/6464](https://github.com/supercollider/supercollider/pull/6464)
- CI: run ctests with linux build by @JordanHendersonMusic in [https://github.com/supercollider/supercollider/pull/6896](https://github.com/supercollider/supercollider/pull/6896)
- cmake: repair windows resource compiling by @sonoro1234 in [https://github.com/supercollider/supercollider/pull/6653](https://github.com/supercollider/supercollider/pull/6653)
- Migrate to Qt6 by @dyfer in [https://github.com/supercollider/supercollider/pull/6475](https://github.com/supercollider/supercollider/pull/6475)
- CMake: fix qt6 detection by @dyfer in [https://github.com/supercollider/supercollider/pull/6511](https://github.com/supercollider/supercollider/pull/6511)
- QMetaType fix for Qt5 by @dyfer in [https://github.com/supercollider/supercollider/pull/6570](https://github.com/supercollider/supercollider/pull/6570)
- Fix compatibility with CMake4 (portaudio) by @dyfer in [https://github.com/supercollider/supercollider/pull/6701](https://github.com/supercollider/supercollider/pull/6701)
- build: install: add an AppStream metainfo file by @djiamnot in [https://github.com/supercollider/supercollider/pull/6393](https://github.com/supercollider/supercollider/pull/6393)
- correct .editorconfig syntax by @xunil-cloud in [https://github.com/supercollider/supercollider/pull/6485](https://github.com/supercollider/supercollider/pull/6485)
- Topic/improve help modularity by @scztt in [https://github.com/supercollider/supercollider/pull/6011](https://github.com/supercollider/supercollider/pull/6011)
- Run testsuite directly by @dyfer in [https://github.com/supercollider/supercollider/pull/6003](https://github.com/supercollider/supercollider/pull/6003)
- Add pre commit by @capital-G in [https://github.com/supercollider/supercollider/pull/6319](https://github.com/supercollider/supercollider/pull/6319)
- add `FULL_CHECK` flag for clang-format by @capital-G in [https://github.com/supercollider/supercollider/pull/6344](https://github.com/supercollider/supercollider/pull/6344)
- Add `.git-blame-ignore-revs` file by @capital-G in [https://github.com/supercollider/supercollider/pull/6350](https://github.com/supercollider/supercollider/pull/6350)
- Replace `boost::filesystem` with `std::filesystem` by @capital-G in [https://github.com/supercollider/supercollider/pull/6331](https://github.com/supercollider/supercollider/pull/6331)
- Remove gedit plugin sced by @capital-G in [https://github.com/supercollider/supercollider/pull/6337](https://github.com/supercollider/supercollider/pull/6337)
- [Windows] switch system calls to UTF-16 by @dyfer in [https://github.com/supercollider/supercollider/pull/6124](https://github.com/supercollider/supercollider/pull/6124)
- Fix for GCC 14 by @Spacechild1 in [https://github.com/supercollider/supercollider/pull/6436](https://github.com/supercollider/supercollider/pull/6436)
- Removed beaglebone platform by @redFrik in [https://github.com/supercollider/supercollider/pull/6751](https://github.com/supercollider/supercollider/pull/6751)
- Bump hidapi to cmake 3.12 by @capital-G in [https://github.com/supercollider/supercollider/pull/6954](https://github.com/supercollider/supercollider/pull/6954)
- Add macOS universal build by @dyfer in [https://github.com/supercollider/supercollider/pull/6996](https://github.com/supercollider/supercollider/pull/6996)




## Documentation changes
@SimonDeplat, @prko, @JordanHendersonMusic, @martindupras, @jamshark70, @mlang, @tedmoore, @capital-G, @telephon, @HotwheelsSisyphus, @OzelotVanilla, @passyur, @mtmccrea, @cdbzb, @redFrik, @juergenrmayer, @paum3, @miczac, @madskjeldgaard, @carltesta, @redFrik, @Shu-AFK, @elifieldsteel, @alexyuwen, @mxw, @wortsampler



## Tests
@telephon, @jamshark70, @elgiano, @mtmccrea, @JordanHendersonMusic, @capital-G



## CI changes
@dyfer, @capital-G, @elgiano, @scztt, @silvanocerza



