python-tee
==========

[![Build Status](https://travis-ci.org/algrebe/python-tee.svg?branch=master)](https://travis-ci.org/algrebe/python-tee)
[![PyPI version](https://badge.fury.io/py/tee.svg)](https://badge.fury.io/py/tee)


Python library to tee stderr / stdout  to a file

## Installation

```bash
pip install tee
```

## Quick Start

`tee_test.py`

```python
import sys
from tee import StdoutTee, StderrTee

with StdoutTee("mystdout.txt"), StderrTee("mystderr.txt"):
    sys.stdout.write("[stdout] hello\n")
    sys.stderr.write("[stderr] hello\n")
    sys.stdout.write("[stdout] world\n")
    sys.stderr.write("[stderr] world\n")

sys.stdout.write("[stdout] not going to be written to file\n")
sys.stderr.write("[stderr] not going to be written to file\n")
```

```bash
$ python tee_test.py

[stdout] hello
[stderr] hello
[stdout] world
[stderr] world
[stdout] not going to be written to file
[stderr] not going to be written to file

$ cat mystdout.txt 
[stdout] hello
[stdout] world

$ cat mystderr.txt 
[stderr] hello
[stderr] world
```

## Filters

StdoutTee and StderrTee take filters as parameters which run before writing to a file or the stream. These filters are callables that take the message to be written as input and return either None or a new message.

I find them particularly useful when you want to write colorized output to the stream, but strip out the control characters when writing to a file, especially when using fabric.

```python
import re
import tee
from fabric.api import run

def _remove_control_chars(message):
    return re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]', "", message)

def echo_color():
    with tee.StdoutTee("fabout.txt", mode="a", file_filters=[_remove_control_chars]):
        run("""echo -e "\E[1;32mHello World \E[4;31mLets add some\E[0m\E[1;34m color" && tput sgr0""")
```

```bash
fab -H localhost echo_color
```
