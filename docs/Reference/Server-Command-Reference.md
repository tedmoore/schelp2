# Server Command Reference

*SuperCollider Server Synth Engine Command Reference*

**Categories:** Server>Architecture

The following is a list of all server commands and their arguments.
Each command has a command number which can be sent to the server as a 32 bit integer instead of an OSC style string. Command numbers are listed at the end of this document.
If a command's description contains the word **Asynchronous**, then that command will be passed to a background thread to complete so as not to steal CPU time from the audio synthesis thread. All asynchronous commands send a reply to the client when they are completed. Many asynchronous commands can contain an OSC message or bundle to be executed upon completion. eg.

```supercollider
    ["/d_load", "synthdefs/void.scsyndef",
        ["/s_new", "void", 1001, 1, 0] // completion message
    ]
```


## Top-Level Commands

### /quit
Quit program. Exits the synthesis server.


**Asynchronous.**
: Replies to sender with **/done** just before completion.






### /notify
Register to receive notifications from server

| **int** | 1 to receive notifications, 0 to stop receiving them. | 
| --- | --- || **int** | client ID (optional) | 
If the first argument is 1, server will remember your return address and send you notifications; if 0, server will stop sending notifications.


**Asynchronous.**
: Replies to sender with **/done /notify clientID [maxLogins]** when complete. If this client has registered for notifications before, this may be the same ID. Otherwise it will be a new one. Clients can use this ID in multi-client situations to avoid conflicts when allocating resources such as node IDs, bus indices, and buffer numbers. **maxLogins** is only returned when the client ID argument is supplied in this command. **maxLogins** is not supported by supernova.






### /status
Query the status. Replies to sender with the following message:


**/status.reply**
: | int | 1. unused. | 
| --- | --- || int | number of unit generators. | | int | number of synths. | | int | number of groups. | | int | number of loaded synth definitions. | | float | average percent CPU usage for signal processing | | float | peak percent CPU usage for signal processing | | double | nominal sample rate | | double | actual sample rate | 
> **Note:** `/status` messages won't be posted, if the server is in `/dumpOSC` mode






### /cmd
Plug-in defined command.

| **string** | command name | 
| --- | --- || **...** | any arguments | 
Commands are defined by plug-ins.




### /dumpOSC
Display incoming OSC messages.

| **int** | code | 
| --- | --- |
Turns on and off printing of the contents of incoming Open Sound Control messages. This is useful when debugging your command stream.

The values for the code are as follows:

| 0 | turn dumping OFF. | 
| --- | --- || 1 | print the parsed contents of the message. | | 2 | print the contents in hexadecimal. | | 3 | print both the parsed and hexadecimal representations of the contents. | 



### /sync
Notify when async commands have completed.

| **int** | a unique number identifying this command. | 
| --- | --- |
Replies with a **/synced** message when all asynchronous commands received before this one have completed. The reply will contain the sent unique ID.


**Asynchronous.**
: Replies to sender with **/synced, ID** when complete.






### /clearSched
Clear all scheduled bundles. Removes all bundles from the scheduling queue.




### /error
Enable/disable error message posting.

| **int** | mode | 
| --- | --- |
Turn on or off error messages sent to the SuperCollider post window. Useful when sending a message, such as **/n_free**, whose failure does not necessarily indicate anything wrong.

The values for mode are as follows:

| 0 | turn off error posting until the next ['/error', 1] message. | 
| --- | --- || 1 | turn on error posting. | 
For convenience of client-side methods, you can also suppress errors temporarily, for the scope of a single bundle.

| -1 | turn off locally in the bundle -- error posting reverts to the "permanent" setting for the next message or bundle. | 
| --- | --- || -2 | turn on locally in the bundle. | 
These "temporary" states accumulate within a single bundle -- so if you have nested calls to methods that use bundle-local error suppression, error posting remains off until all the layers have been unwrapped. If you use ['/error', -1] within a self-bundling method, you should always close it with ['/error', -2] so that subsequent bundled messages will take the correct error posting status. However, even if this is not done, the next bundle or message received will begin with the standard error posting status, as set by modes 0 or 1.

