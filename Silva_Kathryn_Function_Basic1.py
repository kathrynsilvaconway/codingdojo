# 1.
# def a():
#     return 5
#     print(a())

# Expected Output: 5
# Actual Output: 5

# 2.
# def a():
#     return 5
# print(a() + a())

# Expected Output: 10
# Actual Output: 5,10
# * I did not expect it to print the first 5, I just thought it would print the sum. Will have to research this.

# 3.
# def a():
#     return 5
#     return 10
# print(a())

# Expected Output: 5, 10
# Actual Output: 5
# * I forgot that return statement break a loop. Oops.

# 4.
# def a():
#     return 5
#     print(10)
# print(a())

# Expected Output: 5
# Actual Output: 5
# * Return statement broke the loop. Couldn't get me a second time with that.

# 5.
# def a():
#     print(5)
# x = a()
# print(x)

# Expected Output: 5
# Actual Output: 5, None
# * It gives me None because the print statement doesn't actually return a value.
#   I get that, but I don't understand why it shows the 5 at the same time. More research needed.

# 6.
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

# Expected Output: 8
# Actual Output: 3,5
# *Just prints both. Print function doesn't actually add?

# def a(b,c):
#     return str(b) + str(c)
# print(a(2,5))

# Expected Output: 25
# Actual Output: 25

# 8.
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())

# Expected Output: 100,10,7
# Actual Output: 100,10
# *I thought the last return would execute because it is outside of the other loop. Return ends the function.

# 9.
# def a(b,c):
#     if b < c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))

# Expected Output: 7,14,7,14
# Actual Output: 7,14,21
# *I thought it would print the last two separately, as it it did above in #6. I guess it adds them because
# there is return statement in the function?

# 10.
# def a(b,c):
#     return b + c
#     return 10
# print(a(3,5))

# Expected Output: 8
# Actual Output: 8

# 11.
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

# Expected Output: 500,500,300,500
# Actual Output: 500,500,300,500

#12.
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)

# Expected Output: 500,500,300,300,500
# Actual Output: 500,500,300,500
# *No clue why this only prints 300 once.

#13.
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return(b)
# print(b)
# b = a()
# print(b)

# Expected Output: 500,500,300
# Actual Output: 500,500,300,300
# *Now it prints 300 twice? Why? What is the difference?

# 14.
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()

# Expected Output: 1,3,2
# Actual Output: 1,3,2

# 15.
def a():
    print(1)
    x = b()
    print(x)
    return(10)
def b():
    print(3)
    return 5
y = a()
print(y)

# Expected Output: 1,3,5,10
# Actual Output: 1,3,5,10





