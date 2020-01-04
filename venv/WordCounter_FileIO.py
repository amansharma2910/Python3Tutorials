## In order to use and file IO functions, you need to import the os module.
import os

## with ensures that the file is closed after the operations are done on it.
with open("io.txt", mode="w", encoding="utf-8") as txt_file:
    txt_file.write("This is a sample text file.\nWe will see what operations can be performed.\nFile IO is an important topic in programming.")

## read() reads the whole file at once. On the other hand, readline() reads the file line by line.

## With the help of the code below, we will be reading the file line by line, counting the number of words in each line as well as the average word count per line.
with open("io.txt", encoding="utf-8") as txt_file:
    line_num = 1
    while True:
        line = txt_file.readline()
        if not line:
            break
        list1 = line.strip().split()
        word_count = 0
        words = 0
        for i in list1:
            word_count += 1
            words += len(i)
        print("Line {}".format(line_num))
        print("Number of words: {}".format(word_count))
        print("Avg word length: {:.2f}".format(words/word_count))
        line_num += 1
