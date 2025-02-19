def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculate():
    """accepts 2 numbers, operator and calculates result. Can loop to continue calculating with
    this result or start new calculation"""
    accumulate = True
    n1 = float(input("what is the first number?"))
    while accumulate:
        operator = input("What is the math operator? + - * /")
        n2 = float(input("what is the second number?"))
        result = calculator[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {result}")

        carry_on = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or anything else to finish").lower()
        if carry_on == "y":
            n1 = result
        elif carry_on == "n":
            accumulate = False
            calculate()
        else:
            accumulate = False

#math operators dictionary
calculator = {"+":add,
              "-":subtract,
              "*":multiply,
              "/":divide,
              }

#start program
calculate()