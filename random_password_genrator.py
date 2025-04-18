# -*- coding: utf-8 -*-
"""Random_Password_Genrator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Vp0P_jI2QELBHrxwTi2bDw51wkCqBUmB
"""

code = """
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = "!@#$%^&*()_+"
numbers = "1234567890"

all_cahrs = lower + upper + special + numbers

length = int(input("Enter password length: "))

if length > len(all_cahrs):
    password = ''.join(random.choices(all_cahrs, k=length))
else:
    password = ''.join(random.sample(all_cahrs, length))

print("Generated password:", password)
"""

with open("/content/Random_password_genrator/password_generator.py", "w") as f:
    f.write(code)