# number = int(input("Enter a number: "))

# for i in range(2, number):
#     if number % i == 0:
#         print("No prime")
#         break
#     else:
#         print("Prime")


# end = int(input("End number: "))

# primes = []
# for num in range(2, end + 1):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(num)

# print("Prime numbers:", primes)



# Start with the first two Fibonacci numbers
fib1 = 0
fib2 = 1
count = 25  # Number of Fibonacci numbers to generate

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate and print Fibonacci numbers with prime check
print("First 25 Fibonacci numbers with prime check:")
for _ in range(count):
    print(fib1, "- Prime" if is_prime(fib1) else "- Not Prime")
    next_fib = fib1 + fib2  # Compute next Fibonacci number
    fib1 = fib2  # Update first number
    fib2 = next_fib  # Update second number

