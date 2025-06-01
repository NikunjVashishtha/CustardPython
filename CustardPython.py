'''CustardPython is a library of custom Python utility functions and methods that extend the standard library.

It provides a collection of helpful functions for everyday programming tasks.'''

from os import system, name
from time import sleep
import math
from datetime import date

# Enhanced Dictionary Utilities
class DictionaryUtils:
    '''Enhanced dictionary utility functions for key manipulation and insertion.'''

    @staticmethod
    def rename_key(dictionary: dict, old_key: str, new_key: str) -> dict:
        '''Return a new dictionary with the specified key renamed.
        
        Args:
            dictionary (dict): The original dictionary.
            old_key (str): The key to rename.
            new_key (str): The new key name.
        
        Returns:
            dict: A new dictionary with the key renamed.
        '''
        main_dict = dict(dictionary)
        new_dict = {}
        for key in main_dict:
            if key == old_key:
                new_dict[new_key] = main_dict[key]
            else:
                new_dict[key] = main_dict[key]
        return new_dict

    @staticmethod
    def insert_before(dictionary: dict, before_key: str, insert_key: str, insert_value) -> dict:
        '''Return a new dictionary with a key-value pair inserted before a specified key.
        
        Args:
            dictionary (dict): The original dictionary.
            before_key (str): The key before which to insert.
            insert_key (str): The key to insert.
            insert_value: The value to insert.
        
        Returns:
            dict: A new dictionary with the key-value pair inserted.
        '''
        main_dict = dict(dictionary)
        new_dict = {}
        inserted = False
        for key in main_dict:
            if key == before_key and not inserted:
                new_dict[insert_key] = insert_value
                inserted = True
            new_dict[key] = main_dict[key]
        if not inserted:
            new_dict[insert_key] = insert_value
        return new_dict

    @staticmethod
    def merge(dict1: dict, dict2: dict) -> dict:
        '''Merge two dictionaries. Values from dict2 overwrite those from dict1 if keys overlap.
        
        Args:
            dict1 (dict): The first dictionary.
            dict2 (dict): The second dictionary.
        
        Returns:
            dict: The merged dictionary.
        '''
        result = dict(dict1)
        result.update(dict2)
        return result

    @staticmethod
    def filter_by_key(dictionary: dict, predicate) -> dict:
        '''Filter dictionary by key using a predicate function.
        
        Args:
            dictionary (dict): The dictionary to filter.
            predicate (callable): Function that takes a key and returns True/False.
        
        Returns:
            dict: Filtered dictionary.
        '''
        return {k: v for k, v in dictionary.items() if predicate(k)}

    @staticmethod
    def filter_by_value(dictionary: dict, predicate) -> dict:
        '''Filter dictionary by value using a predicate function.
        
        Args:
            dictionary (dict): The dictionary to filter.
            predicate (callable): Function that takes a value and returns True/False.
        
        Returns:
            dict: Filtered dictionary.
        '''
        return {k: v for k, v in dictionary.items() if predicate(v)}

    @staticmethod
    def invert(dictionary: dict) -> dict:
        '''Invert keys and values in a dictionary.
        
        Args:
            dictionary (dict): The dictionary to invert.
        
        Returns:
            dict: Inverted dictionary.
        '''
        return {v: k for k, v in dictionary.items()}

# Enhanced List Utilities
class ListUtils:
    '''Enhanced list utility functions for common list operations.'''

    @staticmethod
    def reversed_list(lst: list) -> list:
        '''Return a new list that is the reverse of the input list.
        
        Args:
            lst (list): The list to reverse.
        
        Returns:
            list: The reversed list.
        '''
        return list(lst)[::-1]

    @staticmethod
    def flatten(nested_list: list) -> list:
        '''Flatten a nested list into a single list.
        
        Args:
            nested_list (list): The list to flatten.
        
        Returns:
            list: The flattened list.
        '''
        flat = []
        for item in nested_list:
            if isinstance(item, list):
                flat.extend(ListUtils.flatten(item))
            else:
                flat.append(item)
        return flat

    @staticmethod
    def deduplicate(lst: list) -> list:
        '''Remove duplicates from a list while preserving order.
        
        Args:
            lst (list): The list to deduplicate.
        
        Returns:
            list: The deduplicated list.
        '''
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    @staticmethod
    def chunk(lst: list, size: int) -> list:
        '''Split a list into chunks of a given size.
        
        Args:
            lst (list): The list to chunk.
            size (int): The chunk size.
        
        Returns:
            list: A list of chunks (lists).
        '''
        return [lst[i:i+size] for i in range(0, len(lst), size)]

    @staticmethod
    def rotate(lst: list, n: int) -> list:
        '''Rotate a list by n positions.
        
        Args:
            lst (list): The list to rotate.
            n (int): Number of positions to rotate.
        
        Returns:
            list: The rotated list.
        '''
        n = n % len(lst) if lst else 0
        return lst[n:] + lst[:n]

# Terminal Output Utilities
class TerminalUtils:
    '''Utility functions for terminal screen output and effects.'''

    @staticmethod
    def clear_screen():
        '''Clear the terminal screen.'''
        system('cls' if name == 'nt' else 'clear')
    
    @staticmethod
    def typewriter(text: str, delay: float):
        '''Print text to the terminal with a typewriter effect.
        
        Args:
            text (str): The text to print.
            delay (float): Delay in seconds between each character.
        '''
        for char in text:
            print(char, end="", flush=True)
            sleep(delay)
        print()

