def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1  

# Accept the input as a string and convert it to a list of integers
list1 = list(map(int,input("enter a list :").split(',')))

# Accept the number to search for and convert it to an integer
a = int(input('Enter a number to search for: '))

# Call the linear search function
b = linear_search(list1, a)

# Print the result
print(b)
