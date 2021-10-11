##Exercise6_A_1
print("hello please enter a character: ")
char_input = str(input())
if len(char_input)-1 > 0 :
    print("wrong input!!!")
if char_input.islower():
    print(char_input.upper())
if char_input.isupper():
    print (char_input*5)



##Exercise6_A_2
print("hello, give me a string: ")
user_str = str(input())
print("Give me a character: ")
user_char = str(input())
output_index = user_str.find(user_char)
if output_index == -1 :
   print("Character was not found...") 
else:
   print(output_index)

##Exercise6_A_3
##not full
print("Give me a word:")

user_string = str(input())

if len(user_string)-1 <= 0 :
    print("Error: Give me a full word and ONLY a word!")

else :
     print(user_string.title())

##Exercise6_B_1b
strings = ["Hello", "Goodbye", "Please", "Thank you"]

for i in range(len(strings)):
   print(f"Index: {i}, Item: {strings[i]}")

##Exercise6_B_2b

list_of_numbers = []
  
print("please enter 5 numbers: ")
for i in range(0, 5):
   
    user_number_input = int(input())
    list_of_numbers.append(user_number_input)
      
print(list_of_numbers)

list_of_numbers[0] = 1  
 
print(list_of_numbers[0:3])


##Python Exercise6_B_1a
list_of_numbers = []
favorite_number = 10
print("please enter 5 numbers: ")
for i in range(0, 5):
   
    user_number_input = int(input())
    list_of_numbers.append(user_number_input)
      
print(list_of_numbers[0:3], list_of_numbers[4])

if (favorite_number in list_of_numbers):
    print("My favorite number,"+ str(favorite_number) + ", was chosen")
else :
    print("My favorite number,"+ str(favorite_number) + ", was sadly not chosen")



list_of_numbers[0] = 1  
list_of_numbers.extend([30])

print(list_of_numbers)

##Exercise6_B_2a
number_list = []
n = int(input("How many numbers in the list?: "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    number_list.append(item)
print("User list is ", number_list)
rev_list = str(list(reversed(number_list) ))
print("Reversed List: "+ rev_list )
sum_list = sum(number_list)
print("Sum: " + str(sum_list))
avg_list = str(sum_list / n)
print("Average: " + avg_list)




