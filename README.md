# PythonYourSuperAPI

Python wrapper for the Australian Taxation Office YourSuper API

## Installation 

```python
pip install YourSuperAPI
```

## Examples

### Fetch all products

```python
from YourSuperAPI import YourSuperAPI

data = YourSuperAPI.get_data()

print(data)
```

### Fetch first 5 products

```python
from YourSuperAPI import YourSuperAPI

data = YourSuperAPI.get_data(amountRange=5)

print(data)
```

### Fetch 10th - 20th products

```python
from YourSuperAPI import YourSuperAPI

data = YourSuperAPI.get_data(amountRange=[10,20])

print(data)
```

### Fetch with custom account balance ($1000.56)

```python
from YourSuperAPI import YourSuperAPI

data = YourSuperAPI.get_data(balance=1000.56)

print(data)
```

### Fetch without private funds

```python
from YourSuperAPI import YourSuperAPI

data = YourSuperAPI.get_data(private=False)

print(data)
```
