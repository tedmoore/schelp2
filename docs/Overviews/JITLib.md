# JITLib

*An overview of the Just In Time programming library*

**Categories:** JITLib, Tutorials>JITLib, Live Coding


## Introduction
*"Passenger to taxi driver: take me to number 37. I'll give you the street name when we are there."*> *An austrian math teacher's joke*

Disclaimer: there is no time, really; punctuality, however, is your personal responsibility.

*Just in time programming* (or: *conversational programming, live coding*> *For Live Coding see: [http://toplap.org](http://toplap.org)**, on-the fly-programming, interactive programming*) is a paradigm that includes the programming activity in the program's operation. Here, a program is not taken as a tool that is made first to be productive later, but instead as a dynamic construction process of description and conversation. Writing code becomes an integral part of musical or experimental practice.

 Being a dynamic programming language, SuperCollider provides several possibilities for modification of a running program - this library extends, unifies and develops them, mainly by providing abstract placeholders, called *proxies*, which can be used in calculations and modified at runtime.


### Overview
 JITLib consists of a number of **placeholders** (server side and client side *proxies*) and **schemes of access**> *They have in common that they treat assignment as a method. In such a way, they are an extension of the assignment implementation in Smalltalk-72, which makes "=" a message sent to the receiving object.*. These two aspects of space corresponding to *inclusion* and *reference*, depend on their context - here the placeholders are like roles which have a certain behaviour and can be fulfilled by certain objects. It is useful to be aware of the three aspects of such a placeholder: a certain set of elements can be their **source**, they can be used in a set of **contexts** and have a default source, if none is given.

Frequently used classes:  [Tdef](../Classes/Tdef.md) (for tasks), [ProxySpace](../Classes/ProxySpace.md), [NodeProxy](../Classes/NodeProxy.md) and [Ndef](../Classes/Ndef.md) (for synths), [Pdef](../Classes/Pdef.md) and [Pdefn](../Classes/Pdefn.md) (for patterns).


> **Note:** For some recent changes, see: [JITLibChanges3.7](../Other/JITLibChanges3.7.md)


For additional functionality, see also **JITLib extensions Quark**. To install it, run the following:


```
"JITLibExtensions".include;
```






## Tutorial: Interactive Programming with SuperCollider and jitlib
This tutorial focusses on some basic concepts used in JITLib. There are many possibilities, such as server messaging and pattern proxies which are not covered in tutorial form presently.


**content:**
: **placeholders in SuperCollider**
: [JITLib/jitlib_basic_concepts_01](../Tutorials/JITLib/jitlib_basic_concepts_01.md)

**referencing and environments**
: [JITLib/jitlib_basic_concepts_02](../Tutorials/JITLib/jitlib_basic_concepts_02.md)

**internal structure of node proxy**
: [JITLib/jitlib_basic_concepts_03](../Tutorials/JITLib/jitlib_basic_concepts_03.md)

**timing in node proxy**
: [JITLib/jitlib_basic_concepts_04](../Tutorials/JITLib/jitlib_basic_concepts_04.md)





## Overview of the different classes and techniques
- **Defs**: One way or style of access is the def-classes (Pdef, Ndef etc.). It binds a symbol to an object in a specific way:
```
Pdef(\name)        //returns the proxy
```


```
Pdef(\name, object)    //sets the source and returns the proxy
```

the rest of the behaviour depends on its use.client side: [Pdef](../Classes/Pdef.md), [Pdefn](../Classes/Pdefn.md), [Tdef](../Classes/Tdef.md), [Pbindef](../Classes/Pbindef.md), [Psym](../Classes/Psym.md), [Pnsym](../Classes/Pnsym.md), [Fdef](../Classes/Fdef.md)server side: [Ndef](../Classes/Ndef.md)
- **Environments**: Another way, for server side NodeProxies, is an environment that returns placeholders on demand:
```
ProxySpace.push
```


```
~out = { ...}
```

helpfile: [ProxySpace](../Classes/ProxySpace.md) for the use together with other environments, see [JITLib/jitlib_basic_concepts_02](../Tutorials/JITLib/jitlib_basic_concepts_02.md)
- **Lower Level Proxies**: There is also direct access *without using the access schemes* : NodeProxy, TaskProxy etc. provide it. Internally the former use these as base classes.language side: [PatternProxy](../Classes/PatternProxy.md), [EventPatternProxy](../Classes/EventPatternProxy.md), [TaskProxy](../Classes/TaskProxy.md), [PbindProxy](../Classes/PbindProxy.md), [Pdict](../Classes/Pdict.md)server side: [NodeProxy](../Classes/NodeProxy.md)
- **History**: To record all textual changes, [History](../Classes/History.md) is provides navigation and a memory of code.
- **Multichannel systems**:, [Monitor](../Classes/Monitor.md) (used internally) has a [playN](../Reference/playN.md) method.
- **GUI**: overviews and mixers: [ProxyMixer](../Classes/ProxyMixer.md), [TdefAllGui](../Classes/TdefAllGui.md), [PdefAllGui](../Classes/PdefAllGui.md), [NdefMixer](../Classes/NdefMixer.md)(for separate use: [TdefGui](../Classes/TdefGui.md), [PdefGui](../Classes/PdefGui.md), [MonitorGui](../Classes/MonitorGui.md), [NdefGui](../Classes/NdefGui.md), [NdefParamGui](../Classes/NdefParamGui.md))




## Tutorials

**[JITLib/proxyspace_examples](../Tutorials/JITLib/proxyspace_examples.md)**
: (a broad variety of inputs and uses)

**[JITLib/jitlib_efficiency](../Tutorials/JITLib/jitlib_efficiency.md)**
: (optimising code)

**[JITLib/the_lazy_proxy](../Tutorials/JITLib/the_lazy_proxy.md)**
: (how the initialisation works)

**[JITLib/jitlib_fading](../Tutorials/JITLib/jitlib_fading.md)**
: (how crossfade of code works)

**[JITLib/jitlib_asCompileString](../Tutorials/JITLib/jitlib_asCompileString.md)**
: (storing and reproducing proxies)

**[JITLib/recursive_phrasing](../Tutorials/JITLib/recursive_phrasing.md)**
: (a specific use of Pdef)

**[JITLib/jitlib_asCompileString](../Tutorials/JITLib/jitlib_asCompileString.md)**
: (how to reproduce source code from objects)

**[JITLib/jitlib_networking](../Tutorials/JITLib/jitlib_networking.md)**
: (how to collaborative live code with JITLib)

**[JITLib/basic_live_coding_techniques](../Tutorials/JITLib/basic_live_coding_techniques.md)**
: (live coding without jitlib)

**[NodeProxy_roles](../Reference/NodeProxy_roles.md)**
: (adverbial syntax for NodeProxy sources)





## Networking
- in remote and local networks thanks to sc-architecture node proxies can be **used on any server**, as long as it notifies the client and has a correctly initialized default node. **Note that the number of logins or the client id should be set**.
```
    s.options.maxLogins = 16; // an ensemble with up to 16 servers
```






## See also these related useful classes:

**[BusPlug](../Classes/BusPlug.md)**
: (listener on a bus)

**[SkipJack](../Classes/SkipJack.md)**
: (a task that keeps awake across cmd-period)

**[LazyEnvir](../Classes/LazyEnvir.md)**
: (and environment that returns proxies)

**[EnvironmentRedirect](../Classes/EnvironmentRedirect.md)**
: (abstract superclass for redirecting environments)

**[EnvGate](../Classes/EnvGate.md)**
: (singleton fade envelope)



History and GUI classes written by Alberto de Campo.

Thanks a lot for all the feedback and ideas!

_____________________________________________________________

The research for this project was funded by: German Research Foundation (DFG) and the Future Funds of Styria, Austria.



