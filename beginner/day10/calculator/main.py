from art import logo
#Calculator
#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiple
def multiple(n1, n2):
  return n1 * n2

#Divide
def devide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiple,
  "/": devide,
}

def caculator():
  print(logo)
  
  num1 = float(input("What is the first number? "))
  
  for symbol in operations:
    print(symbol)
  
  is_continue = True
    
  while is_continue:
    operation_symbol = input("Pick a operation: ")
    num2 = float(input("What is the next number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculator.: ")
  
    if choice == "y":
      is_continue = True
      num1 = answer
    else:
      is_continue = False
      caculator()
    

caculator()