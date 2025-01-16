#WAP to count how many word are present in a file

with open('file.txt', 'w') as f:
    f.write("Hello, this is a file with some words in it. We will count how many words are in this file.")

with open('file.txt', 'r') as f:
    content = f.read()
    print("File content:")
    print(content)
    numOFwORDS = content.split()
    print(len(numOFwORDS))