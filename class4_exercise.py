##Python Exercise4_1##
##sum & avg list
number_list = [9, 41, 12, 3, 74, 15]
sum = 0
for num in number_list:
    sum = sum + num
average = sum / len(number_list)
print("Sum of first ", number_list, "numbers is: ", sum)
print("Average of ", number_list, "numbers is: ", average)


##Python Exercise 4_2##
##sum given numbers
given_str= "done"

sum = 0
user_input = None  
   
while user_input != given_str:
    user_input =  input('Enter your input:')
    if user_input == given_str:
        break
    user_input_conver= int(user_input)
    sum += user_input_conver

print( sum )


##Python Exercise 4_3##
##the Prime Number
given_num = int(input("Enter a number: "))  
 
if given_num > 1:  
   for i in range(2,given_num):  
       if (given_num % i) == 0:  
           print(given_num,"is not a prime number")  
            
           break  
   else:  
       print(given_num,"is a prime number")  
         
else:  
   print(given_num,"is not a prime number")

##Python Exercise 4_4##
##the Perfect Number
for number in range(1, 1000 ):
    sum = 0
    for num in range(1, number - 1):
        if(number % num == 0):
            sum = sum + num
    if(sum == number):
        print( number )


