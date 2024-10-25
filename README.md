
# DATA STRUCTURES IN PYTHON

# Topic :List
# Exercise
# Q1. Create a list of 5 random numbers and print the list.

import random
l1 = [random.randint(1,50) for i in range (5)]
print(l1,type(l1))


![DS 1](https://github.com/user-attachments/assets/df2e7771-6013-4466-9f44-184331deec05)


# Q2. Insert 3 new values to the list and print the updated list.

new_values = [random.randint(1,50)for i in range(3)]
l1.extend(new_values)
print ("Updated list",l1)


![DS 2](https://github.com/user-attachments/assets/fd1e06d6-15a9-4a5b-9245-6baa39031b75)


# Q3. Try to use a for loop to print each element in the list.

for element in l1:
    print(element, end=" ")


![DS 3](https://github.com/user-attachments/assets/f2b8d5fc-f04d-4403-803b-2b3f237dca19)


# Topic: Dictionary
# Exercise
# Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.

person_info = {'name': 'John','age': 25,'address': 'New York'}
print(person_info)


![DS 4](https://github.com/user-attachments/assets/2d526106-73d6-42c5-9973-a439e033eb4b)


# Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.

person_info['phone'] = '1234567890'
print(person_info)


![DS 5](https://github.com/user-attachments/assets/1e0fd069-c7e8-4d66-9038-4b822327109c)


# Topic: Set
# Exercise
# Q1.Create a set with values 1, 2, 3, 4, and 5.

s1 = {1,2,3,4,5}
print(s1,type(s1))


![DS 6](https://github.com/user-attachments/assets/095ff2db-031b-4e96-8477-837a183f2de8)


# # Q2. Add the value 6 to the set created in Q1.

s1.add(6)
print(s1)


![DS 7](https://github.com/user-attachments/assets/b91c9022-dce2-4320-b27c-588dcfbc6ca4)


# # Q3. Remove the value 3 from the set created in Q1.

s1.remove(3)
print(s1)


![DS 8](https://github.com/user-attachments/assets/ea8af328-b0fb-4bc3-ba0b-fe48168259bd)


# Topic:Tuple
# Exercise
# Q1. Create a tuple with values 1, 2, 3, and 4

t1 = 1,2,3,4
print(t1,type(t1))


![DS 9](https://github.com/user-attachments/assets/f371a027-0361-4950-917c-d5a51650269c)


# Q2. Print the length of the tuple created in Q1.

print(len(t1))


![DS 10](https://github.com/user-attachments/assets/14c3ea46-5af5-4975-a60f-4919e22a3f0a)
