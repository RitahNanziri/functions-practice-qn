
# Write a python function to find the maximum of 3 numbers
#a=70 b=80 c=65
def maximum_value(a,b,c):
    if a >b and a>c:  
        print(f"{a} is greater than {b} and {c}")
    elif b>a and b>c:
        print(f"{b} is greater than {a} and {c}")
    else: 
        print (f"{c} is greater than{a} and {b}" ) 
maximum_value(70,80,65)   
maximum_value(99,79,69) 

# Write a python function to sum all numbers in a list
#sample list ( 8, 2, 3, 0,7 )
# a=8 b=2 c=3 d=0 e= 7

def sum_numbers(numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum

numbers = [8, 2, 3, 0, 7]
total_sum = sum_numbers(numbers)
print(total_sum) 
    
 

# passing alist as an argument
# returning values
# passing statement


# Write a python program to reverse a string 1234 abcd



def reverse_string(string):
  return string[::-1]

input_string = "1234 abcd"
print(reverse_string(input_string))





#Write a python function to multiply all the numbers in a list [8,2,3,-1,7] 

def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
numbers = [8, 2, 3, -1, 7]
print(multiply_list(numbers))

# write a python program to print the even numbers in a given list [1,2,3,4,5,6,7,8,9]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number % 2 == 0:
        print(number)

    
    
       
    