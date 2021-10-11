##Exercise9_1b
# Open file        
FILE_PATH = r'C:\Users\aviad\Desktop\haiku.txt'
fileHandler = open (FILE_PATH, "r")
count = 1
while True:
    # Get next line from file
    line = fileHandler.readline()
    
    if line=="" :
        break;
    else:
        print(count, ":", line)
        count+=1
# Close Close    
fileHandler.close()   

##Exercise 9_2b
my_info = {"name": "Yuval", "age": 12, "height": 1.82, "dances ballet": False}

with open("myfile.txt", 'w') as f: 
    for key, value in my_info.items(): 
        f.write('%s:%s\n' % (key, value))

##Exercise9_2

filenames = ['file1.txt', 'file2.txt']
  
with open('file3.txt', 'w') as outfile:
  
    # Iterate through list
    for names in filenames:
  
        # Open each file in read mode
        with open(names) as infile:
  
            ## read the data from file1 and
            ## file2 and write it in file3
            outfile.write(infile.read())
  
        outfile.write("\n")


##Exercise9_3
file = open(FILE_PATH, "rt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))

