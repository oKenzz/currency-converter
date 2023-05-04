# Methods: 
#   convertCurrency
#   GetRates


# def convertCurrency(baseCurrency:str, toCurrency:str, baseValue:float):
#     rate = getRates(baseCurrency)
#     newValue = baseValue * rate[toCurrency]
#     return newValue

def convertCurrency(baseValue:float):
    newValue = float(baseValue) * 10.25
    return newValue


def getRates(baseCurrency):
    # Make request to api with baseCurrency
    # Return json data
    return 0



