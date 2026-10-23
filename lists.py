users =['Alice', 'Bob', 'Charlie', 'David', 'Eve']
data =['Dave', '42', True]
emptylist = []
print("Dave" in emptylist)  # Check if 'Dave' is in the users list
print(users[0])  # Access the first element of the users list
print(users[-2])  # Access the last element of the users list

print(users.index('Charlie'))  # Find the index of 'Charlie' in the users list
print(users[0:2])  # Slice the users list to get the first two element
print(users[-3:-1])  # Slice the users list to get the last two elements

print(len(data))
users.append('Frank')  # Add 'Frank' to the end of the users list
print(users)

users +=['Jason', 'Grace']  # Add multiple elements to the users list
print(users)

users.extend(['Hannah', 'Ian'])  # Extend the users list with another list
print(users)
# users.extend(data)
# print(users)
users.insert(0, 'Zara')  # Insert 'Zara' at the beginning of the users list 
print(users)
users[2:2] = ['Sam', 'Tom']  # Replace the element at index 2 with 'Sam' 
print(users)
users.remove('Bob')  # Remove 'Bob' from the users list
print(users)
print(users.pop())  # Remove the last element from the users list
print(users)
data.clear()  # Clear all elements from the data list
print(data)

users[1:2] = ["Dave"]  # Remove the element at index 1 from the users list
users.sort()  # Sort the users list in ascending order
print(users)    

users.sort(key=str.lower)  # Sort the users list in ascending order
print(users)  
nums = [5, 2, 9, 1, 7]
nums.reverse()  # Reverse the order of elements in the nums list
print(nums)

# nums.sort(reverse=True)  # Sort the nums list in descending order
# print(nums)
numscopy = nums.copy()  # Create a copy of the nums list
print(numscopy)

numscopy = nums.copy()  # Create a copy of the nums list
mynums = list(nums)
mycopy = nums[:]


print(numscopy)
print(mynums)
mycopy.sort()  # Sort the mycopy list in ascending order
print(mycopy)
print(nums)

mytuple = tuple(('Toluwani', 'David', 'Eve', 'Frank'))

anothertuple=(1, 2, 3, 4, 5 , 3, 3)
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist=list(mytuple)  # Convert the mytuple to a list
newlist.append('Grace')  # Add 'Grace' to the newlist
print(newlist)


(one,two, *hey)= anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(3))


