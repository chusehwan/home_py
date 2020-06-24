num = int(input())
list_OX = []
for i in range(num):
    list_OX.append(input())
score_list = []
for i in list_OX:
    score = 0
    abc = 1
    for a in i:
        if a == 'O':
            score = score + abc
            abc += 1
        elif a == 'X':
            abc = 1

    score_list.append(score)

for b in score_list:
    print(b)