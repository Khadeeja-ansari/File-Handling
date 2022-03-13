# read() -> It is used to read the file
# Read contents of a1.txt and display them on screen

f = open("a1.txt","r")
for i in f:
    print(i)
f.close()