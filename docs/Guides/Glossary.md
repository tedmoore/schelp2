# Glossary

*Glossary of some relevant words*

**Categories:** Help


**bufferbuffer**
: A server-side header and array of 32 bit floating point sample data. Buffers are used for sound files, delay lines, arrays of global controls, and arrays of inter-synth patch points. Represented by the client-side class [Buffer](../Classes/Buffer.md).

**classclass**
: A description of the state and behaviour of a set of objects.

**clientclient**
: SC is divided into two separate applications: The client and the server. The client is where the SuperCollider language is implemented and where one executes code. The server actually synthesizes the audio, contains the node tree of synths and groups and responds to Open Sound Control messages from the client. See [ClientVsServer](../Guides/ClientVsServer.md) for more information.

**groupgroup**
: A linked list of nodes. Groups provide ways to control execution of many nodes at once. A group is a kind of node. Colloquially one can understand a group as an ordered grouping of other nodes, which may include both synths and other groups. Represented by the client-side class [Group](../Classes/Group.md).

**interfaceinterface**
: The set of messages to which an object responds.

**instanceinstance**
: One of the objects described by a class.

**instance variablevariable**
: A part of an object's internal state

**messagemessage**
: A request for an object to perform an operation.

**methodmethod**
: A description of the operations necessary to implement a message for a particular class.

**MIDImidi**
: A protocol for sending music control data between synthesizers.

**nodenode**
: One point in a tree of nodes executed in a depth first traversal order by the synth engine. There are two types of nodes, synths and groups. These are represented by the client-side classes [Synth](../Classes/Synth.md) and [Group](../Classes/Group.md), and their abstract superclass [Node](../Classes/Node.md). The node tree defines the order of execution for synths.

**objectobject**
: Something that has data, representing the object's state, and a set of operations that can be performed on the object.

**Open Sound ControlOSCopensoundcontrol**
: a protocol defined by CNMAT at UCBerkeley for controlling synthesizers. See [http://opensoundcontrol.org/.](http://opensoundcontrol.org/.) SuperCollider communicates between the client and server using OSC messages over UDP or TCP.

**OSC**
: See Open Sound Control.

**polymorphismpolymorphism**
: The ability for different kinds of objects to respond differently to the same message.

**protocolprotocol**
: A set of messages that implement a specific kind of behaviour.

**receiverreceiver**
: The object to which a message is sent.

**serverserver**
: SC is divided into two separate applications: The client and the server. The client is where the SuperCollider language is implemented and where one executes code. The server actually synthesizes the audio, contains the node tree of synths and groups and responds to Open Sound Control messages from the client. See [ClientVsServer](../Guides/ClientVsServer.md) for more information.

**synthsynth**
: A sound processing module, based upon a particular synth definition. Similar to "voice " in other systems. Synths are referred to by a number. Represented by the client-side class [Synth](../Classes/Synth.md).

**synth definitionsynthdef**
: A definition for creating new synths. Synth definitions are like a pattern or design for synths. Similar to "instrument" in other systems. Represented by the client-side class [SynthDef](../Classes/SynthDef.md).

**TCPtcp**
: A protocol for streaming data over a network.

**UDPudp**
: A protocol for sending datagrams over a network.




