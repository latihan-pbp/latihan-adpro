class Calculator:

    def power(self, a, b):
        return a**b
    
if __name__ == "__main__":
    calc = Calculator()
    print("Power: ", calc.power(10, 5))