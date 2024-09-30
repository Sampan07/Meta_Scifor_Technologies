file = open("demo_file.txt","r")
lines = file.readlines()
print(lines)

file = open("demo_file2.txt","w")
for i, line in enumerate(lines, start=1):
    file.write(f"{i}: {line}")
file.close()