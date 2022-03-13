# append -> Changes can be done using this function
# Input names and store it in a file called Stud.txt using append 

f = open("Stud.txt","a")
for i in range (0,3):
    i=input("Name : ")
    f.write("Name : ")
    f.write(i)
    f.write("\n")
f.close()