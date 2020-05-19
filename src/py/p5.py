# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.

class InputOutString:
    def __init__(self):
        self.str = ""
    def getString(self):
        self.str= input("Please enter a string:- ")
    def printString(self):
        print(f"The upper case of string entered by user is {self.str.upper()}")

strObj = InputOutString()
strObj.getString()
strObj.printString()