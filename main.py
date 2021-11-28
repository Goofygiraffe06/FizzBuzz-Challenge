num = int(input("Enter Number: "))

if num % 15 == 0: #Lcm of 3 & 5
  print("Fizz Buzz!") 
elif num % 3 == 0:
  print("Fizz!")
elif num % 5 == 0:
  print("Buzz!")
elif num % 3 != 0:
  print("Special Case! - Not divisible by both 3 and 5")
elif num % 5 != 0:
  print("Special Case! - Not divisible by both 3 and 5")