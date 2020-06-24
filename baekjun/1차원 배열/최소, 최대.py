num = int(input())

samples = input()
samples = samples.split()
# get max num

min_num = samples[0]
max_num = samples[0]

for i in samples:
    if int(i) < int(min_num):
        min_num = int(i)

for i in samples:
    if int(i) > int(max_num):
        max_num = int(i)

print(min_num, max_num)
