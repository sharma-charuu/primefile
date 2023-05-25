#write a program to display the number of lines in the files and size of a file in bytes
import os

print("enter the name of file:")
filename = input()
sizeoffile = os.path.getsize(filename)
print("\n size of given file(in bytes) is:")
print(sizeoffile)