# redis-mass-insertion

Lightweight Python script to prepare Redis commands for mass insertion using redis-cli --pipe.

## Usage

redis-mass.py can be used in two ways, either way assumes input with the following format.

```
SET key value
SET key2 value2
SADD someset value
SADD someset value2
SADD someset value3 value4
```

You can specify a file to the script as a command-line argument

```sh
python redis-mass.py input.txt | redis-cli --pipe
```

or pipe input from stdin

```sh
cat input.txt | python redis-mass.py | redis-cli --pipe
```
