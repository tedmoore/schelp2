# Audio device selection

**Categories:** Server

*A reference for making audio device selection*

**Related:** [Server](../Classes/Server.md), [ServerOptions](../Classes/ServerOptions.md)

This reference provides information on audio device selection, including platform-specific details.
Specific devices can be selected through an instance of [ServerOptions](../Classes/ServerOptions.md). To access `ServerOptions` instance of the default server, you can use `Server.default.options`. [ServerOptions](../Classes/ServerOptions.md) also allows you to specify other important parameters of the device - the sample rate and hardware buffer size.

> **Note:** Device selection won't take effect until the server is (re)booted.



## macOS
By default the server will boot to your system's default audio devices. If you want to explicitly tell the server to use the internal soundcard, you need to specify both input and output device. The following example comes from a MacBook Pro:


```
Server.default.options.inDevice_("Built-in Microph");
Server.default.options.outDevice_("Built-in Output");
```


In case of a dedicated audio interface, you might need to specify a single device, e.g.


```
Server.default.options.device_("MOTU 828");
```


On Windows and macOS you can programmatically obtain a list of available audio devices without booting the server:


```
ServerOptions.devices; // all devices
ServerOptions.inDevices; // input devices
ServerOptions.outDevices; // output devices
```



### Sample rate mismatch
One possible reason why a server may fail to boot is a mismatch between input and output devices' sample rates, which may occur when using a different device for input and output (which is the case when using a Mac's internal soundcard). If the server fails to boot due to sample rate mismatch, an error will be posted accordingly.

You should set both input and output devices' sample rate to the same value. You can do this in Audio MIDI Setup:


```
"open -a 'Audio MIDI Setup'".unixCmd; // execute this to launch it
```





### Aggregate device
Sometimes you might want to use multiple devices for input or output. macOS provides a way to combine multiple physical devices into a virtual *Aggregate Device*. To create one, you have to open the Audio MIDI Setup application (in `/Applications/Utilities`). You should do this from an user account with administrator privileges.


```
"open -a 'Audio MIDI Setup'".unixCmd; // execute this to launch it
```




- In the `Audio Devices` window click on the Plus button on the bottom left and choose `Create Aggregate Device`.
- You can change its name to something specific if desired, for example "InternalAndMOTU".
- Check the `Use` column on the right for the devices you want to combine.


Now you need to tell SuperCollider to use your new aggregate device.


```
Server.default.options.device = "Aggregate Device"; //or the name you have specified in the previous step
```


After rebooting the server (`Server.default.reboot`) you should see in the post window that it now uses the Aggregate Device instead of system defaults:


Note that when you specify a sound device through SuperCollider's `ServerOptions`, there is no need to use the aggregate device as the system's default device.





## Linux
By default, SuperCollider on Linux uses JACK, and the audio device selection is managed by the JACK server. `ServerOptions` cannot override JACK's selection of audio hardware.


### Setup with JACK server
The SuperCollider server is considered a JACK *client*. In the following section, the term *client* will refer to the SuperCollider server, from the perspective of JACK.

When the server is compiled to use JACK as the audio backend, the `ServerOption`'s `device` can be used in two ways: to set the client name to register with JACK:


```
Server.default.options.device = "my_synth";
```


to use a specific JACK server, as well as set the client name:


```
Server.default.options.device = "JACKServerName:scsynthName";
```


A `nil` device is equivalent to `Server.default.options.device = "default:SuperCollider";`




### Jack Environment variables
The JACK connections can be configured via the environment variables `SC_JACK_DEFAULT_INPUTS` and `SC_JACK_DEFAULT_OUTPUTS`. These allow SuperCollider to detect system preferences for Jack inputs and outputs to/from the scsynth server. 

These variables are written as a string that specifies another jack client or a comma-separated list of jack ports formatted as a string.

The SuperCollider language client sets these environment variables to "system" by default, so that a server booted from SC language will connect by default.

