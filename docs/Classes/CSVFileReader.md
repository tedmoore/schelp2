# CSVFileReader

*file reader for comma separated data*

**Related:** [File](../Classes/File.md)

**Categories:** Files

## Description

CSVFileReader reads comma-separated text files into 2D arrays line by line.
For tab delimited files use [TabFileReader](../Classes/TabFileReader.md). For semi-colon-delimited files use [SemiColonFileReader](../Classes/SemiColonFileReader.md). For space-delimited files, or custom delimiters, use [FileReader](../Classes/FileReader.md).

## Examples


```
(
// write a test file:
f = File("CSVReadTest.sc", "w");
f.write(
"Some,comma,delimited,items, in line 1

and then, some more, with several commas,,,, in line 3
"
);
f.close;
)


    // open file, read and put strings into array, close file.
x = CSVFileReader.read("CSVReadTest.sc").postcs;

    // can skip empty lines:
x = CSVFileReader.read("CSVReadTest.sc", true).postcs;

    // can skip blank entries caused by multiple commas:
x = CSVFileReader.read("CSVReadTest.sc", true, true).postcs;

    // do file open/close by hand if you prefer:
f = File("CSVReadTest.sc", "r"); f.isOpen;
t = CSVFileReader(f);
t.read(true, true).postcs;
f.close;

(
// write a test file with numbers:
f = File("CSVReadTestNum.sc", "w");

(1..10).do { |n| f.write(n.asString ++ ",") };
f.close;
)

x = CSVFileReader.read("CSVReadTestNum.sc", true, true).postcs;
x.collect(_.collect(_.interpret));    // convert to numbers.

    // or do it immediately:
x = CSVFileReader.readInterpret("CSVReadTestNum.sc").postcs;

(
// write a test file with several lines of numbers:
f = File("CSVReadTestNum.sc", "w");

(1..100).do { |n|
    f.write(n.asString ++ if (n % 10 != 0, ",", Char.nl)) };
f.close;
)


x = CSVFileReader.readInterpret("CSVReadTestNum.sc", true, true).postln;
```




