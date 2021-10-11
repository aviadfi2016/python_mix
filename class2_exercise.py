##ex 2_1 
name= input("please enter your name: ")
print( "Hello "+name)


##ex 2_2
work_hours= int(input("please enter your work hours: "))

work_wage= int(input("please enter your wage: "))
salary=str(work_wage*work_hours)
print( "Your salary is: "+salary )

## ex 2_3
user_input= int(input("please enter the temperature in Fahrenheit: " ))

convert_temp= str((user_input-32)*(5/9))

print("The temperature in Celsius is: " +convert_temp)

##ex 2_4

cow_legs= int(input("How many cows do you have?:"))
sheep_legs= int(input("How many sheep do you have?:") )
chicken_legs = int(input("How many chickens do you have?:"))
spider_legs = int(input("How many spiders do you have?: "))

sum_legs= str(cow_legs*4+sheep_legs*4+chicken_legs*2+spider_legs*8)
print("You have " + sum_legs + " legs on your farm!")


##ex 2_5

a_num= float(input("Please enter the a number "))
b_num= float(input("Please enter the b number "))
c_num= float(input("Please enter the c number "))


first_ans= (-b_num+((b_num**2-4*a_num*c_num)**(0.5)))/(2*a_num)


seconde_ans=(-b_num-((b_num**2-4*a_num*c_num)**(0.5)))/(2*a_num)

print(first_ans)
print(seconde_ans)