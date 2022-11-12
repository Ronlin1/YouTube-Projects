h = eval(input("Please enter height: "))

# top half of the diamond
for x in range(h):
    print(" " * (h-x), "*" * (2*x + 1))

# bottom-half
for x in range(h-2, -1, -1):
    print(" " * (h-x), "*" * (2*x + 1))
