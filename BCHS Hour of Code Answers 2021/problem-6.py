slope = int(input("What is the slope of the line? "))
yInt = int(input("What is the y-intercept of the line? "))
equation = "y = " + str(slope) + "x + " + str(yInt)
print(equation)
xL = int(input("What is the lower x-constraint? "))
xU = int(input("What is the upper x-constraint? "))
integral = (1 / 2) * ((slope * xL + yInt) + (slope * xU + yInt)) * (xU -xL)
print("The integral of", equation, "from", str(xL), "to", str(xU), "is",
str(integral) + ".")
