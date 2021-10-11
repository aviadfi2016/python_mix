##Python Exercise3_1##
given_name = input("please enter your name: ")
if given_name == "aviad":
    print("Hello ",given_name, " Have a great day!")
else:
    print("Greetings, stranger.")




##Python Exercise3_2##

score = float(input("please enter your score: "))
if score > 1.0:
    print("Error –Bad score –should be between 0.0 and 1.0.")
if score < 0.9 and score >= 0.8:
      print("B")
if score < 0.8 and score >= 0.7:
      print("C")
if score < 0.7 and score >= 0.6:
      print("D")        
if score < 0.6 :
      print("F")

##Python Exercise3_3##
hours = float(input("Enter Hours: "))
if hours < 40:
    print("not enough hours")
elif hours >= 50:   
    wage = float(input("Enter Wage: "))

    print(hours*1.5*wage)


elif hours < 50 and hours >= 40:   
    wage = float(input("Enter Wage: "))
    print(hours*wage)





##Python Exercise3_4##
suit_cost = float(input("How much the suit costs "))
fifty_bill = float(input("How many 50$ bills?: "))
ten_bill = float(input("How many 10$ bills?: "))
five_bill = float(input("How many 5$ bills?: "))

num_of_fifty=int(suit_cost/50)

suit_cost= suit_cost%50

num_of_ten=int(suit_cost/10)
if num_of_ten == 0 :
        num_of_ten = 1 
        change = 10-(suit_cost%50) 
        num_of_five = 0
        print(num_of_fifty, num_of_ten, num_of_five)






##Python Exercise 3_5##

circle1_x = int(input("enter x circle 1:"))
circle1_y = int(input("enter y circle 1:"))
circle1_radius = int(input("enter radius circle 1:"))

circle2_x = int(input("enter x circle 2: "))
circle2_y = int(input("enter y circle 2: "))
circle2_radius = int(input("enter radius circle 2: "))
##formula for checking if 2 circles overlapping ##
if ((circle2_x-circle1_x)*0.5+(circle2_y-circle1_y)*0.5) < circle1_radius+circle2_radius:
   print("YES, the circles are  overlapping.")

else:
   print("No, the circles are not overlapping.")