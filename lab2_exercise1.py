# Getting input from the user
power = int(input("What is the base number? "))  # Convert input to integer
number = int(input("What is the exponent? "))    # Convert input to integer

# Define the recursive function to calculate the exponential
def exponential(number, power):
    # Base case: Any number raised to the power of 0 is 1
    if power == 0:
        return 1
    # Recursive case: Multiply base by the result of base raised to (exponent - 1)
    else:
        return number * exponential(number, power - 1)

# Call the function and print the result
print(f"{power} to the power of {number} is: {exponential(power, number)}")
