def printLine(times):
    print("this is an example called: "+str(times))


for i in range(1,10):
    printLine(i)

def add(a=10,b=30):
    return a+b

ans=add(100,234)

print("Answer is"+str(ans))

celsius = int(input("Please enter an integer value for degrees celsius. "))


def fahrenheit(cel):
    # To avoid the approximation error that would occur if the float 1.8 was used in the calculation, 1.8 * 10 is used
    # instead, resulting in the integer 18.  To balance this out, 32 is also multiplied by 10 to get 320.  After the
    # calculations in the parentheses are finished, the result is divided by 10, which gives the correct Fahrenheit
    # temperature.
    return (18 * cel + 320) / 10


print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")
