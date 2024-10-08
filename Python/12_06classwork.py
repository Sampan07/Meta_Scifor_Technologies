# -*- coding: utf-8 -*-
"""12/06Classwork

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L9gAU0LxsHAYuB6G9vpLPrytXjYwV4Yj
"""

name = str(input("Enter pet name: " ))
name2 = name[::-1]
if name==name2:
  print("True")
else:
  print("False")

word = input("Enter word: ")
reverse=word[::-1]
odd_chars=''.join(reverse[i] for i in range(1,len(reverse),2))
even_chars=''.join(reverse[i] for i in range(0,len(reverse),2))

secret_word = odd_chars + even_chars
print(secret_word)

length = len(secret_word)
mid = (length+1)//2
odd_chars=secret_word[:mid]
even_chars=secret_word[mid:]
original_word_reversed=''
for i in range(mid):
  if i<len(even_chars):
    original_word_reversed+=even_chars[i]
  if i<len(odd_chars):
    original_word_reversed+=odd_chars[i]

phone_number = input("Enter the phone number: ")
starting_dig = ['9', '8', '7']
if len(phone_number) == 10:
    if phone_number.isnumeric():
        if phone_number[0] in starting_dig:
            print(f"Phone number {phone_number} is valid")
        else:
            print(f"Phone number {phone_number} is Invalid: (First digit not 9, 8, or 7)")
    else:
        print(f"Phone number {phone_number} is Invalid: (Contains non-numeric characters)")
else:
    print(f"Phone number {phone_number} is Invalid: (Length not 10 digits)")