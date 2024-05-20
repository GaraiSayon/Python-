fact = 1
n = int(input("Enter a number greater than 0: "))

for i in range(1, n+1):
    fact *= i

print(f"Factorial of {n} is {fact}")
