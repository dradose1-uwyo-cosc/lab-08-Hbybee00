# Hayden Bybee
# UWYO COSC 1010
# 11/04/24
# Lab 08
# Lab Section: 16
# Sources, people worked with, help given to:
# TA help :) 


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convert(numb):
    """This converts string to integers or floats"""
    negative = False
    if numb[0] == "-":
        negative = True
        numb = numb.replace("-","")

    if "." in numb:
        splnum = numb.split(".")
        if len(splnum) == 2 and splnum[0].isdigit() and splnum[1].isdigit():
            if negative:
                return -1*float(numb)
            else:
                return float(numb)

        else: 
            return False
    
    elif numb.isdigit():
        if negative:
            return -1*int(numb)
        else:
            return int(numb)

    else:
        return False


while True:
    intorflt = input("Put in a decimal or number to convert them to such!('exit to quit')")
    ans = convert(intorflt)
    if ans == False:
        print("Invalid input :(")
        continue
    else:
        print(ans)
        break

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slopeintercept(m, b, lowerx, upperx):
    """Slope intercept formula function"""
    y = []
    if type(lowerx) is int and type(upperx) is int and lowerx <= upperx:
        for x in range(lowerx, upperx+1):
            y.append((m*x)+b)
    else:
        return False
    return y

while True:
    rawinform = input("Put in point slope information to get out a list of y values! (Format m, b, lower x bound, upper x bound)!('exit to quit')")
    if rawinform.lower() == "exit":
        break
    if " " in rawinform:
        rawinform.replace(" ","")
    splitinf = rawinform.split(",")
    m = convert(splitinf[0])
    if m == False:
        print("Invalid slope :(")
        continue
    b = convert(splitinf[1])
    if b == False:
        print("Invalid y intercept :(")
        continue
    x1 = convert(splitinf[2])
    if x1 == False:
        print("Invalid lower bound :(")
        continue
    x2 = convert(splitinf[3])
    if x2 == False:
        print("Invalid upper bound :(")
        continue
    else:
        print(slopeintercept(m,b,x1,x2))
    

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

# q.f. - (-b +- sqrt(b^2 - 4ac))/2a
def sqrt(number):
    """This is a square root function"""
    answer = number**0.5
    return answer

while True:
    numbers = input("Put in the coefficients of a quadratic equation to get answer from the quadratic formula! a, b, c format!('exit to quit')")
    if numbers.lower() == "exit":
        break
    if " " in numbers:
        numbers.replace(" ","")
    newnumbers = numbers.split(",")
    for nm in newnumbers:
        if not nm.isdigit():
            print("Not valid input!")
            continue
    a = int(newnumbers[0])
    b = int(newnumbers[1])
    c = int(newnumbers[2])
    sqinputstr = str((b**2) - (4*a*c))
    sqinput = ((b**2) - (4*a*c))
    if "-" in sqinputstr:
        print("Square root input is negative--null")
        continue
    elif "-" not in sqinputstr:
        answ1 = ((-1*b) + sqrt(sqinput))/(2*a)
        answ2 = ((-1*b) - sqrt(sqinput))/(2*a)
        print(f"The answers to this are {answ1} and {answ2}!")
