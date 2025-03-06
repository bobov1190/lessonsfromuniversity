nums = [1,2,3,4,5,6,7,8,9]
ev = []
odd = []
pri = []
no_pri = []


# for y in nums:
#     if y%2 == 0:
#         ev.append(y)
#     else:
#         odd.append(y)

for i in nums:
    is_prime = 1

    for j in range(2,i):
        if i%j == 0:
            is_prime = 0

    if is_prime == 0:
        no_pri.append(i)
    else:
        pri.append(i)


print(pri, no_pri)
