![logo](assets/esptools-logo.png)

# EspTools

EspTools is an extenive toolset for [Espanso](https://espanso.org/)

## Prerequisites

* [Espanso](https://espanso.org/): Version 2.2.1
* [Python](https://www.python.org/): Version 3.12

## Installation

Close the repository

```sh
git clone --branch v0.1.0-alpha https://github.com/yaz008/esptools
```

Navigate to the Espanso `match` directory and copy the `esptools.yml` file there

Replace `[python]` with the full path to your Python 3.12 interpreter and `[main]` with the full path to the `src\main.py` file within the cloned esptools directory

Restart Espanso or reload its configs to ensure that the new match is loaded

**Check the installation:** type `:esptools` in any text field. If everything is set up correctly, it should be replaced with `Hello, EspTools!`

## Usage

Type `=` followed by an expression and a `;` at the end

The expression will be evaluated and replaced with the result

For example: `=sqrt(37);` -> `6.082762530298219`

**Note:** Espanso matches [patterns](https://espanso.org/docs/matches/regex-triggers/) of up to 30 characters long — make sure your expressions stay within this length

## License

EspTools is a free, open-source software distributed under the [MIT License](LICENSE.txt)
