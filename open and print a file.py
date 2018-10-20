# open a file and print every line
f = open ("F:/2830n_1125_s2/setenv.sh")
line = f.readline()
while line:
    print line,
    line = f.readline()
f.close()
count=0
for line in open("F:/2830n_1125_s2/setenv.sh") :
    print line,
    count+=1
print count