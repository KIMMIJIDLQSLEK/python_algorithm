input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for i in array:
        if i==number:
            return True
    return False


result = is_number_exist(3, input)
print(result)
#커밋 수정