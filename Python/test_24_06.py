# -*- coding: utf-8 -*-
"""Test 24/06

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BOU4RUt_Zs-_ryp43Ni-ynWibjcuzGpI

In a classroom, there are desks arranged in a row and column fashion. The math teacher, Mr. James, asked one of the kid whose name was Robert to count the total number of desks present in the class. Robert was just wondering if there is software that could take the number of rows and number of columns and show how many desks there are that would make his job easier. So write a python program to help Robert to count the number of desks present in the class.
"""

rows = int(input("Enter no of rows: "))
columns = int(input("Enter no of columns: "))
desks=0
for i in range(rows):
    for j in range(columns):
        desks+=1
print("Desks Count = ",desks)

"""Mr James, A businessman in canada was throwing a small party in a banquet hall and wanted to track the number of people attended the party so he kept a people tracker device in the entrance where every person enters is supposed to enter his or her authorization code to enter the hall, certain codes were assigned they are as follows :
If Banquet Hall Team Members like Manager, waiter, and Mr. James himself then their authorization code will be : 0
If Guests Their Authorization Code Will be : 1
If the Authorization Code Entered is 1 then increment the number_of_guests Variable by 1, Wish the Guest like
"Door Opened"
"Welcome to the Party, We Hope you have fun."
else If the Authorization Code Entered is 0 then print as follows
"Access Granted"
"Door Opened"
else tell the person that his entered number is invalid

"""

guests_count = 0
team_members_count = 0
running = True
print("Code 0 for Team Members")
print("Code 1 for Guests")
print("Code 2 to exit")
while running:
  code = int(input("Enter code: "))
  if code == 2:
      running = False
  elif code == 0:
      team_members_count += 1
      print("Access Granted")
      print("Door Opened")
  elif code == 1:
      guests_count += 1
      print("Door Opened")
      print("Welcome to the Party, We Hope you have fun.")
  else:
      print("Invalid Code")
print(f"Number of Team Members = {team_members_count}")
print(f"Number of Guests = {guests_count}")

"""Mathew, a 13 year old kid, is good at math but whenever it comes to the even and odd numbers he always faces difficulty to find the even or odd number greater than 10. So write a python program to help Mathew to print odd and even numbers in a certain range using a for loop."""

n= int(input("Enter the range: "))
print("Even numbers in the range: ")
for i in range (1,n+1):
    if i%2==0:
        print(i,end=',')
print("\nOdd numbers in the range: ")
for i in range (1,n+1):
    if i%2!=0:
        print(i,end=',')

"""An online essay writing competition was held in a school. The students were required to write at least 250 words. According to the rule, only that essay should be checked which contains at least 250 words. Teachers were just guessing the number of words in the essay but that was not an accurate way to count the number of words. So write a program that can count the number of words in an essay ( Hint: Take input and count the number of words using for loop | Note: to count the number of words you can just count the number of blank spaces given in the input. )

"""

essay = input("Enter the essay: ")
words= 1
for i in essay:
    if i==' ':
        words+=1
print("Number of words in the essay: ",words)

"""Create  a program that find the number is prime number or not.

"""

num = int(input("Enter the number: "))
if num<=1:
    print("Number is not prime")
else:
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print("Not Prime")
                break
        else:
            print("Prime")