incorrect_word = input("Enter the incorrect word: ")
file = open("demo.txt","r")
texts = file.read()

correct_word = input("Enter the correct replacement of the incorrect word: ")
update_text = texts.replace(incorrect_word,correct_word)
file1 = open("demo.txt", 'w')
file1.write(update_text)
print("All occurances changed.")
file.close()