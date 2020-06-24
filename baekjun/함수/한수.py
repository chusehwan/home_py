num = int(input())
count_hansu = 0

def check_list(han_li):
    # list상 index 바탕 각 수사이의 차이 수가 일정한지 검토( [1,0,0] = 한수아님, [1,0,1] =한수아님, [1,1,1] = 한수, ....[1,2,3] = 한수)
    compare_list = []
    len_of_han_li = len(han_li)
    for i in range(len_of_han_li):
        if i+1 < len_of_han_li:
            compare_list.append(int(han_li[i+1])-int(han_li[i]))
    for i in compare_list:
        if compare_list[0] != i:
            return '한수아님'
    return '한수'


def judge_num(num):
    if num < 100:
        return '한수'
    str_num = str(num)
    # 두자리 이상일경우 list를 만들어서 각 자리수를 list에 저장
    han_list = []
    for i in str_num:
        han_list.append(i)
    result = check_list(han_list)
    return result


for i in range(num):
    if judge_num(i+1) == '한수':
        count_hansu+=1

print(count_hansu)
