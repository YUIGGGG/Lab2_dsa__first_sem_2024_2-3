number = int(input("Enter any number: "))

for i in range(1, number + 1):
    for j in range(1, number + 1):
        # Print '*' on the borders (first row, last row, first column, or last column)
        if i == 1 or i == number or j == 1 or j == number:
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space inside the hollow square
    print()  # Move to the next line after each row