#write a program to read a file line by line and print it
L = ["Charu\n","Pradeep\n","Sharma\n"]
file1 = open('myfile.txt', 'w')
file1.writelines()
file1.close()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()

count = 0

for line in lines:
    count+=1

print("line".format(count,line.strip()))