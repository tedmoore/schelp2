# LID permissions

*Details how to configure your computer to set the permissions to access LID's*

**Categories:** External Control>HID

**Related:** [HID_permissions](../Guides/HID_permissions.md), [LID](../Classes/LID.md)


## On Linux
You will have to set the permissions with udev to be correct, create a file in the folder: `/etc/udev/rules.d/`, and name it (e.g.) `90-lid-permissions.rules`

In the file, you will need this line:

`KERNEL=="event[0-9]*", NAME="input/%k", MODE="0664", GROUP="plugdev"`

This will give read and write permissions to lid-devices to users that are in the `plugdev` group on your system.

To check whether you belong to that group execute the command `groups` in the terminal.

After you have added the udev rules file, you can access the device after plugging and replugging the device.

You can change the permission manually (as root) from the terminal with the command:


```
sudo chmod 664 /dev/input/event*
sudo chgrp plugdev /dev/input/event*
```


Check the permissions with:


```
"ls /dev/input/event* -lah".unixCmd;
```






