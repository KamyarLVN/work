again = ""
while again != "yes" or again != "no":

  again = input("do you wanna start?(yes or no): ")
  if again == "no":
      print("happy to help come back anytime")
  else:
    while again == "yes":
  
      first_num = float(input("enter first number: "))
      second_num = float(input("enter second number: "))
      operator = input("enter your operator + , - , /, *: ")
      if operator == "+":
          print(first_num + second_num)
      elif operator == "-":
          print(first_num - second_num)
      elif operator == "*":
          print(first_num * second_num)
      elif operator == "/":
         if second_num == 0:
            print("not able to operate")
         else:
            print(first_num / second_num)
      else:
          print("operation failed not able to read")
      again = input("do you wanna go again?(yes or no): ")
      if again == "no":
        print("happy to help come back anytime")
        break
  
