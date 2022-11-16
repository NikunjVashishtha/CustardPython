'''CustardPython is a library of custom python functions and methods that do not exist in Python by-default.

It provides all functions of your need at one place'''

from os import system, name
from time import sleep
import math
from datetime import date

# Custom Dictionary Functions
class cusDict:
    '''Custom dictionary functions from CustardPython.'''

    @staticmethod
    def alterKey(DictionaryName: dict, OldKey: str, NewKey: str):
        '''Switches the key of a dictionary value to a new one.'''

        mainDict = dict(DictionaryName)
        newDict = {}
        for dictKey in mainDict.keys():
            if mainDict[dictKey] == mainDict[OldKey]:
                newDict[NewKey] = mainDict[dictKey]
            else:
                newDict[dictKey] = mainDict[dictKey]
            print(dictKey)
        return newDict

    @staticmethod
    def insertBefore(DictionaryName: dict, PreviousKey: str, Key: str, Value: str):
        '''Inserts a dictionary element before a chosen element.'''
        
        mainDict = dict(DictionaryName)
        newDict = {}
        for dictKey in mainDict.keys():
            if mainDict[dictKey] == mainDict[PreviousKey]:
                newDict[Key] = Value
            newDict[dictKey] = mainDict[dictKey]
        return newDict
    
class cusList:
    '''Custom list functions from CustardPython.'''

    @staticmethod
    def reverse(ListName: list):
        '''Reverses a list.'''

        mainList = list(ListName)
        newList = mainList[::-1]
        return newList

class cusScr:
    '''Custom functions for program screen output from CustardPython.'''

    @staticmethod
    def clear():
        '''Clears the terminal while program is running.'''

        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
    
    @staticmethod
    def typeWrite(String: str,Delay: float):
        '''String is the text to be printed; Delay is the time between two consecutive text prints.'''
        
        for ltr in String:
            print(ltr,end="",flush=True)
            sleep(Delay)
        print()

class cusShape:
    '''Draw shapes on your screen with a symbol.'''

    @staticmethod
    def triangle(Side: int,Element: str):
        '''Side(int) is the length of side of equilateral triangle.'''

        for i in range(1,Side+1):
            print(" "*(Side+1-i),end="")
            for j in range(0,i):
                print(f"{Element} ",end="")
            print()
    
    @staticmethod
    def square(Side: int,Element: str):
        '''Side(int) is the length of side of square.'''

        for i in range(1,Side):
            for j in range(1,Side):
                print(f"{Element} ",end="")
            print()

    @staticmethod
    def hexagon(Side: int, Element: str):
        '''Side(int) is the length of side of hexagon.'''

        for i in range(Side,2*Side-1):
            print(" "*(2*Side-1-i),end="")
            for j in range(0,i):
                print(f"{Element} ",end="")
            print()
        for i in range(2*Side-1,Side-1,-1):
            print(" "*(2*Side-1-i),end="")
            for j in range(0,i):
                print(f"{Element} ",end="")
            print()

class cusDate:
    '''Custom date functions'''

    @staticmethod
    def date(Format: str,Year: int = date.today().year, Month: int = date.today().month,Day: int = date.today().day) :
        '''
        Returns a date in a given format

        MM/DD/YYYY

        DD/MM/YYYY

        YYYY/MM/DD

        Month Day(31), Year

        Weekday Day(31)
        '''

        days = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
        months = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
        dateUsed = date(Year,Month,Day)
        year = dateUsed.year
        month = dateUsed.month
        monthName = months[month]
        dat = dateUsed.day
        day = dateUsed.weekday()
        dayName = days[day]
        mainDate = ""
        if Format == "MM/DD/YYYY":
            mainDate = f"{month}/{dat}/{year}"
        elif Format == "DD/MM/YYYY":
            mainDate = f"{dat}/{month}/{year}"
        elif Format == "YYYY/MM/DD":
            mainDate = f"{year}/{month}/{dat}"
        elif Format == "Month Day(31), Year":
            mainDate = f"{monthName} {dat}, {year}"
        elif Format == "Weekday Day(31)":
            mainDate = f"{dayName} {dat}"
        return mainDate

class cusMath:
    '''Custom Math functions from CustardPython.'''

    @staticmethod
    def Collatz(Number: float,PrintSteps: bool = False):
        '''Number(int) is the starting number, PrintSteps(Default: False) prints intemediate numbers.'''
        
        if PrintSteps == True:
            print(Number)
        i = 1
        while Number != 1:
            if Number%2 == 0:
                Number /= 2
            else:
                Number = (Number * 3)+1
            if PrintSteps == True:
                print(int(Number))
            i += 1
        steps = i
        return steps
    
class cusChem:
    '''Some chemisty concepts made easier with CustardPython.'''

    @staticmethod
    def emp(Formula: str) -> str:
        '''Instructions:\

    1. Don't leave any space between Elements and Numbers.\
    
        Eg: H2O2 (For Hydrogen Peroxide)\
        
    2. In case the number of atoms of Element if one then it must be followed by \"1\".\
        
        Eg: Mg1Cl2 (For Magnesium Chloride)
        '''

        chars = []
        nums = []
        newNums = []
        elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si',
            'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni',
            'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb',
            'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
            'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho',
            'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
            'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np',
            'Pu', 'Am', 'Cu', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg',
            'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
        formula = Formula+"A"
        num = ""
        alpha = ""
        for a in formula:
            if a.isdigit():
                num += a
                if alpha != "":
                    if alpha.capitalize() in elements:
                        chars.append(alpha.capitalize())
                    else:
                        ValueError("Invalid chemical formula !")
                alpha = ""
            elif a.isalpha():
                alpha += a
                if num != "":
                    nums.append(num)
                num = ""
            else:
                ValueError("Invalid chemical formula !")
        i = 0
        while i < len(nums):
            nums[i] = int(nums[i])
            i += 1
        gcd = math.gcd(*nums)
        for a in nums:
            if int(a)/gcd == 1:
                newNums.append("")
            else:
                newNums.append(int(int(a)/gcd))
        i = 0
        newFormula = ""
        while i < len(chars):
            newFormula += chars[i]+str(newNums[i])
            i += 1
        return newFormula