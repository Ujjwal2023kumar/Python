# Python Loops and Conditional Statements Demonstration

print("===== LOOPS =====")
# 1. for loop
print("\n1. for loop:")
for i in range(3):
    print(i, end=" ")
print()

# 2. while loop
print("\n2. while loop:")
x = 0
while x < 3:
    print(x, end=" ")
    x += 1
print()

# 3. nested loops
print("\n3. nested loops:")
for i in range(2):
    for j in range(2):
        print(f"({i},{j})", end=" ")
print()

# 4. loop with else
print("\n4. loop with else:")
for i in range(2):
    print(i, end=" ")
else:
    print("\nLoop completed without break")

print("\n===== CONDITIONAL STATEMENTS =====")
x = 7

# 1. if statement
print("\n1. if statement:")
if x > 5:
    print("x is greater than 5")

# 2. if-else statement
print("\n2. if-else statement:")
if x > 10:
    print("x > 10")
else:
    print("x <= 10")

# 3. if-elif-else ladder
print("\n3. if-elif-else ladder:")
if x > 10:
    print("x > 10")
elif x > 5:
    print("x > 5 but <= 10")
else:
    print("x <= 5")

# 4. nested if
print("\n4. nested if:")
if x > 5:
    if x % 2 == 0:
        print("x > 5 and even")
    else:
        print("x > 5 and odd")

# 5. shorthand if (single-line if)
print("\n5. shorthand if:")
y = 8
if y % 2 == 0: print("y is even")

# 6. shorthand if-else (ternary)
print("\n6. shorthand if-else (ternary):")
result = "Even" if y % 2 == 0 else "Odd"
print(f"y is {result}")

# 7. pass in condition
print("\n7. pass in if statement:")
z = 3
if z > 5:
    pass  # do nothing
else:
    print("z <= 5")
