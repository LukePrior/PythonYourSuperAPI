# Python YourSuper API

Python wrapper for the Australian Taxation Office [YourSuper API](https://www.ato.gov.au/YourSuper-Comparison-Tool/)

## Installation 

```python
pip install YourSuperAPI
```

## Available Options

### amountRange (default=All)

Indicate how many results to return accepts integer between 1 and 9999 or array of two values to indicate range to return.

### age (default=0)

Positive integer less than 100 to set account holder age.

### balance (default=50000)

Positive Integer or Float value to set account balance, used to determine fees for each product.

### private (default=False)

Boolean value to determine if private super funds will be returned.

### performance (default=0)

Integer value to determine what [performance tested](https://www.apra.gov.au/quarterly-superannuation-statistics) super funds will be returned.
- 0 (return all super funds)
- 1 (return only super funds assessed to meet benchmark)
- 2 (return only super funds assessed to fail benchmark)
- 3 (return only super funds not assessed)


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

data = YourSuperAPI.get_data(private=True)

print(data)
```

### Fetch underperforming funds

```python
from YourSuperAPI import YourSuperAPI

data = YourSuperAPI.get_data(performance=2)

print(data)
```

## Advanced Examples

### Print 7 year net returns for public funds with $200,000 balance and 50 year old account holder

```python
from YourSuperAPI import YourSuperAPI

data = YourSuperAPI.get_data(private=True, age=50, balance=200000)

for superfund in data:
    print(superfund["superannuationProviderProductName"])
    for subproduct in superfund["subProduct"]:
        print(subproduct["fundNetReturnLastSevenYearsPercentageNumber"])
```

## Data Structure

The API returns a Python list of super funds, the structure of each of these funds follows:

```
{
  'performanceRatingCode': 'Performing', 
  'superannuationProviderDetailFundName': 'QSuper', 
  'superannuationProviderProductName': 'QSuper Lifetime', 
  'subProduct': [{
    'lifeCycleStageName': 'Focus 1 Group', 
    'fundNetReturnLastSevenYearsPercentageNumber': 7.98, 
    'fundNetReturnLastFiveYearsPercentageNumber': 7.37, 
    'fundNetReturnLastThreeYearsPercentageNumber': 8.2, 
    'privateFundIndicator': 'N', 
    'adminFeesDisclosedAmount': 80.0, 
    'riskLevelCode': 'Medium', 
    'internetURLAddress': 'https://qsuper.qld.gov.au/our-products/investment-options/lifetime', 
    'superannuationFundInvestmentStrategyTypeCode': 'Lifecycle', 
    'superannuationProductSubproductID': 724652609, 
    'investmentFeesDisclosedAmount': 195.0, 
    'totalFeesDisclosedAmount': 275.0
  }]
}
```
