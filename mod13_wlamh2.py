#validation.py
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

# test_validation.py
from validation import (
    ValidSymbol,
    ValidChartType,
    ValidTimeSeries,
    ValidDate
)
#symbol tests
def test_CorrectSymbol():
    assert ValidSymbol("AAPL")==True
    assert ValidSymbol("GOOGL")==True
def test_WrongSymbolLowercase():
    assert ValidSymbol("aapl")==False
def test_WrongSymbolTooLong():
    assert ValidSymbol("ABCDEFGH")==False
def test_WrongSymbolNumbers():
    assert ValidSymbol("AAPL1")==False
#chart tests
def test_CorrectChartType():
    assert ValidChartType("1")==True
    assert ValidChartType("2")==True
def test_WrongChartType():
    assert ValidChartType("0")==False
    assert ValidChartType("3")==False
    assert ValidChartType("line")==False
#time series tests
def test_CorrectTimeSeries():
    assert ValidTimeSeries("1")==True
    assert ValidTimeSeries("2")==True
    assert ValidTimeSeries("3")==True
    assert ValidTimeSeries("4")==True
def test_WrongTimeSeries():
    assert ValidTimeSeries("0")==False
    assert ValidTimeSeries("5")==False
    assert ValidTimeSeries("daily")==False
#date tests
def test_CorrectDate():
    assert ValidDate("2024-01-10")==True
def test_WrongDateFormat():
    assert ValidDate("01-10-2024")==False
    assert ValidDate("2024/01/10")==False
def test_WrongActualDate():
    assert ValidDate("2024-13-01")==False
    assert ValidDate("2024-02-30")==False
