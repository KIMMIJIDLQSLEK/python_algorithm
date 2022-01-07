#반복문을 통해 list만들기
#list를 차례로 돌며 1인값 반환

input = "abadabac"


def find_not_repeating_character(string):
    list=[0]*26
    for i in string:
        list[ord(i)-ord('a')]+=1

    for i in string:
        if list[ord(i)-ord('a')]==1:  #문자열의 순서대로 문자에 해당하는 list안의 값이 1이면 바로 반환
            return i

    return "존재하지 않음"


result = find_not_repeating_character(input)
print(result)