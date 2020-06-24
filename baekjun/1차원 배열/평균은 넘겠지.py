test_cases = int(input())
input_numbers = []
# 테스트 케이스 횟수만큼 잇풋 넘버를 받는다
for i in range(test_cases):
    input_numbers.append(input())

for test_case in input_numbers:
    each_case = test_case.split()
    new_list = []
    for element in each_case:
        new_list.append(int(element))

    average = sum(new_list[1:])/new_list[0]
    num_of_over_average = 0
    for element in new_list[1:]:
        if element > average:
            num_of_over_average += 1
    result = float(num_of_over_average)/float(new_list[0])*100
    print("%0.3f" % result + '%')


# 3
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80