# Input the size of the array
array_size = int(input("Input the size of the array: "))


# Define a function to process the array
def array_function(array_size):
    # Initialize an empty array
    array = []

    # Check if the input array_size is valid (non-zero)
    if array_size > 0:
        # Ask how many elements to add based on array_size
        for i in range(array_size):
            element = int(input(f"Enter element {i + 1}: "))
            cubed_element = element ** 3  # Cube the element
            array.append(cubed_element)  # Add cubed element to array
    else:
        print("Invalid size. The size of the array should be greater than 0.")

    return array


# Call the function and store the result
result = array_function(array_size)

# Print the resulting array
print("The cubed array is:", result)
