s = input()
len_s = len(s)
s_list = []
for i in range(len_s):
    s_list.append(s[i])

print_result = ''
for i in range(26):
    if chr(97+i) not in s_list:
        print_result = print_result + '-1 '
    else:
        print_result = print_result+(str(s_list.index(chr(97+i))))+' '

print(print_result)