# Define a set with a mix of different data types
sett = {1, True, "Akshaya Baalaji", False, 'a', 23.24, -234}

# Print the set, note that the order is unpredictable due to the nature of sets
print(sett)

# Convert the set to a list
listt = list(sett)

# Print the list
print("List is ", listt)

# Access the 4th element of the list (Python uses 0-based indexing)
print("The 4th element is ", listt[3])

# Slice the list from index 1 to 5 (end index is exclusive)
print("The elements from 1 to 6 are ", listt[1:6])
    """
    {False, 1, 'a', 'Akshaya Baalaji', -234, 23.24}
List is  [False, 1, 'a', 'Akshaya Baalaji', -234, 23.24]
The 4th element is  Akshaya Baalaji
The elements from 1 to 6 are  [1, 'a', 'Akshaya Baalaji', -234, 23.24]
    """