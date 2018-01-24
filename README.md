# Closest bars

The script analyzes the .json file with the data about the Moscow bars ([data.mos.ru](https://data.mos.ru/)) and finds the largest, the smallest and nearest bars in relation to entered coords.

# Running

The script requires the installed Python interpreter version 3.5.

Running on Linux:

```bash

$ python bars.py bars.json # possibly requires call of python3 executive instead of just python
The biggest bar is Спорт бар «Красная машина»
The smallest bar is БАР. СОКИ
Coordinates: 38 90 # input coords here
The closest bar is Гудсон бар

```

Running on Windows is similar.

# Project Goals

The code was created for training purposes in the web development training course - [DEVMAN.org](https://devman.org).
