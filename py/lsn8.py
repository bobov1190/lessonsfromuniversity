# Exercise 3.2

# v = [5,1,7,9,11,13,2,17,19,21]
# w = [3,33,-4,5,6,0,1,1,19,17]

# c = []

# max_number = 0

# for i in v:
#     for j in w:
#         a = i-j

#         if  a < 0:
#             a = 0 - a

#         c.append(a)

#         max_number = c[0]

#         for num in c:
#             if num > max_number:
#                 max_number = num

# print(f"Самое большое число в списке: {max_number}")

# Exercise 3.1

# v = [5,1,7,9,11,13,2,17,19,21]
# w = [3,33,-4,5,6,0,1,1,19,17]

# c = []

# max_number = 0

# for i in range(len(v)):
#     a = v[i] - w[i]

#     if a < 0:
#         a = 0-a

#     c.append(a)

# for num in c:
#     if num > max_number:
#         max_number = num


# print(f"Самое большое число в списке: {max_number} , а список: {c}")

# Exercise 3.3

# base = [1,-2,3,4,-5]
# exp = [4,3,2,3,2]

# c = []

# for i in range(len(base)):
#     a = base[i] ** exp[i]
#     c.append(a)

# print(f"Powers: {c}")


v = [2.0,3.1,4.3,-10.6,-2.0,5.2,1.2,8.9,3.1,-9.2,8.3]

positive_subsequence = [num for num in v if num > 0]
print(positive_subsequence)
