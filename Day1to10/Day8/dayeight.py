import re
# arr = [1,2,3,4,66,78,100]
#
# x = int(input('Enter a number: '))
#
# if x in arr:
#     print('Number Found')
# else:
#     print('Number not found')


# num = 12456
# reverse = 0
#
# while num > 0:
#     rem = num % 10
#     reverse = (reverse * 10) + rem
#     num = num // 10
# #TODO after reverse, sort it in descending order
# print(reverse)

#Q3
# def get_grade(s1, s2, s3):
#     ave = (s1 + s2 + s3) / 3
#     if 90 <= ave <=100:
#         print('A')
#     elif 80 <= ave < 90:
#         print('B')
#     elif 70<= ave < 80:
#         print('C')
#     elif 60<= ave < 70:
#         print('D')
#     return 'F'
#
# get_grade(90, 55, 52)

#Q4
# def reverse_list(lst):
#     new_lst = lst[::-1]
#     return new_lst
#
# lst = [[1,2,3,4], [4,3,2,1]]
# print(reverse_list(lst))
#
# #Q5
# def add_int_to_bin(num1, num2):
#     sum = bin(num1 + num2)[2:]
#     return sum
#
# print(add_int_to_bin(1,1))
#
# def add_binary(num1, num2):
#     return bin(int(num1, 2) + int(num2, 2))[2:]
# print(add_binary('1001','0001'))
#
# #Q6
# def odd_or_even(arr):
#     if sum(arr) % 2 == 0:
#         return 'even'
#     return 'odd'
# print(odd_or_even([2,2,2]))

a = '1234'
pattern = '\d{3}'
result = re.match(pattern, a)
if result:
    print('Valid')
else:
    print('Invalid')