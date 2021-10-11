##ex 5_1

string_output = "hello world" 
print(string_output)

string_output = string_output.replace(string_output[5], 'f')
print(string_output)

str2 = string_output[4:]
str1 = string_output[:4] 
str3= str1 + ' ' + str2
print(str3)
str_swap1 = str3[7:]
str_swap2 = str3[0:5]
str_swap3 = str3[5:7]

print(str_swap1)
print(str_swap2)
print(str_swap3)
new_string = str_swap1+' '+ str_swap3 + ' ' + str_swap2
print(new_string)

##ex 5_2

str_name= 'my name is aviad'

for i in range(len(str_name)):
    print(i, str_name[i])

##ex 5_3b 
given_string = input("please enter a string: ")

print(given_string[::-1])

## ek 5_4b

word = "Mississippi"
counter = 0
letter = "i"

for  i in word:
    if i == letter:
      counter += 1
print(counter)
    

## ex 5_5b

word = "Mississippi"
substring = "ssi"
count = word.count(substring)
print("Count: " , count)


## ex 5_3

given_str = input( "Please write a message: ")

print(given_str)

str_len = len(given_str)
i = str_len
while i != 0:
   
    print (given_str[0:i-1])
    i = i-1


