print("Number 1:")
n1 = int(input())
print("Number 2:")
n2 = int(input())
if n1 % 2 == 0:
    n1even = True
else:
    n1even = False
if n2 % 2 == 0:
    n2even = True
else:
    n2even = False
if n1even and n2even:
    print("Gordon wins")
elif not n1even and not n2even:
    print("Charlie wins")
else:
    print("Nikhil wins")

#Alternate Solution:
print("Number 1:")
n1 = int(input())
print("Number 2:")
n2 = int(input())
if (n1 * n2) % 2 == 1:
    print("Charlie wins")
elif (n1 + n2) % 2 == 0:
    print("Gordon wins")
else:
    print("Nikhil wins")