Temporary error suppression may not affect asynchronous commands in every case.




### /version
Query the SuperCollider version. Replies to sender with the following message:


**/version.reply**
: | string | Program name. May be "scsynth" or "supernova". | 
| --- | --- || int | Major version number. Equivalent to sclang's `Main.scVersionMajor`. | | int | Minor version number. Equivalent to sclang's `Main.scVersionMinor`. | | string | Patch version name. Equivalent to the sclang code `"." ++ Main.scVersionPatch ++ Main.scVersionTweak`. | | string | Git branch or tag name. | | string | First seven hex digits of the commit hash. |



The standard human-readable version string can be constructed by concatenating `major_version ++ "." ++ minor_version ++ patch_version`. Since version information is easily accessible to sclang users via the methods described above, this command is mostly useful for alternate clients.

The git branch/tag name and commit hash could be anything if the user has forked SC, so they should only be used for display and user interface purposes.




### /rtMemoryStatus
Queries the amount of currently free real-time memory (in bytes).


**/rtMemoryStatus.reply**
: | int | Amount of free real-time memory (in bytes). | 
| --- | --- || int | Size of largest continuous block (in bytes). |







## Synth Definition Commands

### /d_recv
Receive a synth definition file.

| **bytes** | buffer of data. | 
| --- | --- || **bytes** | an OSC message to execute upon completion. (optional) | 
Loads a file of synth definitions from a buffer in the message. Resident definitions with the same names are overwritten.


**Asynchronous.**
: Replies to sender with **/done** when complete.






### /d_load
Load synth definition.

| **string** | pathname of file. Can be a pattern like `"synthdefs/perc-*"` | 
| --- | --- || **bytes** | an OSC message to execute upon completion. (optional) | 
Loads a file of synth definitions. Resident definitions with the same names are overwritten.


**Asynchronous.**
: Replies to sender with **/done** when complete.






### /d_loadDir
Load a directory of synth definitions.

| **string** | pathname of directory. | 
| --- | --- || **bytes** | an OSC message to execute upon completion. (optional) | 
Loads a directory of synth definitions files. Resident definitions with the same names are overwritten.


**Asynchronous.**
: Replies to sender with **/done** when complete.






### /d_free
Delete synth definition.

| N * **string** | synth def name | 
| --- | --- |
Removes a synth definition. The definition is removed immediately, and does not wait for synth nodes based on that definition to end.





## Node Commands

### /n_free
Delete a node.

| N * **int** | node ID | 
| --- | --- |
Stops a node abruptly, removes it from its group, and frees its memory. A list of node IDs may be specified. Using this method can cause a click if the node is not silent at the time it is freed.




### /n_run
Turn node on or off.

| N * |  | 
| --- | --- |


- If the run flag set to zero then the node will not be executed.
- If the run flag is set back to one, then it will be executed.


Using this method to start and stop nodes can cause a click if the node is not silent at the time run flag is toggled.




### /n_set
Set a node's control value(s).

| **int** | node ID | 
| --- | --- || N * |  | 
Takes a list of pairs of control indices and values and sets the controls to those values. If the node is a group, then it sets the controls of every node in the group.

This message now supports array type tags ($[ and $]) in the control/value component of the OSC message. Arrayed control values are applied in the manner of n_setn (i.e., sequentially starting at the indexed or named control).




### /n_setn
Set ranges of a node's control value(s).

| **int** | node ID | 
| --- | --- || N * |  | 
Set contiguous ranges of control indices to sets of values. For each range, the starting control index is given followed by the number of controls to change, followed by the values. If the node is a group, then it sets the controls of every node in the group.




### /n_fill
Fill ranges of a node's control value(s).

| **int** | node ID | 
| --- | --- || N * |  | 
Set contiguous ranges of control indices to single values. For each range, the starting control index is given followed by the number of controls to change, followed by the value to fill. If the node is a group, then it sets the controls of every node in the group.




### /n_map
Map a node's controls to read from a bus.

