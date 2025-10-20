# Download

*Fetch a file from a remote URL*

**Categories:** Files

**Related:** [File](../Classes/File.md)

## Description

Download allows you to download a file from a specified URL


## Class Methods



### `new`
Create and start a new Download.**Arguments:**

| Argument | Description |
|----------|-------------|
| `requestedURL` | A [String](../Classes/String.md) containing the URL of the file to download. |  
| `localPath` | A [String](../Classes/String.md) containing the local path at which to save the downloaded file. |  
| `finishedFunc` | A [Function](../Classes/Function.md) to evaluate when the download is complete. |  
| `errorFunc` | A [Function](../Classes/Function.md) to evaluate if the download fails due to an error. |  
| `progressFunc` | A [Function](../Classes/Function.md) to process the download's progress. This Function will be passed two arguments, the bytes received, and the total bytes. |  
**Returns:** A new Download.

### `cancelAll`
Cancel all active Downloads.

## Instance Methods


### `cancel`
Cancel the download.
### `errorFunc`
Get or set the error [Function](../Classes/Function.md).
### `finishedFunc`
Get or set the download finished [Function](../Classes/Function.md).
### `progressFunc`
Get or set the download progress [Function](../Classes/Function.md).
## Examples


```
(
var url = "https://scottwilson.ca/files/flame.mp3";
var localPath = Platform.defaultTempDir +/+ url.split($/).last;

d = Download(
    url,
    localPath,
    {
        "downloaded to %".format(localPath).postln;
    },
    {
        "error".postln;
    },
    { |receivedBytes, totalBytes|
        "Downloaded %\\%".format((receivedBytes/totalBytes*100.0).round(1e-2)).postln;
    },
);
)

d.cancel; // cancel this
```




