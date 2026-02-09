class Calculator:
    def modulo(self, c, d):
        return c % d

    if __name__ == "__main__":
        calc = Calculator()
        print("Modulo: ", calc.modulo(10, 5))