# Name: Sunmi Kim
# Date: 05/09/2023
# Class: Object Oriented Programming with Python

class Temperature:
    def __init__(self, fahrenheit, celsius):
        self.__fahrenheit = fahrenheit
        self.__celsius = celsius

    @property
    def fahrenheit(self):
        return self.__fahrenheit
    
    @fahrenheit.setter
    def fahrenheit(self, newFahrenheit):
        if not isinstance(newFahrenheit, (int, float)):
            raise ValueError("Fahrenheit must be a number.")
        self.__fahrenheit = newFahrenheit

    def to_fahrenheit(self, celsius=None):
        if celsius is None:
            celsius = self.__celsius
        return (celsius * 9/5) + 32
    
    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, newCelsius):
        if not isinstance(newCelsius, (int, float)):
            raise ValueError("Celsius must be a number.")
        self.__celsius = newCelsius
    
    def to_celsius(self, fahrenheit=None):
        if fahrenheit is None:
            fahrenheit = self.__fahrenheit
        return (fahrenheit - 32) * 5/9
    
    def convert_temp(self):
        option = input("\t1. Celsius to Fahrenheit\n\t2. Fahrenheit to Celsius \n\nEnter a menu option (1 or 2): ")
        if option == str(1):
            c = input("Enter degrees Celsius: ")
            if not c.isnumeric():
                print("Degrees Celsius must be a number.")
                return
            c = float(c)
            f = self.to_fahrenheit(c)
            f = round(f, 2)
            print("Degrees Fahrenheit:", f)    
        elif option == str(2):
            f = input("Enter degrees Fahrenheit: ")
            if not f.isnumeric():
                print("Degrees Fahrenheit must be a number.")
                return
            f = float(f)
            c = self.to_celsius(f)
            c = round(c, 2)
            print("Degrees Celsius:", c)
        else:
            print("You must enter a valid number.")
