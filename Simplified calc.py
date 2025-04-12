print("Hello, there!")
print("Enter any two numbers to be calculated")
x = float(input("What is the first number?: "))
y = float(input("What's the second number?: "))
z = (input("What's the operation (+, -, *, /): 20"))
operation = f"Your request is {x} {z} {y}"
print(operation)
if z == "+" :
    result_calc = x + y
elif z == "-" :
    result_calc = x - y
elif z == "*" :
    result_calc = x * y
elif z == "/" :
    result_calc = x / y     
  
result = f"The results are {result_calc}"
print(result)
