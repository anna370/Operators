def print_results(first_number, second_number):
  print(first_number + second_number)
  print(int(first_number - second_number))
  print(first_number * second_number)
  
  if second_number == 0:
    print("Cannot divide by zero.")
  else:
    print(first_number / second_number)

first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))

print_results(first_number, second_number)