| **int** | node ID | 
| --- | --- || N * |  | 
Takes a list of pairs of control names or indices and bus indices and causes those controls to be read continuously from a global control bus. If the node is a group, then it maps the controls of every node in the group. If the control bus index is -1 then any current mapping is undone. Any n_set, n_setn and n_fill command will also unmap the control.




### /n_mapn
Map a node's controls to read from buses.

| **int** | node ID | 
| --- | --- || N * |  | 
Takes a list of triplets of control names or indices, bus indices, and number of controls to map and causes those controls to be mapped sequentially to buses. If the node is a group, then it maps the controls of every node in the group. If the control bus index is -1 then any current mapping is undone. Any n_set, n_setn and n_fill command will also unmap the control.




### /n_mapa
Map a node's controls to read from an audio bus.

| **int** | node ID | 
| --- | --- || N * |  | 
Takes a list of pairs of control names or indices and audio bus indices and causes those controls to be read continuously from a global audio bus. If the node is a group, then it maps the controls of every node in the group. If the audio bus index is -1 then any current mapping is undone. Any n_set, n_setn and n_fill command will also unmap the control. For the full audio rate signal, the argument must have its rate set to \ar.




### /n_mapan
Map a node's controls to read from audio buses.

| **int** | node ID | 
| --- | --- || N * |  | 
Takes a list of triplets of control names or indices, audio bus indices, and number of controls to map and causes those controls to be mapped sequentially to buses. If the node is a group, then it maps the controls of every node in the group. If the audio bus index is -1 then any current mapping is undone. Any n_set, n_setn and n_fill command will also unmap the control. For the full audio rate signal, the argument must have its rate set to \ar.




### /n_before
Place a node before another.

| N * |  | 
| --- | --- |
Places node A in the same group as node B, to execute immediately before node B.




### /n_after
Place a node after another.

| N * |  | 
| --- | --- |
Places node A in the same group as node B, to execute immediately after node B.




### /n_query
Get info about a node.

| N * **int** | node ID | 
| --- | --- |
The server sends an /n_info message for each node to registered clients. See Node Notifications below for the format of the /n_info message.




### /n_trace
Trace a node.

| N * **int** | node IDs | 
| --- | --- |
Causes a synth to print out the values of the inputs and outputs of its unit generators for one control period. Causes a group to print the node IDs and names of each node in the group for one control period.




### /n_order
Move and order a list of nodes.

| **int** | add action (0,1,2 or 3 see below) | 
| --- | --- || **int** | add target ID | | N * **int** | node IDs | 
Move the listed nodes to the location specified by the target and add action, and place them in the order specified. Nodes which have already been freed will be ignored.


**add actions:**
: | 0 | construct the node order at the head of the group specified by the add target ID. | 
| --- | --- || 1 | construct the node order at the tail of the group specified by the add target ID. | | 2 | construct the node order just before the node specified by the add target ID. | | 3 | construct the node order just after the node specified by the add target ID. |







## Synth Commands

### /s_new
Create a new synth.

| **string** | synth definition name | 
| --- | --- || **int** | synth ID | | **int** | add action (0,1,2, 3 or 4 see below) | | **int** | add target ID | | N * |  | 
Create a new synth from a synth definition, give it an ID, and add it to the tree of nodes. There are four ways to add the node to the tree as determined by the add action argument which is defined as follows:


**add actions:**
: | 0 | add the new node to the head of the group specified by the add target ID. | 
| --- | --- || 1 | add the new node to the tail of the group specified by the add target ID. | | 2 | add the new node just before the node specified by the add target ID. | | 3 | add the new node just after the node specified by the add target ID. | | 4 | the new node replaces the node specified by the add target ID. The target node is freed. |



Controls may be set when creating the synth. The control arguments are the same as for the n_set command.

If you send **/s_new** with a synth ID of -1, then the server will generate an ID for you. The server reserves all negative IDs. Since you don't know what the ID is, you cannot talk to this node directly later. So this is useful for nodes that are of finite duration and that get the control information they need from arguments and buses or messages directed to their group. In addition no notifications are sent when there are changes of state for this node, such as **/go**, **/end**, **/on**, **/off**.

