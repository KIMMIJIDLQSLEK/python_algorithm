#array의 길이구하기
#길이만큼 반복하여 i와 i+1의 곱셈과 더하기 비교
#비교하여 더 큰 값으로 곱하기
input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(arr):
    value=arr[0]
    for i in arr[1:]:
        if value*i>value+i:
            value=value*i
        else:
            value=value+i

    return value


result = find_max_plus_or_multiply(input)
print(result)