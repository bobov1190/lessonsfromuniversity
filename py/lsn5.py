# a = int(input('a : '))
# b = int(input('b : '))

# total = 0
# i = 0

# current = a

# while current <= b:
#     total += current  
#     i += 1        
#     current += 1       

# if i > 0:
#     average = total / i
#     print(f"The average of numbers between {a} and {b} is {average}")
# else:
#     print('Error')


# num = int(input("Enter a number: "))
# result = 1

# for i in range(1, num + 1):  # Loop from 1 to num (inclusive)
#     result *= i

# print(f"The factorial of {num} is {result}.")

number = int(input("Enter a number: "))


for i in range(2, number):
    if number % i == 0:
        print("No prime")
        break
else:
    print("Prime")