If these are not set, the server will not connect to any JACK ports automatically. You may connect them manually, or by issuing `jack_connect` / `jack_disconnect` shell commands ([String#-unixCmd](../Classes/String.md#-unixcmd)). A server booted from the command line will thus not auto-connect, unless you set the variables in the same terminal session or shell profile (below).

This is the recommended way of changing the Jack environment variables for SuperCollider from within a SuperCollider script:


```
// connect first to input channels with system
"SC_JACK_DEFAULT_INPUTS".setenv("system:capture_1,system:capture_2");

// connect all output channels with system
"SC_JACK_DEFAULT_OUTPUTS".setenv("system");
```


As an alternative, these may be also be changed by setting the following environment variables in your **.bash_profile**, **.zsh_profile** or similar startup file for your shell:


```
export SC_JACK_DEFAULT_INPUTS="system"
export SC_JACK_DEFAULT_OUTPUTS="system"
```


To disable autoconnect from the language:


```
"SC_JACK_DEFAULT_INPUTS".unsetenv;
"SC_JACK_DEFAULT_OUTPUTS".unsetenv;
```






## Windows
By default the server will boot to your system's default audio devices using a `WASAPI` driver.

On Windows there are multiple audio driver APIs (e.g. `WASAPI`, `ASIO` etc.) that can be used to communicate with audio devices. The API (listed before the device name) needs to match between the input and the output, for example:


```
o = Server.default.options;
o.inDevice_("Windows WASAPI : Microphone");
o.outDevice_("Windows WASAPI : Speakers");
Server.default.reboot;
```


You can programmatically obtain a list of available audio devices without booting the server:


```
ServerOptions.devices; // all devices
ServerOptions.inDevices; // input devices
ServerOptions.outDevices; // output devices
```


Partial device name matching is supported in Windows (though not in macOS).


> **Note:** Leaving the `sampleRate` (e.g. `Server.default.options.sampleRate`) as `nil` for an `ASIO` device will likely result in setting the hardware to run at 44100 Hz.



### Choosing the device and the API
- If you need to specify the device, you will need to do so for both input and output (setting both `.inDevice`, as well as `.outDevice`), unless you use ASIO
- Both input and output device needs to use the same API (listed before the name, for example `WASAPI`, `ASIO` etc.).
- Both input and output device should use the same sample rate (although some APIs might provide resampling). This can be set in Windows's Audio Control Panel.


The following list provides basic reference for different APIs. The most recommended APIs are listed first.




### List of available APIs
As of SuperCollider 3.15, only `WASAPI` and `ASIO` APIs are enabled in the official releases.


**ASIO**
: - **Maximum channel count:** Supports an arbitrary number of input/output channels, as provided by the hardware
- **Typical latency:** Low
- **Caveats:** Dedicated ASIO driver needs to be provided by the audio device's manufacturer; this is common for most (semi-)professional interfaces, but not necessarily for internal soundcards
- **More info:** Designed for pro-audio devices; control over sampling rate and hardware buffer size is usually provided by the driver's control panel (i.e. not settable by SuperCollider); ASIO stands for Audio Stream Input/Output and was developed by Steinberg

**WASAPI**
: - **Maximum channel count:** Typically supports mono or stereo only; devices with more than 2 channels might be represented as multiple stereo pairs
- **Typical latency:** Low
- **Caveats:** Resampling is enabled by default, so SuperCollider can run at a different sample rate than the hardware, and other applications can share the same device
- **More info:** WASAPI stands for Windows Audio Session API and is the most modern Windows audio API

**WDM-KS**
: - **Maximum channel count:** Typically supports mono or stereo only; devices with more than 2 channels might be represented as multiple stereo pairs
- **Typical latency:** Low
- **Caveats:** On some systems SuperCollider will prevent other applications from using the audio device when using this API
- **More info:** WDM-KS stands for Windows Driver Model Kernel Streaming. It was the first native Windows API providing reasonably low latency

**DirectSound**
: - **Maximum channel count:** Typically supports mono or stereo only; devices with more than 2 channels might be represented as multiple stereo pairs
- **Typical latency:** Moderate/high
- **Caveats:** It is an older API and typically provides worse performance than the newer ones
- **More info:** DirectSound is part of DirectX and was originally created with game audio in mind

**MME**
: - **Maximum channel count:** Typically supports mono or stereo only; devices with more than 2 channels might be represented as multiple stereo pairs
- **Typical latency:** High
- **Caveats:** It is the oldest API on this list; it is chosen by default if the user does not specify which device to use
- **More info:** This API might work out-of-the-box, but choosing a newer one instead will usually provide better performance; MME stands for Multimedia Extension (for Windows 3.0)



If ASIO driver is available, it is probably the best choice to ensure low input/output latency. ASIO drivers usually provide both inputs and outputs through a single device.


> **Note:** On Windows, ASIO driver is likely the only option for multichannel operation (allowing to use more than 2 inputs/outputs simultaneously).



```
o = Server.default.options;
o.device = "ASIO : UMC ASIO Driver";
Server.default.reboot;
```





### ASIO4ALL
If you are using an internal soundcard or a device which does not come with an ASIO driver, an alternative is to use ASIO4ALL. It is a virtual ASIO driver, communicating with the soundcard using Windows' native APIs. It might provide better performance with built-in soundcards and it should allow for multichannel operation with such devices (if supported by the hardware). Use a web search engine to find a download link.


> **Note:** ASIO4ALL will usually **not** provide a better performance than a dedicated ASIO driver.


After installing ASIO4ALL, it can be selected as follows (confirm in the post window when the server boots):


```
Server.default.options.device = "ASIO : ASIO4ALL v2";
```








