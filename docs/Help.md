# Help

*Documentation home*

**Categories:** Help


> **Note:** [News in SuperCollider version 3.14](Guides/News-3_14.md)



## An introductory overview
*SuperCollider* is a cross-platform environment for audio synthesis and algorithmic composition used by musicians, artists and researchers working with sound. It can [be installed and run on Linux, macOS and Windows](https://supercollider.github.io/downloads.html), as well as microcomputers such as [Raspberry Pi](https://github.com/supercollider/supercollider/blob/develop/README_RASPBERRY_PI.md) or [Bela](https://github.com/supercollider/supercollider/blob/develop/README_BELA.md). *SuperCollider* [was originally developed](https://www.audiosynth.com) by James McCartney and [is now distributed](https://supercollider.github.io/) as Free Software under the GNU General Public License. It [is maintained and developed](https://github.com/supercollider/supercollider) by an active and enthusiastic community.

*SuperCollider* consists of three main components:


**•  [scsynth](Classes/Server.md#switching-the-server-application) — A real-time audio engine implemented as a [server](Classes/Server.md).**
: The default server is [scsynth](Classes/Server.md#switching-the-server-application). SuperCollider also includes an alternative implementation of scsynth called [supernova](Classes/Server.md#switching-the-server-application) which has multi-threading support to fully exploit the potential of multi-core CPUs.

**•  [sclang](Classes/Main.md#.thisprocess) — A text-based programming language and interpreter that acts as a client to the server.**
: *sclang* controls audio synthesis processes on the server and offers an interactive programming environment for [live coding](Overviews/JITLib.md), an extensive library for creating [patterns](Tutorials/A-Practical-Guide/PG_01_Introduction.md) and a library of [scales and modes](Classes/Scale.md) from various cultures. Creating [processes](Tutorials/Getting-Started/15-Sequencing-with-Routines-and-Tasks.md) that unfold over time is straightforward in *sclang*. It also provides all the essential features of a graphical user interface ([GUI](Guides/GUI-Introduction.md)) that can be used to create custom user interfaces, data visualization, and animations. With support for [MIDI](Guides/UsingMIDI.md), [OSC](Guides/OSC_communication.md), [HID](Guides/Working_with_HID.md), and [Serial Port](Classes/SerialPort.md), *sclang* can be easily interfaced with local and networked hardware and software.| Although sclang is the native language and client for the server, there are also several client implementations in other programming languages, such as [Python (via Supriya API)](https://supriya-project.github.io/supriya/), [JavaScript](https://crucialfelix.github.io/supercolliderjs/), [Haskell](https://rohandrape.net/?t=hsc3), or [Scala](https://codeberg.org/sciss/ScalaCollider). | 
| --- |

**•  [ScIDE](Classes/ScIDE.md) — A dedicated editor for SuperCollider with an integrated help system.**
: The SuperCollider Integrated Development Environment ([IDE](Guides/SCIde.md)) allows you to start writing code right out of the box. Community members also maintain sclang integration with other popular IDEs. The full list of support editors is available at [https://github.com/supercollider/supercollider/wiki/Systems-interfacing-with-SC#editors](https://github.com/supercollider/supercollider/wiki/Systems-interfacing-with-SC#editors)



The server and client [communicate](Guides/ClientVsServer.md) via Open Sound Control ([OSC](http://opensoundcontrol.org/)), allowing SuperCollider to run on a single machine or on multiple machines over a network. Thanks to this client/server architecture, it is possible for [multiple clients](Guides/MultiClient_Setups.md) to connect and control what is happening on the server. Users can also control the audio server directly with any OSC-enabled program by using the [NodeMessaging](Guides/NodeMessaging.md) protocol.

An extensive library of Unit Generators—the building blocks of audio synthesis networks—are included with SuperCollider. Users may optionally extend this core library with the [sc3-plugins](https://github.com/supercollider/sc3-plugins) suite of UGens. Additionally, there are many of user-developed language extensions, called [Quarks](Classes/Quarks.md), to further extend the functionality of SuperCollider. Quarks can be browsed in the distribution [repository](https://github.com/supercollider-quarks/quarks) where users can submit their own Quarks for distribution.



## Getting started
These are useful starting points for getting help on SuperCollider:


### Introduction & Reference Materials
- [Getting Started tutorial series](Tutorials/Getting-Started/00-Getting-Started-With-SC.md)
- [Glossary](Guides/Glossary.md)
- [More On Getting Help](Guides/More-On-Getting-Help.md):Using Help Files effectively and inspecting class definition files to build more understanding
- [All tutorials](Browse.html.md#tutorials):Index of all help files categorized under *Tutorials*
- [Common Errors and FAQ](Guides/UserFAQ.md)
- SuperCollider examples folder:
```
Platform.exampleDir.openOS 
// Hold down the Shift key and press the Enter key to open the "SuperCollider examples folder".
```







### Getting Sound

#### Generating Sound from Scratch
- [Function#-play](Classes/Function.md#-play)
- [Function#-scope](Classes/Function.md#-scope)
- [Function#-freqscope](Classes/Function.md#-freqscope)
- [Event#-play](Classes/Event.md#-play)





#### Defining and Instantiating Synths
- [SynthDef](Classes/SynthDef.md)
- [Synth](Classes/Synth.md)
- [Node](Classes/Node.md)
- [Group](Classes/Group.md)
- [Bus](Classes/Bus.md)





#### Live Coding Essentials
- [Ndef](Classes/Ndef.md)
- [Tdef](Classes/Tdef.md)
- [Task](Classes/Task.md)





#### Building Musical Patterns
- [Pdef](Classes/Pdef.md)
- [Pbind](Classes/Pbind.md)








## Diving deeper
These are helpful for gaining a better grasp of SuperCollider:


### Debugging
1. [How-to-Use-the-Interpreter](Guides/How-to-Use-the-Interpreter.md)
2. [Understanding-Errors](Guides/Understanding-Errors.md)
3. [Debugging-tips](Guides/Debugging-tips.md)
4. [Tracing-Processes](Guides/Tracing-Processes.md)
5. [Internal-Snooping](Guides/Internal-Snooping.md)
6. [HID_permissions](Guides/HID_permissions.md)
7. [LID_permissions](Guides/LID_permissions.md)





### Language Reference
Guides on writing code in the SuperCollider language (`sclang`).

1. [Comments](Reference/Comments.md)
2. [Expression-Sequence](Reference/Expression-Sequence.md)
3. [Intro-to-Objects](Guides/Intro-to-Objects.md)
4. [Classes](Reference/Classes.md)
5. [Messages](Reference/Messages.md)
6. [Polymorphism](Guides/Polymorphism.md)
7. [Assignment](Reference/Assignment.md)
8. [Scope](Reference/Scope.md)
9. [Functions](Reference/Functions.md)
10. [Conditional-Execution](Reference/Conditional-Execution.md)
11. [Syntax-Shortcuts](Reference/Syntax-Shortcuts.md)
12. [SymbolicNotations](Overviews/SymbolicNotations.md)
13. [Adverbs](Reference/Adverbs.md)
14. [Key-Value-Pairs](Reference/Key-Value-Pairs.md)
15. [Literals](Reference/Literals.md)
16. [Partial-Application](Reference/Partial-Application.md)
17. [Working with Multi-dimensional Arrays (J concepts in SC)](Guides/J-concepts-in-SC.md)
18. [ListComprehensions](Guides/ListComprehensions.md)
19. [Tour-of-Special-Functions](Guides/Tour-of-Special-Functions.md)





### Overviews
Guides and Tutorials on broad topics:

1. [AudioDeviceSelection](Reference/AudioDeviceSelection.md)
2. [Tour_of_UGens](Guides/Tour_of_UGens.md)
3. [Operators](Overviews/Operators.md)
4. [Collections](Overviews/Collections.md)
5. [GenericCollectors](Overviews/GenericCollectors.md)
6. [Randomness](Guides/Randomness.md)
7. [Streams](Overviews/Streams.md)
8. [Event_types](Overviews/Event_types.md)
9. [GUI-Introduction](Guides/GUI-Introduction.md)
10. [GUI-Classes](Overviews/GUI-Classes.md)
11. [GUI-Layout-Management](Guides/GUI-Layout-Management.md)
12. [FFT-Overview](Guides/FFT-Overview.md)
13. [Non-Realtime-Synthesis](Guides/Non-Realtime-Synthesis.md)





### Architecture
Guides and References focused on the important relationship between the Client and Server.

1. [ClientVsServer](Guides/ClientVsServer.md)
2. [UGens-and-Synths](Guides/UGens-and-Synths.md)
3. [NodeMessaging](Guides/NodeMessaging.md)
4. [Multichannel-Expansion](Guides/Multichannel-Expansion.md)
5. [Order-of-execution](Guides/Order-of-execution.md)
6. [default_group](Reference/default_group.md)
7. [Server-Guide](Guides/Server-Guide.md)
8. [Server-Architecture](Reference/Server-Architecture.md)
9. [MultiClient_Setups](Guides/MultiClient_Setups.md)
10. [Server_Tutorial](Tutorials/Server_Tutorial.md)
11. [Server-Command-Reference](Reference/Server-Command-Reference.md)
12. [ServerTiming](Guides/ServerTiming.md)
13. [Bundled-Messages](Guides/Bundled-Messages.md)
14. [Synth-Definition-File-Format](Reference/Synth-Definition-File-Format.md)





### Extending SC
If there are things you want to do that can't be achieved using SuperCollider as it exists, you can extend SuperCollider's capabilities.

1. [StartupFile](Reference/StartupFile.md)
2. [UsingExtensions](Guides/UsingExtensions.md)
3. [UsingQuarks](Guides/UsingQuarks.md)
4. [WritingClasses](Guides/WritingClasses.md)
5. [standalones](Guides/standalones.md)
6. [WritingTests](Guides/WritingTests.md)
7. [WritingUGens](Guides/WritingUGens.md)
8. [ServerPluginAPI](Reference/ServerPluginAPI.md)
9. [WritingPrimitives](Guides/WritingPrimitives.md)





### Sharing your work

#### Share Music
- [Music on scsynth.org](https://scsynth.org/c/music)







#### Share Code
- [http://sccode.org/](http://sccode.org/)
- [Code Review on scsynth.org](https://scsynth.org/c/questions/code-review)
- [Code Tennis on scsynth.org](https://scsynth.org/c/music/code-tennis)
- [Style Guide: SuperCollider Code (for sclang)](https://github.com/supercollider/supercollider/wiki/Style-Guidelines:-SuperCollider)







### Contributing to SC

#### Discussing
- [Development on scsynth.org](https://scsynth.org/c/development)





#### Help Documents
- [WritingHelp](Guides/WritingHelp.md)
- [SCDocSyntax](Reference/SCDocSyntax.md)
- [Style Guide: SuperCollider Help Files](https://github.com/supercollider/supercollider/wiki/Style-Guidelines:-SCDocs)





#### Developing
- [SuperCollider on GitHub](https://github.com/supercollider/supercollider)
- [Style Guide: SuperCollider C++ Code (for scsynth)](https://github.com/supercollider/supercollider/wiki/Style-Guidelines:-Cpp)







### For more information
- [SuperCollider Wiki](https://github.com/supercollider/supercollider/wiki)
- [SuperCollider Forum](https://scsynth.org)






## Licensing
SuperCollider is free software published under the GPL: [Licensing](Other/Licensing.md).

These help files are published under the Creative Commons CC-BY-SA-3 license: [HelpDocsLicensing](Other/HelpDocsLicensing.md).



