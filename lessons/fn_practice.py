"""Example functions to learn definition and alling syntax"""

def my_max(number1: int, number2: int) -> int:
    """returns the maximum value out two numbers"""
    if number1 >= number2:
        return number1
    else: #number1 < number2
        return number2
    
max_number: int = my_max(1,10)
other_max_numver: int = my_max(11,3)
print(max_number)
