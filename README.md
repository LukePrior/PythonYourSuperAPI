# PythonYourSuperAPI

Python wrapper for the Australian Taxation Office [YourSuper API](https://www.ato.gov.au/YourSuper-Comparison-Tool/)

## Installation 

```python
pip install YourSuperAPI
```

## Available Options

### amountRange (default=9999)

Indicate how many results to return accepts integer between 1 and 9999 or array of two values to indicate range to return.

### age (default=0)

Positive integer less than 100 to set account holder age.

### balance (default=50000)

Positive Integer or Float value to set account balance, used to determine fees for each product.

### private (default=False)

Boolean value to determine if private super funds will be returned.

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

### Fetch with custom account holder age (42 years)

```python
from YourSuperAPI import YourSuperAPI

data = YourSuperAPI.get_data(age=42)

print(data)
```

### Fetch without private funds

```python
from YourSuperAPI import YourSuperAPI

data = YourSuperAPI.get_data(private=False)

print(data)
```
