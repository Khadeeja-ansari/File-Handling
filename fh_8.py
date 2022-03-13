# Read contents of a1.txt and copy them into a3.txt

f1 = open("a1.txt","r")
f2 = open("a3.txt","w")
for i in f1:
    f2.write(i)
f1.close()
f2.close()