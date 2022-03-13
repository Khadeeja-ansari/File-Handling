# Enter any file name to remove 

import os
n = input("Enter a file name with extension : ")
if(os.path.exists(n)):
    os.remove(n)
else:
    print("File with this name doesn't exists.")