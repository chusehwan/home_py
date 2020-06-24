value = int(input())

if value%2 == 0:
    first_line = int(value /2)
    one_result = '* ' * first_line
else:
    first_line = int(round(value/2+1,1))
    one_result = '* ' * first_line

second_line = value - first_line
two_result = ' *' * second_line

for i in range(value):
    print(one_result)
    print(two_result)