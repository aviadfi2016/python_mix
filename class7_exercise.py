##Exercise7_1b
def nine():
    return 9
##test
print(nine())


##Exercise7_2b

def multiply_word(given_word , num_of_multi):
    multiply_word = given_word * num_of_multi
    return multiply_word
##test
print(multiply_word("ban", 5))

##Exercise7_3b
def add_and_subtract(number1 , number2):
    num_add = number1 + number2
    num_sub = number1 - number2
    return  (num_add , num_sub)

print(add_and_subtract(5, 2))
add, subtract = add_and_subtract(100, 137)
print(add, subtract)


##Exercise7_3a

def isPalindrome(given_str):
     if given_str == given_str[::-1]:
      return True
     else: 
        return False
##test
print(isPalindrome("rats live on no evil star"))






##Ex 7_6a

def multiply( x , y ):
    if x < y:
        return multiply(y, x)
    elif y != 0:
        return (x + multiply(x, y - 1))
    else:
        return 0 
# test
x = 2
y = 2
print( multiply(x, y))


def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(multiply(base ,power(base,exp-1)))
# test
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))



