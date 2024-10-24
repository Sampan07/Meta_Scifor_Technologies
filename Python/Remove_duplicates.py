file = open("demo_file.txt","r")
words = file.read().split()
distinct_words = []
for i in range(len(words)):
    if i == 0 or words[i] != words[i - 1]:
        distinct_words.append(words[i])
after_removing_duplicates = ' '.join(distinct_words)
file = open("demo_file.txt","w")
file.write(after_removing_duplicates)