If you use a node ID of -1 for any other command, such as **/n_map**, then it refers to the most recently created node by **/s_new** (auto generated ID or not). This is how you can map the controls of a node with an auto generated ID. In a multi-client situation, the only way you can be sure what node -1 refers to is to put the messages in a bundle.

This message now supports array type tags ($[ and $]) in the control/value component of the OSC message. Arrayed control values are applied in the manner of n_setn (i.e., sequentially starting at the indexed or named control). See the [NodeMessaging](../Guides/NodeMessaging.md) helpfile.




### /s_get
Get control value(s).

| **int** | synth ID | 
| --- | --- || N * **int** or **string** | a control index or name | 
Replies to sender with the corresponding **/n_set** command.




### /s_getn
Get ranges of control value(s).

| **int** | synth ID | 
| --- | --- || N * |  | 
Get contiguous ranges of controls. Replies to sender with the corresponding **/n_setn** command.




### /s_noid
Auto-reassign synth's ID to a reserved value.

| N * **int** | synth IDs | 
| --- | --- |
This command is used when the client no longer needs to communicate with the synth and wants to have the freedom to reuse the ID. The server will reassign this synth to a reserved negative number. This command is purely for bookkeeping convenience of the client. No notification is sent when this occurs.





## Group Commands

### /g_new
Create a new group.

| N * |  | 
| --- | --- |
Create a new group and add it to the tree of nodes. There are four ways to add the group to the tree as determined by the add action argument which is defined as follows (the same as for **/s_new**):


**add actions:**
: | 0 | add the new group to the head of the group specified by the add target ID. | 
| --- | --- || 1 | add the new group to the tail of the group specified by the add target ID. | | 2 | add the new group just before the node specified by the add target ID. | | 3 | add the new group just after the node specified by the add target ID. | | 4 | the new node replaces the node specified by the add target ID. The target node is freed. |



Multiple groups may be created in one command by adding arguments.




### /p_new
Create a new parallel group.

| N * |  | 
| --- | --- |
Create a new parallel group and add it to the tree of nodes. Parallel groups are relaxed groups, their child nodes are evaluated in unspecified order. There are four ways to add the group to the tree as determined by the add action argument which is defined as follows (the same as for **/s_new**):


**add actions:**
: | 0 | add the new group to the head of the group specified by the add target ID. | 
| --- | --- || 1 | add the new group to the tail of the group specified by the add target ID. | | 2 | add the new group just before the node specified by the add target ID. | | 3 | add the new group just after the node specified by the add target ID. | | 4 | the new node replaces the node specified by the add target ID. The target node is freed. |



Multiple groups may be created in one command by adding arguments.




### /g_head
Add node to head of group.

| N * |  | 
| --- | --- |
Adds the node to the head (first to be executed) of the group.




### /g_tail
Add node to tail of group.

| N * |  | 
| --- | --- |
Adds the node to the tail (last to be executed) of the group.




### /g_freeAll
Delete all nodes in a group.

| N * **int** | group ID(s) | 
| --- | --- |
Frees all nodes in the group. A list of groups may be specified.




### /g_deepFree
Free all synths in this group and all its sub-groups.

| N * **int** | group ID(s) | 
| --- | --- |
Traverses all groups below this group and frees all the synths. Sub-groups are not freed. A list of groups may be specified.




### /g_dumpTree
Post a representation of this group's node subtree.

| N * |  | 
| --- | --- |
Posts a representation of this group's node subtree, i.e. all the groups and synths contained within it, optionally including the current control values for synths.




### /g_queryTree
Get a representation of this group's node subtree.

| N * |  | 
| --- | --- |
Request a representation of this group's node subtree, i.e. all the groups and synths contained within it. Replies to the sender with a **/g_queryTree.reply** message listing all of the nodes contained within the group in the following format:

