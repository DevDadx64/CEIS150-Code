# Author: Miller Emion
# Date: 2023-11-03

class Stock:
    # init class attributes
    def __init__(self, name, symbol, share):
        self.name = name
        self.symbol = symbol
        self.share = share
        self.DataList = []
    # Mehtod to append stockData to DataList
    def addData(self, stockData):
        self.DataList.append(stockData)

class DailyData:
    # init class attributes
    def __init__(self, date, close, volume):
        self.date = date
        self.close = close
        self.volume= volume
    
# Unit Test - Do Not Change Code Below This Line *** *** *** *** *** *** *** *** ***
# main() is used for unit testing only. It will run when stock_class.py is run.
# Run this to test your class code. Once you have eliminated all errors, you are
# ready to continue with the next part of the project.
def main():
    error_count = 0
    error_list = []
    print("Unit Testing Starting---")
    # Test Add Stock
    print("Testing Add Stock...",end="")
    try:
        testStock = Stock("TEST","Test Company",100)
        print("Successful!")
    except:
        print("***Adding Stock Failed!")
        error_count = error_count+1
        error_list.append("Stock Constructor Error")
    
    # Test Change Symbol
    print("Test Change Symbol...",end="")
    try:
        testStock.symbol = "NEWTEST"
        if testStock.symbol == "NEWTEST":
            print("Successful!")
        else:
            print("***ERROR! Symbol change unsuccessful.")
            error_count = error_count+1
            error_list.append("Symbol Change Error")
    except:
        print("***ERROR! Symbol change failed.")
        error_count = error_count+1
        error_list.append("Symbol Change Failure")
        print("Test Change Name...",end="")
    try:
        testStock.name = "New Test Company"
        if testStock.name == "New Test Company":
            print("Successful!")
        else:
            print("***ERROR! Name change unsuccessful.")
            error_count = error_count+1
            error_list.append("Name Change Error")
    except:
        print("***ERROR! Name change failed.")
        error_count = error_count+1
        error_list.append("Name Change Failure")
        print("Test Change Name...",end="")
    try:
        testStock.shares = 2000
        if testStock.shares == 2000:
            print("Successful!")
        else:
            print("***ERROR! Shares change unsuccessful.")
            error_count = error_count+1
            error_list.append("Shares Change Error")
    except:
        print("***ERROR! Shares change failed.")
        error_count = error_count+1
        error_list.append("Shares Change Failure")

    # Test add daily data
    print("Creating daily stock data...",end="")
    daily_data_error = False
    try:
        dayData = DailyData("1/1/20",float(14.50),float(100000))
        testStock.addData(dayData)
        if testStock.DataList[0].date != "1/1/20":
            error_count = error_count + 1
            daily_data_error = True
            error_list.append("Add Daily Data - Problem with Date") 
        if testStock.DataList[0].close != 14.50:
            error_count = error_count + 1
            daily_data_error = True
            error_list.append("Add Daily Data - Problem with Closing Price")
        if testStock.DataList[0].volume != 100000:
            error_count = error_count + 1
            daily_data_error = True
            error_list.append("Add Daily Data - Problem with Volume")
    except:
        print("***ERROR! Add daily data failed.")
        error_count = error_count + 1
        error_list.append("Add daily data Failure!")
        daily_data_error = True
    if daily_data_error == True:
        print("***ERROR! Creating daily data failed.")
    else:
        print("Successful!")
    if (error_count) == 0:
        print("Congratulations - All Tests Passed")
    else:
        print("-=== Problem List - Please Fix ===-")
    for em in error_list:
        print(em)
        print("Goodbye")
# Program Starts Here
if __name__ == "__main__":
# run unit testing only if run as a stand-alone script
    main()