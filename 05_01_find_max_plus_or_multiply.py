#value값이 0이거나 1일경우 더하기
#i값이 0이거나 1일경우 더하기
#나머지는 곱하기
input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    value=0
    for i in array:
        if i<=1 or value<=1:
            value+=i
        else:
            value*=i
    return value


result = find_max_plus_or_multiply(input)
print(result)