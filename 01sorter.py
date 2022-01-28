in1 = open("mapout.txt","r")  # open file, read-only
out = open("sorter.txt", "w") # open file, write
lines = in1.readlines()
lines.sort()

for line in lines:
 out.write(line)

in1.close()
out.close()