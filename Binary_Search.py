def binary_search(arr, x, low, high):
    result = -1
    while low <= high:
        mid = low + (high - low) // 2  # Calculate the middle index

        if arr[mid] == x:
            result = mid  # Found the element, return the index
            break  # Exit the loop once we find the element
        elif arr[mid] > x:
            high = mid - 1  # Search in the left half
        else:
            low = mid + 1  # Search in the right half
    return result  # Return the result (index or -1 if not found)

# Accept the input as a string and convert it to a list of integers
list1 = list(map(int, input("Enter a list : ").split(',')))

# Accept the number to search for and convert it to an integer
a = int(input('Enter a number to search for: '))

# Call the binary search function
b = binary_search(list1, a, 0, len(list1) - 1)

# Print the result
print(b)
