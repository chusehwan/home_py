num_list = []
for i in range(10):
    a = int(input())
    b = a%42
    if b not in num_list:
        num_list.append(b)

print(len(num_list))