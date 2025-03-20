# v = [2.0, 3.1, 4.3, -10.6, -2.0, 5.2, 1.2, 8.9, 3.1, -9.2, 8.3]

# all_groups = []
# current_group = []
# start_point = 0

# for index, number in enumerate(v):
#     if number >= 0:
#         if len(current_group) == 0:
#             start_point = index
#         current_group.append(number)
#     else:
#         if len(current_group) > 0:
#             all_groups.append((start_point, current_group))
#             current_group = []

# if len(current_group) > 0:
#     all_groups.append((start_point, current_group))

# print("Results:")
# for position, group in all_groups:
#     print(f"starting point {position} in the list {group}")

numbers = []

print("Enter positive numbers (enter a negative number to stop):")
while True:  
    num = int(input("Enter a number: ")) 
    if num < 0:  
        break
    numbers.append(num)

while len(numbers) < 200:
    numbers.append(0)

compacted_numbers = []
for num in numbers:
        compacted_numbers.append(num)

while len(compacted_numbers) < 200:
    compacted_numbers.append(0)

print("\nThe compacted array (non-zero elements):")
for num in compacted_numbers:
    if num != 0:
        print(num, end=" ")
