#0에서 1로 바뀌는 시점/ 1네서 0으로 바뀌는 시점에서 0과 1의 첫번째 원소의 빈도수를 세면됨
#문자열의 첫번째 카운트
#01일경우 0으로 바꿔야하므로 1 빈도수 카운트
#10일경우 1로 바꿔야하므로 0 빈도수 카운트

input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zero=0
    one=0
    if string[0]=='1':
        zero+=1
    if string[0]=='0':
        one+=1

    for i in range(len(string)-1):
        if string[i]!=string[i+1]:
            if string[i+1]=='0':
                one+=1
            elif string[i+1]=='1':
                zero+=1

    if one>zero:
        return zero
    else:
        return one



result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)