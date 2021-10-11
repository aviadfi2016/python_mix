##Exercise 11_1
def sum_of_list(given_list):
    return sum(given_list)
##test
list= [1, 2, 3, 4]
print(sum_of_list(list))


##Exercise 11_2
def multiply(given_list):
    my_new_list = [i * 2 for i in given_list]
    print(my_new_list)

##test
list= [1, 2, 3, 4]
multiply(list)


##Exercise 11_3
def nums_to_str(given_list):
    
    print (', '.join(map(str, given_list)))



##test
list= [1, 2, 3, 4]
nums_to_str(list)



