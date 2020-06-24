num = int(input())
scores = input()
scores = scores.split()
int_scores = []
for i in scores:
    int_scores.append(int(i))

max_score = int_scores[0]
for i in int_scores:
    if i>max_score:
        max_score = i

convert_scores = []

for i in int_scores:
    b = i/max_score*100
    convert_scores.append(b)

# get sum
sum_score = 0
for i in convert_scores:
    sum_score = sum_score+i

average = sum_score/num
print(average)