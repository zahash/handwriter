# HandWriter

> Text to Handwriting converter

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

A simple Python program that takes the text inside a .txt file and converts it into handwritten .pdf file

![header.png](assets/header.png)

## Installation

First, Download and Install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)

then, pip install this repo.
(Note: Incompatible with Python 2.x)

```sh
pip3 install git+https://github.com/zahash/handwriter.git

(or)

pip install git+https://github.com/zahash/handwriter.git
```

## Usage example

To get help with commandline arguments

```sh
python3 -m handwriter --help
```

Using Command-line Arguments

```sh
python3 -m handwriter -i "some/folder/mytext.txt" -o "other/folder/myoutput.pdf" -s "set1"
```

## Development setup

This project uses pytest. Clone this repo and install packages listed in requirements.dev.txt

```sh
pip3 install -r requirements.dev.txt
```

## Meta

M. Zahash – zahash.z@gmail.com

Distributed under the AGPLv3 license. See `LICENSE` for more information.

[https://github.com/zahash/](https://github.com/zahash/)

## Contributing

1. Fork it (<https://github.com/zahash/handwriter/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
