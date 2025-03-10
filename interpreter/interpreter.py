#prompt the user for input
expression = input("Expression: ")
x, y, z = expression.split(" ")
x = int(x)
z = int(z)
#if else case for different expressions
match y:
    case "+":
        print(f"{(x + z):.1f}")
    case "-":
        print(f"{(x - z):.1f}")
    case "*":
        print(f"{(x * z):.1f}")
    case "/":
         print(f"{(x / z):.1f}")
    case _:
        print("WRONG EXPRESSION!!!")