# simple calculator
def calculator(a: int, b: float):
  sum = a + b
  diff = a - b
  mul = a * b

  if b != 0:
    div = a / b
    mod = a % b
    
  else:
    div = "undefined"
    mod = "undefined"
    
  print("sum of 2 numbers: ", sum)
  print("diff of 2 numbers: ", diff)
  print("mul of 2 numbers: ", mul)
  print("division of 2 numbers: ", div)
  print("modulus of 2 numbers: ", mod)

def main():
  try:
      x = int(input("Enter an integer: "))
      y = float(input("Enter a float: "))
      calculator(x, y)
  except ValueError:
        print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    main()

  
