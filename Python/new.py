# use for loop, write a program to read a file and
# print the number of upper letters,words ,lower letters,digits and the symbols and
# how many sentences are getting started with a A letter


file = open("doc.txt","r")
text = file.read()
file.close()
upper = 0
lower = 0
digits = 0
symbol = 0
start_with_A = 0
formatted_text = text.split()
for word in formatted_text:
    if word.isupper():
        upper+=1
    elif word.islower():
        lower+=1
    elif word.isdigit():
        digits+=1
    elif word.startswith("A"):
        start_with_A+=1
    else:
        symbol+=1
print("Upper Letter: ",upper)
print("Lower Letter: ",lower)
print("Digits: ",digits)
print("Symbol: ",symbol)
print("Words starting with A: ",start_with_A)