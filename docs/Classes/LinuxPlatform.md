# LinuxPlatform

*Linux platform-specific methods*

**Categories:** Platform

## Description

This class is available only on Linux, and implements Linux platform-specific methods.

### Environment variables for Jack
Among other things, this class makes it possible to set some environment variables in your Linux operating system to automate connecting the Jack Audio Server on startup.

See [AudioDeviceSelection / Linux ](../Reference/AudioDeviceSelection.md#linux) for more information on this.




## Class Methods


### Setting or finding a terminal emulator
### `runInTerminalCmd`
get or set the preferred command to invoke a terminal emulator when performing [String#-runInTerminal](../Classes/String.md#-runinterminal).If `nil` (which is the default), sclang will search for a supported terminal emulator installed on the system, the first time `runInTerminal` is called (see [#*getTerminalEmulatorCmd](#*getterminalemulatorcmd)).
> **Note:** this setting doesn't persist across sessions

**Arguments:**

| Argument | Description |
|----------|-------------|
| `value` | a string, which has to necessarily include **two** `%`. For example:
```supercollider
LinuxPlatform.runInTerminalCmd = "xterm -T % -e %"
```

The first `"%"` is a placeholder for the window title, and the second is a placeholder for the actual command to be executed. Refer to your terminal emulator's documentation to find appropriate command line flags. |  

### `getTerminalEmulatorCmd`
scans the system for a supported terminal emulator. This method runs synchronously, and could block other scheduled operations while searching. If you rely on [String#-runInTerminal](../Classes/String.md#-runinterminal), it is recommended to run this method before you start scheduling Patterns or Routines, or to set [#*runInTerminalCmd](#*runinterminalcmd) manually.**Returns:** command to invoke a terminal emulator, to be used as [LinuxPlatform#*runInTerminalCmd](../Classes/LinuxPlatform.md#*runinterminalcmd)jacklinux


