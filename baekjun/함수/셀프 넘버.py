def d(n):
    string_n = str(n)
    sum = 0
    splited_string = list(string_n)
    for i in splited_string:
        sum += int(i)
    sum = sum + n
    return sum


new_list = []
for i in range(10000):
    num = d(i)
    new_list.append(num)
for a in range(10000):
    if a not in new_list:
        print(a)