# ZipLs

A practical tool that lists all the files in a compressed archive (zip, rar, 7zip) and saves this information to a JSON file.

## Installation

You can **use executable files from [release page](https://github.com/Ljzd-PRO/zipls/releases/)** or follow steps below. 

1. (Optional)Prepare a python virtual environment.
2. Install requirements (`requirements.txt`).
    - `pip install requirements.txt`
3. Run the tool.
    - `python -m zipls`

## Usage

### 📌 Print files information from zip files

```shell
zipls ls [Zip File]...
```

Example:
```shell
zipls ls /path/to/data.zip
zipls ls data.zip data1.zip data2.zip
zipls ls *.zip
```

### 📌 Dump files information to a file

```shell
zipls dump [Output File] [Zip File]...
```

Example:
```shell
zipls dump ./info.json /path/to/data.zip
zipls dump info.json data.zip data1.zip data2.zip
zipls dump info.json *.zip
```

### 📌 Dump JSON Schema of `ZipLsInfo`

> JSON Schema enables the confident and reliable use of the JSON data format. \
> https://json-schema.org/

```shell
zipls schema [Schema File]
```

Example:
```shell
zipls schema ./schema.json
```

### 📌 Get All Usage

```shell
zipls --help
```

```shell
zipls [COMMAND] --help
```

Example:
```shell
zipls -h
zipls ls -h
```

### 📌 ZipLs version

```shell
zipls version
```

## License

ZipLs is licensed under BSD 3-Clause.

Copyright © 2024 by Ljzd-PRO.
