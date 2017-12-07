from function import collatz
try:
    x = int(input("Type a number"))
except ValueError:
    x = int(input("Please type a number"))
while x != 1:
    x = collatz(x)
