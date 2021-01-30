infile = open("inputfile.txt", 'r')                 # Reading input text file
count = {}                                          # Creating a dictionary
line = infile.readline().replace('\n','')           # Reading first line

while line != "":                                   # If the line is not empty loop will run
    for i in line.split(" "):                       # Spilt each line with " "
        temp = (count.get(i))
        if temp is None:                            # If the word is not in dictionary it will add
            count[i] = 1
        else:
            count[i] = count[i] + 1                 # If the word is present in dictionary ut will update the count
    line = infile.readline().replace('\n','')       # Reading next line

print("Word count = ")
outfile = open("outfile.txt", 'w')
for i in count:
    outfile.write(i + ": " + str(count[i])+"\n")    # Writing output in output file
    print(i, " ", count[i])