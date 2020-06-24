num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
result = num_1*num_2*num_3

result = str(result)
num_list = []

def get_num(li, num):
    re = 0
    for i in li:
        if str(num) == i:
            re += 1
    return re

for i in range(10):
    a = get_num(result, i)
    num_list.append(a)

for i in num_list:
    print(i)