# ASCII Shape Drawing Utilities
class ShapeDrawer:
    '''Draw ASCII shapes on the terminal using a specified symbol.'''

    @staticmethod
    def draw_triangle(side_length: int, symbol: str):
        '''Draw an equilateral triangle of a given side length.
        
        Args:
            side_length (int): The length of each side.
            symbol (str): The symbol to use for drawing.
        '''
        for i in range(1, side_length+1):
            print(" "*(side_length+1-i), end="")
            print(f"{symbol} " * i)

    @staticmethod
    def draw_square(side_length: int, symbol: str):
        '''Draw a square of a given side length.
        
        Args:
            side_length (int): The length of each side.
            symbol (str): The symbol to use for drawing.
        '''
        for _ in range(side_length):
            print(f"{symbol} " * side_length)

    @staticmethod
    def draw_hexagon(side_length: int, symbol: str):
        '''Draw a hexagon of a given side length.
        
        Args:
            side_length (int): The length of each side.
            symbol (str): The symbol to use for drawing.
        '''
        for i in range(side_length, 2*side_length-1):
            print(" "*(2*side_length-1-i), end="")
            print(f"{symbol} " * i)
        for i in range(2*side_length-1, side_length-1, -1):
            print(" "*(2*side_length-1-i), end="")
            print(f"{symbol} " * i)

# Date Formatting Utilities
class DateUtils:
    '''Utility functions for formatting and manipulating dates.'''

    @staticmethod
    def formatted_date(fmt: str, year: int = date.today().year, month: int = date.today().month, day: int = date.today().day) -> str:
        '''
        Return a date string in the specified format.

        Supported formats:
            - MM/DD/YYYY
            - DD/MM/YYYY
            - YYYY/MM/DD
            - Month Day(31), Year
            - Weekday Day(31)
        '''
        days = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
        months = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
        date_used = date(year, month, day)
        year_val = date_used.year
        month_val = date_used.month
        month_name = months[month_val]
        day_val = date_used.day
        weekday = date_used.weekday()
        weekday_name = days[weekday]
        if fmt == "MM/DD/YYYY":
            return f"{month_val}/{day_val}/{year_val}"
        elif fmt == "DD/MM/YYYY":
            return f"{day_val}/{month_val}/{year_val}"
        elif fmt == "YYYY/MM/DD":
            return f"{year_val}/{month_val}/{day_val}"
        elif fmt == "Month Day(31), Year":
            return f"{month_name} {day_val}, {year_val}"
        elif fmt == "Weekday Day(31)":
            return f"{weekday_name} {day_val}"
        else:
            raise ValueError("Unknown date format")

# Math Utilities
class MathUtils:
    '''Mathematical utility functions for number theory and sequences.'''

    @staticmethod
    def collatz_steps(number: float, print_steps: bool = False) -> int:
        '''Compute the number of steps in the Collatz sequence for a given number.
        
        Args:
            number (float): The starting number.
            print_steps (bool): If True, print each step.
        
        Returns:
            int: The number of steps to reach 1.
        '''
        if print_steps:
            print(int(number))
        i = 1
        while number != 1:
            if number % 2 == 0:
                number /= 2
            else:
                number = number * 3 + 1
            if print_steps:
                print(int(number))
            i += 1
        return i

# Chemistry Utilities
class ChemistryUtils:
    '''Utility functions for basic chemistry calculations and formula manipulation.'''

    @staticmethod
    def empirical_formula(formula: str) -> str:
        '''
        Convert a molecular formula to its empirical formula.

        Instructions:
        1. Do not leave any space between elements and numbers.
           Eg: H2O2 (for hydrogen peroxide)
        2. If the number of atoms of an element is one, it must be followed by "1".
           Eg: Mg1Cl2 (for magnesium chloride)

        Args:
            formula (str): The molecular formula.

        Returns:
            str: The empirical formula.
        '''
        chars = []
        nums = []
        new_nums = []
        elements = [
            'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si',
            'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni',
            'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb',
            'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
            'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho',
            'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
            'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np',
            'Pu', 'Am', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg',
            'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og'
        ]
        formula = formula + "A"
        num = ""
        alpha = ""
        for a in formula:
            if a.isdigit():
                num += a
                if alpha:
                    if alpha.capitalize() in elements:
                        chars.append(alpha.capitalize())
                    else:
                        raise ValueError("Invalid chemical formula!")
                    alpha = ""
            elif a.isalpha():
                alpha += a
                if num:
                    nums.append(num)
                    num = ""
            else:
                raise ValueError("Invalid chemical formula!")
        if num:
            nums.append(num)
        if alpha and alpha.capitalize() in elements:
            chars.append(alpha.capitalize())
        if len(nums) != len(chars):
            raise ValueError("Invalid chemical formula!")
        nums = [int(x) for x in nums]
        gcd = math.gcd(*nums)
        for a in nums:
            val = int(a) // gcd
            new_nums.append("" if val == 1 else str(val))
        new_formula = ""
        for i in range(len(chars)):
            new_formula += chars[i] + new_nums[i]
        return new_formula