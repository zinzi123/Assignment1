# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 11:02:52 2023

@author: User
"""
#Write a Python program which accepts the radius of a circle from the user
#nd compute the area.
import math
# Input radius from the user
r = float(input("Enter the radius: "))

# Calculate the area of the circle
a = math.pi * (r ** 2)

# Display the result
print("Area of circle",a)

#Write a Python Program to accept the details of a student like name, roll
#number and mark and display it.
name = input("Enter the name: ")
roll_number = input("Enter the roll number: ")
mark = input("Enter the mark: ")

# Display the student details
print("Name:",name)
print("Roll No:",roll_number)
print("Mark:",mark)

#list of numbers
list1 = [10, 20, 4, 45, 99]
 
# sorting the list
list1.sort()
 
# printing the last number
print("Largest number is:", list1[-1])


# Initialize the previous number
bef_no= 0

# Iterate through the range of numbers from 1 to 10
for cur_no in range(1, 11):
    # Calculate the sum of the current and previous numbers
    cur_sum = cur_no + bef_no
    
    # Print the result
    print("Cur no. is ", cur_no )
    print("bef no is", bef_no )
    print("Sum is" ,cur_sum)
    
    # Update the previous number for the next iteration
    bef_no = cur_sum
    
# Define a list of numbers
n1 = [10, 25, 30, 42, 50, 63, 75, 90]

# no. divisble by 5
for number in n1:
    # Check if the number is divisible by 5
    if number % 5 == 0:
        # If divisible by 5, print the number
        print(number)
        
        
import math
 
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
 
print(is_prime(11))  # True
print(is_prime(1))   # False


def rev_list(input_list):
    rev_list = []
    for item in input_list:
        rev_list.insert(0, item)
    return rev_list

# Input a list from the user
input_list = input("Enter a list of elements separated by spaces: ").split()

# Reverse the list using the function
rev_result = rev_list(input_list)

print("Reversed list:", rev_result)

n = 4  # we can change the value to adjust the number of rows in the pattern

for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()
    
# Input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the maximum
if num1 >= num2 and num1 >= num3:
    maximum = num1
elif num2 >= num1 and num2 >= num3:
    maximum = num2
else:
    maximum = num3

# Print the maximum
print("The maximum of the three numbers is:", maximum)




n = 5  # Change this value to adjust the number of rows in the pattern

# Print the top half of the pattern
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()

# Print the bottom half of the pattern
for i in range(n - 1, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
Copy and paste this code into a Python environment, and when you run it with n = 5, it will produce the following output:

markdown
Copy code
*
**
***
****
*****
****
***
**
*
You can adjust the value of n to control the number of rows in the pattern.








