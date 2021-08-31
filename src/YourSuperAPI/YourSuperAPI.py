import json
import requests
from requests.structures import CaseInsensitiveDict

performanceList = ["All", "Performing", "Underperforming", "Not%20Assessed"]


def get_data(amountRange=9999, age=0, balance=50000, private=False, performance=0):

    # Number of products to return
    if isinstance(amountRange, int) and 0 < amountRange <= 9999:
        amountStart = 0
        amountEnd = amountRange
    elif isinstance(amountRange, list) and len(amountRange) == 2 and isinstance(amountRange[0], int) and isinstance(
            amountRange[1], int) and 0 <= amountRange[0] < amountRange[1] <= 9999:
        amountStart = amountRange[0]
        amountEnd = amountRange[1]
    else:
        amountStart = 0
        amountEnd = 9999

    # Age of account holder
    if isinstance(age, int) and 0 <= age <= 99:
        individualAgeNumber = str(age)

    # Balance of account holder
    if (isinstance(balance, int) or isinstance(balance, float)) and balance >= 0:
        superannuationIndividualAccountBalanceAmount = format(round(balance, 2), '.2f')

    # Show private funds
    if isinstance(private, bool):
        privateFundsExcludedIndicator = str(private)

    # Filter Performance Rating
    if isinstance(performance, int):
        if 0 <= performance <= len(performanceList):
            performanceRatingCode = performanceList[performance]
        else:
            performanceRatingCode = performanceList[0]

    url = "https://www.ato.gov.au/api/v1/YourSuper/APRAData?Filter='clientIdentifierTypeCode=0,clientIdentifierValueID=0,individualAgeNumber=" + individualAgeNumber + ",performanceRatingCode=" + performanceRatingCode + ",privateFundsExcludedIndicator=" + privateFundsExcludedIndicator + ",retrieveAllProductsIndicator=False,superannuationIndividualAccountBalanceAmount=" + superannuationIndividualAccountBalanceAmount + "'"

    headers = CaseInsensitiveDict()
    headers["range"] = "items=" + str(amountStart) + "-" + str(amountEnd)

    resp = requests.get(url, headers=headers)

    data = json.loads(resp.content)

    return data["response"]["fundProduct"]