| **int** | flag: if synth control values are included 1, else 0 | 
| --- | --- || **int** | node ID of the requested group | | **int** | number of child nodes contained within the requested group | | then for each node in the subtree: |  | 
N.B. The order of nodes corresponds to their execution order on the server. Thus child nodes (those contained within a group) are listed immediately following their parent. See the method Server:queryAllNodes for an example of how to process this reply.





## Unit Generator Commands

### /u_cmd
Send a command to a unit generator.

| **int** | node ID | 
| --- | --- || **int** | unit generator index | | **string** | command name | | **...** | any arguments | 
Sends all arguments following the command name to the unit generator to be performed. Commands are defined by unit generator plug ins.





## Buffer Commands
Buffers are stored in a global array, indexed by integers starting at zero.


### /b_alloc
Allocate buffer space.

| **int** | buffer number | 
| --- | --- || **int** | number of frames | | **int** | number of channels (optional. default = 1 channel) | | **bytes** | an OSC message to execute upon completion. (optional) | | **float** | the required sample rate (optional. default (or 0) = the server's sample rate) | 
Allocates zero filled buffer to number of channels and samples.


**Asynchronous.**
: Replies to sender with **/done /b_alloc bufNum** when complete.






### /b_allocRead
Allocate buffer space and read a sound file.

| **int** | buffer number | 
| --- | --- || **string** | path name of a sound file. | | **int** | starting frame in file (optional. default = 0) | | **int** | number of frames to read (optional. default = 0, see below) | | **bytes** | an OSC message to execute upon completion. (optional) | 
Allocates buffer to number of channels of file and number of samples requested, or fewer if sound file is smaller than requested. Reads sound file data from the given starting frame in the file. If the number of frames argument is less than or equal to zero, the entire file is read.


**Asynchronous.**
: Replies to sender with **/done /b_allocRead bufNum** when complete.






### /b_allocReadChannel
Allocate buffer space and read channels from a sound file.

| **int** | buffer number | 
| --- | --- || **string** | path name of a sound file | | **int** | starting frame in file | | **int** | number of frames to read | | N * | N >= 0 | | **bytes** | an OSC message to execute upon completion. (optional) | 
As b_allocRead, but reads individual channels into the allocated buffer in the order specified. If the channels argument is absent or empty all channels are read in the order they appear in the file.


**Asynchronous.**
: Replies to sender with **/done /b_allocReadChannel bufNum** when complete.






### /b_read
Read sound file data into an existing buffer.

| **int** | buffer number | 
| --- | --- || **string** | path name of a sound file. | | **int** | starting frame in file (optional. default = 0) | | **int** | number of frames to read (optional. default = -1, see below) | | **int** | starting frame in buffer (optional. default = 0) | | **int** | leave file open (optional. default = 0) | | **bytes** | an OSC message to execute upon completion. (optional) | 
Reads sound file data from the given starting frame in the file and writes it to the given starting frame in the buffer. If number of frames is less than zero, the entire file is read. If reading a file to be used by [DiskIn](../Classes/DiskIn.md) ugen then you will want to set "leave file open" to one, otherwise set it to zero.


**Asynchronous.**
: Replies to sender with **/done /b_read bufNum** when complete.






### /b_readChannel
Read sound file channel data into an existing buffer.

| **int** | buffer number | 
| --- | --- || **string** | path name of a sound file | | **int** | starting frame in file | | **int** | number of frames to read | | **int** | starting frame in buffer | | **int** | leave file open | | N * | N >= 0 | | **bytes** | completion message | 
As **b_read**, but reads individual channels in the order specified. The number of channels requested must match the number of channels in the buffer.


**Asynchronous.**
: Replies to sender with **/done /b_readChannel bufNum** when complete.






### /b_write
Write sound file data.

| **int** | buffer number | 
| --- | --- || **string** | path name of a sound file. | | **string** | header format. | | **string** | sample format. | | **int** | number of frames to write (optional. default = -1, see below) | | **int** | starting frame in buffer (optional. default = 0) | | **int** | leave file open (optional. default = 0) | | **bytes** | an OSC message to execute upon completion. (optional) | 
Write a buffer as a sound file.


**Header format is one of:**
: "aiff", "next", "wav", "ircam"", "raw"

**Sample format is one of:**
: "int8", "int16", "int24", "int32", "float", "double", "mulaw", "alaw"



Not all combinations of header format and sample format are possible. If number of frames is less than zero, all samples from the starting frame to the end of the buffer are written. If opening a file to be used by DiskOut ugen then you will want to set "leave file open" to one, otherwise set it to zero. If "leave file open" is set to one then the file is created, but no frames are written until the DiskOut ugen does so.


**Asynchronous.**
: Replies to sender with **/done /b_write bufNum** when complete.






### /b_free
Free buffer data.

| **int** | buffer number | 
| --- | --- || **bytes** | an OSC message to execute upon completion. (optional) | 
Frees buffer space allocated for this buffer.


**Asynchronous.**
: Replies to sender with **/done /b_free bufNum** when complete.






### /b_zero
Zero sample data.

| **int** | buffer number | 
| --- | --- || **bytes** | an OSC message to execute upon completion. (optional) | 
Sets all samples in the buffer to zero.


**Asynchronous.**
: Replies to sender with **/done /b_zero bufNum** when complete.






### /b_set
Set sample value(s).

| **int** | buffer number | 
| --- | --- || N * |  | 
Takes a list of pairs of sample indices and values and sets the samples to those values.




### /b_setn
Set ranges of sample value(s).

| **int** | buffer number | 
| --- | --- || N * |  | 
Set contiguous ranges of sample indices to sets of values. For each range, the starting sample index is given followed by the number of samples to change, followed by the values.




### /b_setSampleRate
Set the sampling rate of the buffer.

| **int** | buffer number | 
| --- | --- || **float** | the desired sampling rate. 0 or nil will set to the Server's sample rate. | 
Set the sampling rate of the buffer.




### /b_fill
Fill ranges of sample value(s).

| **int** | buffer number | 
| --- | --- || N * |  | 
Set contiguous ranges of sample indices to single values. For each range, the starting sample index is given followed by the number of samples to change, followed by the value to fill. This is only meant for setting a few samples, not whole buffers or large sections.




### /b_gen
Call a command to fill a buffer.

| **int** | buffer number | 
| --- | --- || **string** | command name | | **...** | command arguments | 
Plug-ins can define commands that operate on buffers. The arguments after the command name are defined by the command. The currently defined [buffer fill commands](../Reference/Server-Command-Reference.md#buffer-fill-commands) are listed below in a separate section.

`/b_gen` does not accept a completion message as the final argument.


**Asynchronous.**
: Replies to sender with **/done /b_gen bufNum** when complete.






### /b_close
Close soundfile.

| **int** | buffer number | 
| --- | --- || **bytes** | an OSC message to execute upon completion. (optional) | 
After using a buffer with [DiskOut](../Classes/DiskOut.md), close the soundfile and write header information.


**Asynchronous.**
: Replies to sender with **/done /b_close bufNum** when complete.






### /b_query
Get buffer info.

| N * **int** | buffer number(s) | 
| --- | --- |
Responds to the sender with a **/b_info** message. The arguments to /b_info are as follows:

| N * |  | 
| --- | --- |



### /b_get
Get sample value(s).

| **int** | buffer number | 
| --- | --- || N * **int** | a sample index | 
Replies to sender with the corresponding **/b_set** command.




### /b_getn
Get ranges of sample value(s).

| **int** | buffer number | 
| --- | --- || N * |  | 
Get contiguous ranges of samples. Replies to sender with the corresponding **/b_setn** command. This is only meant for getting a few samples, not whole buffers or large sections.





## Control Bus Commands

### /c_set
Set bus value(s).

| N * |  | 
| --- | --- |
Takes a list of pairs of bus indices and values and sets the buses to those values.




### /c_setn
Set ranges of bus value(s).

| N * |  | 
| --- | --- |
Set contiguous ranges of buses to sets of values. For each range, the starting bus index is given followed by the number of channels to change, followed by the values.




### /c_fill
Fill ranges of bus value(s).

| N * |  | 
| --- | --- |
Set contiguous ranges of buses to single values. For each range, the starting sample index is given followed by the number of buses to change, followed by the value to fill.




### /c_get
Get bus value(s).

| N * **int** | a bus index | 
| --- | --- |
Takes a list of buses and replies to sender with the corresponding **/c_set** command.




### /c_getn
Get ranges of bus value(s).

| N * |  | 
| --- | --- |
Get contiguous ranges of buses. Replies to sender with the corresponding **/c_setn** command.





## Non Real Time Mode Commands

### /nrt_end
End real time mode, close file. Not yet implemented.

This message should be sent in a bundle in non real time mode. The bundle timestamp will establish the ending time of the file. This command will end non real time mode and close the sound file. Replies to sender with **/done** when complete.





## Replies to Commands
These messages are sent by the server in response to some commands.


### /done
An asynchronous message has completed.

| **string** | the name of the command | 
| --- | --- || **other** | (optional) some commands provide other information, for example a buffer index. | 
Sent in response to all asynchronous commands. Sent only to the sender of the original message.




### /fail
An error occurred.

| **string** | the name of the command | 
| --- | --- || **string** | the error message. | | **other** | (optional) some commands provide other information, for example a buffer index. | 
There was a problem. Sent only to the sender of the original message.




### /late
A command was received too late. not yet implemented

| **int** | the high 32 bits of the original time stamp. | 
| --- | --- || **int** | the low 32 bits of the original time stamp. | | **int** | the high 32 bits of the time it was executed. | | **int** | the low 32 bits of the time it was executed. | 
The command was received too late to be executed on time. Sent only to the sender of the original message.





## Node Notifications from Server
These messages are sent as notification of some event to all clients who have registered via the **/notify** command.

All of these have the same arguments:

| **int** | node ID | 
| --- | --- || **int** | the node's parent group ID | | **int** | previous node ID, -1 if no previous node. | | **int** | next node ID, -1 if no next node. | | **int** | 1 if the node is a group, 0 if it is a synth | | The following two arguments are only sent if the node is a group: | | **int** | the ID of the head node, -1 if there is no head node. | | **int** | the ID of the tail node, -1 if there is no tail node. | 

### /n_go
A node was started. This command is sent to all registered clients when a node is created.




### /n_end
A node ended. This command is sent to all registered clients when a node ends and is deallocated.




### /n_off
A node was turned off. This command is sent to all registered clients when a node is turned off.




### /n_on
A node was turned on. This command is sent to all registered clients when a node is turned on.




### /n_move
A node was moved. This command is sent to all registered clients when a node is moved.




### /n_info
Reply to /n_query. This command is sent to all registered clients in response to an **/n_query** command.





## Trigger Notification
These messages are sent as notification of some event to all clients who have registered via the **/notify** command.


### /tr
A trigger message.

| **int** | node ID | 
| --- | --- || **int** | trigger ID | | **float** | trigger value | 
This command is the mechanism that synths can use to trigger events in clients. The node ID is the node that is sending the trigger. The trigger ID and value are determined by inputs to the SendTrig unit generator which is the originator of this message.





## Buffer Fill Commands
These are the currently defined fill routines for use with the **/b_gen** command.


### Wave Fill Commands
There are three defined fill routines for sine waves.

The flags are defined as follows:

| 1 | normalize - Normalize peak amplitude of wave to 1.0. | 
| --- | --- || 2 | wavetable - If set, then the buffer is written in wavetable format so that it can be read by interpolating oscillators. | | 4 | clear - if set then the buffer is cleared before new partials are written into it. Otherwise the new partials are summed with the existing contents of the buffer. | 
These flags can be added together to create a unique single integer flag that describes the true/false combinations for these three options:

| 3 | 1 + 2 | normalize + wavetable | 
| --- | --- | --- || 5 | 1 + 4 | normalize + clear | | 6 | 2 + 4 | wavetable + clear | | 7 | 1 + 2 + 4 | normalize + wavetable + clear | 

**sine1**
: | **int** | flags, see above | 
| --- | --- || N * |  | Fills a buffer with a series of sine wave partials. The first float value specifies the amplitude of the first partial, the second float value specifies the amplitude of the second partial, and so on.

**sine2**
: | **int** | flags, see above | 
| --- | --- || N * |  | Similar to sine1 except that each partial frequency is specified explicitly instead of being an integer series of partials. Non-integer partial frequencies are possible.

**sine3**
: | **int** | flags, see above | 
| --- | --- || N * |  | Similar to sine2 except that each partial may have a nonzero starting phase.

**cheby**
: | **int** | flags, see above | 
| --- | --- || N * |  | Fills a buffer with a series of chebyshev polynomials, which can be defined as:
```supercollider
cheby(n) = amplitude * cos(n * acos(x))
```

The first float value specifies the amplitude for n = 1, the second float value specifies the amplitude for n = 2, and so on. To eliminate a DC offset when used as a waveshaper, the wavetable is offset so that the center value is zero.






### Other Commands

**copy**
: | **int** | sample position in destination | 
| --- | --- || **int** | source buffer number | | **int** | sample position in source | | **int** | number of samples to copy | Copy samples from the source buffer to the destination buffer specified in the b_gen command. If the number of samples to copy is negative, the maximum number of samples possible is copied.
**Asynchronous.**
: Replies to sender with **/done** when complete.







## Command Numbers
These are the currently defined command numbers. More may be added to the end of the list in the future.


```supercollider
enum {
    cmd_none = 0,

    cmd_notify = 1,
    cmd_status = 2,
    cmd_quit = 3,
    cmd_cmd = 4,

    cmd_d_recv = 5,
    cmd_d_load = 6,
    cmd_d_loadDir = 7,
    cmd_d_freeAll = 8,

    cmd_s_new = 9,

    cmd_n_trace = 10,
    cmd_n_free = 11,
    cmd_n_run = 12,
    cmd_n_cmd = 13,
    cmd_n_map = 14,
    cmd_n_set = 15,
    cmd_n_setn = 16,
    cmd_n_fill = 17,
    cmd_n_before = 18,
    cmd_n_after = 19,

    cmd_u_cmd = 20,

    cmd_g_new = 21,
    cmd_g_head = 22,
    cmd_g_tail = 23,
    cmd_g_freeAll = 24,

    cmd_c_set = 25,
    cmd_c_setn = 26,
    cmd_c_fill = 27,

    cmd_b_alloc = 28,
    cmd_b_allocRead = 29,
    cmd_b_read = 30,
    cmd_b_write = 31,
    cmd_b_free = 32,
    cmd_b_close = 33,
    cmd_b_zero = 34,
    cmd_b_set = 35,
    cmd_b_setn = 36,
    cmd_b_fill = 37,
    cmd_b_gen = 38,

    cmd_dumpOSC = 39,

    cmd_c_get = 40,
    cmd_c_getn = 41,
    cmd_b_get = 42,
    cmd_b_getn = 43,
    cmd_s_get = 44,
    cmd_s_getn = 45,

    cmd_n_query = 46,
    cmd_b_query = 47,

    cmd_n_mapn = 48,
    cmd_s_noid = 49,

    cmd_g_deepFree = 50,
    cmd_clearSched = 51,

    cmd_sync = 52,

    cmd_d_free = 53,

    cmd_b_allocReadChannel = 54,
    cmd_b_readChannel = 55,

    cmd_g_dumpTree = 56,
    cmd_g_queryTree = 57,


    cmd_error = 58,

    cmd_s_newargs = 59,

    cmd_n_mapa = 60,
    cmd_n_mapan = 61,
    cmd_n_order = 62,

    cmd_p_new = 63,

    cmd_version = 64,

    cmd_rtMemoryStatus = 65,

    cmd_b_setSampleRate = 66,

    NUMBER_OF_COMMANDS = 67
    };
```


copyright © 2002 James McCartney - converted to ScDoc format 2011 by Jonatan Liljedahl



