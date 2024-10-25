
# DATA STRUCTURES IN PYTHON

# Topic :List
# Exercise
# Q1. Create a list of 5 random numbers and print the list.

import random
l1 = [random.randint(1,50) for i in range (5)]
print(l1,type(l1))

# Q2. Insert 3 new values to the list and print the updated list.

new_values = [random.randint(1,50)for i in range(3)]
l1.extend(new_values)
print ("Updated list",l1)

# Q3. Try to use a for loop to print each element in the list.

for element in l1:
    print(element, end=" ")

# Topic: Dictionary
# Exercise
# Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.

person_info = {'name': 'John','age': 25,'address': 'New York'}
print(person_info)

# Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.

person_info['phone'] = '1234567890'
print(person_info)

# Topic: Set
# Exercise
# Q1.Create a set with values 1, 2, 3, 4, and 5.

s1 = {1,2,3,4,5}
print(s1,type(s1))

# # Q2. Add the value 6 to the set created in Q1.

s1.add(6)
print(s1)

# # Q3. Remove the value 3 from the set created in Q1.

s1.remove(3)
print(s1)

# Topic:Tuple
# Exercise
# Q1. Create a tuple with values 1, 2, 3, and 4

t1 = 1,2,3,4
print(t1,type(t1))

# Q2. Print the length of the tuple created in Q1.

print(len(t1))