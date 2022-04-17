text = "Are you sure about that\nProbably you need more coffee\nSee You Later\n"

with open('test.txt', 'a') as file:
    file.write(text)

# w --> overwrite the file
# a --> append new lines
