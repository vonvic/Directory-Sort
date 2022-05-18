# Directory Sort
Sorts the files in a directory, where files are moved into folders titled
with their extensions. Python is used for fast and easy development, as it is
a familiar language to the author.

## Requirements
`python 3.10.0`

## How To Run
In the command line, run
```
python3 .
```
in the project directory.

Then, you will be met with the prompt
```
Enter which directory to sort (`.` for the current directory or `CTRL+C` to quit):
```

### Examples of Valid Inputs
```
/Users/john/Documents
/Users/john/Downloads
~/Downloads
```

After inputting a valid directory input, then you will be prompted with a `Sorting...`; once, sorting is finished, then `Done!` will be appended.
```
Sorting...Done!
```

### Full example:
```
$ python3 .
Enter which directory to sort (`.` for the current directory or `CTRL+C` to quit): ~/Downloads
Sorting...Done!
$
```