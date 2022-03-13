# Input 6 names and store it in a file called Stud.txt

f = open("Stud.txt","w")
for i in range (0,6):
    i = input("Name : ")
    f.write("Name : ")
    f.write(i)
    f.write("\n")
f.close()