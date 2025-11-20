from datetime import datetime

def ValidSymbol(symbol: str):
    return (
        symbol.isalpha() and symbol.isupper() and 1<=len(symbol)<=7
    )

def ValidChartType(choice: str):
    return choice in ["1","2"]

def ValidTimeSeries(choice: str):
    return choice in ["1","2","3","4"]

def ValidDate(date_str: str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
