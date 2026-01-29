# Prime Number Finder

# Input and validation using while loop
while True:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    
    if start > 1 and end > start:
        break
    else:
        print("Invalid input! Start must be > 1 and End must be greater than Start.")

print("Prime numbers between", start, "and", end, "are:")

# Loop to find prime numbers
for num in range(start, end + 1):
    is_prime = True
    
    # Check prime using for loop
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num)
