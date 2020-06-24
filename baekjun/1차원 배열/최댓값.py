int_samples = []

for i in range(9):
    int_samples.append(int(input()))

max_num = int_samples[0]

for i in int_samples:
    if i>max_num:
        max_num = i

for i in range(9):
    if max_num == int_samples[i]:
        a = i+1

print(max_num)
print(a)
