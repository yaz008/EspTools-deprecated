![logo](assets/esptools-logo.png)

# EspTools

EspTools is an extenive toolset for [Espanso](https://espanso.org/)

**Version:** `0.1.0-alpha`

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

**Check the installation:** Type `:esptools` in any text field. If everything is set up correctly, it should be replaced with `Hello, EspTools!`

## Usage

Place your cursor in any text field and type a command, it will be executed and replaced with the result

**For, example:** `=2 ** 31 - 1;` -> `2147483647`

Read the [Documentation](docs/DOC.md) to learn more

## License

EspTools is a free, open-source software distributed under the [MIT License](LICENSE.txt)
