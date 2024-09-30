file = open("demo_file.txt","r")
list = file.read().split(".")
print(list)
file = open("demo_file.txt","w")
for i in list: