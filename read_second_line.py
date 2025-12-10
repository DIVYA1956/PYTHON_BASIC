
f = open("practice1.txt","w")
f.write("This is the first line.\n")
f.write("Python is amazing!\n")
f.write("File handling is easy.\n")
f.close()  # close after writing



# Program to read the second line and print first 5 characters of it

f = open("practice1.txt", "r")  # open file in read mode
lines = f.readlines()         # read all lines

print("2nd line is:", lines[1])      # print full second line
print("First 5 characters:", lines[1][:5])  # print first 5 characters

f.close()