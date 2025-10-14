# News in 3.7

*A summary of news in SC 3.7*

**Categories:** News

**Related:** [News-3_6](../Guides/News-3_6.md), [News-3_5](../Guides/News-3_5.md), [Debugging-tips](../Guides/Debugging-tips.md)

In addition to the new features and changes described here, there are **many bugfixes and interesting improvements**, a full list of which can be found in CHANGELOG.md.

## SuperCollider IDE
- Menu entries for Recording, scope and server inspection
- Modify and query IDE documents from sclang
- Support for the Atom text editor
- Integrated help with auto-completion
- Autosave feature




## SuperCollider Language
- Improved [Quark](../Classes/Quark.md) system and many new interesting Quarks.
- [TempoClock#-beats](../Classes/TempoClock.md#-beats) can be set.
- An interface for key-value-pairs, see [Key-Value-Pairs](../Reference/Key-Value-Pairs.md)
- Refactored JITLib, see [JITLibChanges3.7](../Other/JITLibChanges3.7.md) (in particular dynamic channel expansion).
- [QuartzComposerView](../Classes/QuartzComposerView.md)



### External Interfacing
There is an entirely new HID (Human Interface Device) implementation: see [Working_with_HID](../Guides/Working_with_HID.md) that works cross platform (Linux and macOS thus far). This deprecates the GeneralHID interface. Also the [LID](../Classes/LID.md) interface has been updated to match the API of the new HID implementation.




### New methods and classes
- [Collection#-collectCopy](../Classes/Collection.md#-collectcopy), [Collection#-collectInPlace](../Classes/Collection.md#-collectinplace)
- [SimpleNumber#-lcm](../Classes/SimpleNumber.md#-lcm) and [SimpleNumber#-gcd](../Classes/SimpleNumber.md#-gcd) have consistent interpretations of negative values and zero.
- [Dictionary#-embedInStream](../Classes/Dictionary.md#-embedinstream) can be customized from within the dictionary.
- [Server#*remote](../Classes/Server.md#*remote) Create a new Server instance corresponding to a server app running on a separate machine.





### Deprecated classes and methods
- TuningInfo
- ScaleInfo
- Proutine (use Prout instead)
- Document style api - set postColor background etc.
- Date-bootTime
- Platform-getMouseCoords (use GUI.cursorPosition instead)






## SuperCollider Server
Apart from UDP, the TCP-protocol is now supported.

When mapping controls of synths to busses, their number of channels is limited to the number of control channels, avoiding a "spill-over" of mappings.


### List of new UGens
- NodeID (UGen that returns the current node id)
- [Dconst](../Classes/Dconst.md)





### Improved or corrected behavior
- [LinXFade2](../Classes/LinXFade2.md) (correct fading direction)
- [LFPulse](../Classes/LFPulse.md) (when width = 0.5, return exactly as many 0 as 1)
- [TrigControl](../Classes/TrigControl.md) is now independent of synth order, like [Control](../Classes/Control.md).
- [TRand](../Classes/TRand.md), [TExpRand](../Classes/TExpRand.md), [TIRand](../Classes/TIRand.md) (can operate at audio rate)
- [Env#*new](../Classes/Env.md#*new) accepts a new `step2` shape, which steps to a value at the end of a shape
- [UGen#-curvelin](../Classes/UGen.md#-curvelin) is now inverse of [UGen#-lincurve](../Classes/UGen.md#-lincurve)
- [Server#-record](../Classes/Server.md#-record) correctly closes short files
- In combinations of demand-ugens: Instances of PV_Copy are added automatically where necessary for parallel processing





### More operators work uniformly across sclang and scserver
The following operators have been added as UGens and work the same as in sclang:

| unary operators | `rand, rand2, linrand, bilinrand, sum3rand, coin` | 
| --- | --- || binary operators | `lcm, gcd, rrand, exprand` | 
See [Operators](../Overviews/Operators.md)





## Known Issues
While much has improved and many bugs from 3.6 have been fixed, there are still many known issues. For a complete list see: [https://github.com/supercollider/supercollider/issues/](https://github.com/supercollider/supercollider/issues/)

Please do not hesitate to add new issues you find to the [issue tracker](https://github.com/supercollider/supercollider/issues) or mention them on the [mailing list](http://www.birmingham.ac.uk/facilities/ea-studios/research/supercollider/mailinglist.aspx)



