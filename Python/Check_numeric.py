file = open("demo.txt","r")
textlist = file.readlines()
lines_with_numbers = []
for line_number, line in enumerate(textlist, start=1):
            for char in line:
                if char.isdigit():
                    lines_with_numbers.append(line_number)
                    break
print("Lines having Numerical Values: ")
for i in lines_with_numbers:
    print(i)

file.close()

