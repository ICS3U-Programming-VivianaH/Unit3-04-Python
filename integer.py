#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: march 26 2025
# This program tells if the input
# is a positive or negative number
# Ask for thhe number
user_num = int(input("Enter a number: "))

# Check if it's positive, negative, or zero
if user_num > 0:
    print(user_num, "is a positive number")
elif user_num < 0:
    print(user_num, "is a negative number")
else:
    print(user_num, "is just zero!")
