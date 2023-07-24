
# PyFaudit

PyFaudit is a Python utility to scan Python files in a directory (and its subdirectories), check for encoding issues, and provide a summary of the files scanned.

## Installation

You can install PyFaudit with pip:
`pip install PyFaudit`


## Usage

You can use PyFaudit from the command line or import it in your Python script.

### Command line

Run PyFaudit from the command line like this:
`PyFaudit /path/to/your/directory`

For verbose output, use the `-v` or `--verbose` option:
`PyFaudit /path/to/your/directory --verbose`


### Python script

Here is how to use PyFaudit in a Python script or Jupyter notebook:

```python
from PyFaudit import scan_files

total_files, total_size, problem_files = scan_files('/path/to/your/directory')
```
The scan_files function returns a tuple containing the total number of files scanned,
the total size of scanned files in bytes, and a list of paths to the files that
caused a UnicodeDecodeError.
