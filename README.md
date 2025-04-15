# 🔐 Random Password Generator

This is a simple Python script to generate secure, random passwords of any desired length. It includes lowercase letters, uppercase letters, numbers, and special characters.

## 🚀 Features

- Generates a random password of custom length
- Ensures a strong mix of characters:
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters
- Prevents repetition (when possible)
- Easy to use and customize

## 🧠 How It Works

The script uses Python’s built-in `random` module to generate a password by selecting characters from a defined character set.

## 📌 Requirements

- Python 3.x
- No external libraries required

## 📝 Usage

In your Python environment or Google Colab:

```python
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = "!@#$%^&*()_+"
numbers = "1234567890"
all_chars = lower + upper + special + numbers

length = int(input("Enter the desired password length: "))

# Ensures unique characters if length <= total character set
if length > len(all_chars):
    password = ''.join(random.choices(all_chars, k=length))
else:
    password = ''.join(random.sample(all_chars, length))

print("Generated Password:", password)



