# Password Generator

Simple password generator Cli with Python.

## Usage

```python
# Print help command
python password_generator.py -h
```

```python
# Generate password with 20 lowercase letters
python password_generator.py -l 20 -a
python password_generator.py -l 20 --alpha
```

```python
# Generate password with 20 lowercase letters and numbers
python password_generator.py -l 10 -a -n
python password_generator.py -l 10 -a --numbers
```

```python
# Generate 10 passwords with 10 characters. include all possible character
python password_generator.py -l 10 -a -A -n -s -m 10
```
