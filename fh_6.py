# read(n) -> 'n' is number of characters
# Read first 7 characters from a1.txt

f = open("a1.txt","r")
print(f.read(7))
f.close()