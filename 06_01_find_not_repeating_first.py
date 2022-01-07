

input = "abadabac"


def find_not_repeating_character(string):
    list=[0]*26
    for i in string:
        list[ord(i)-ord('a')]+=1

    not_repeat_arr=[]

    for index in range(len(list)):  #list의 길이만큼 index반복(0...25)
        if list[index]==1:  #list에 들어있는 값이 1이면
            not_repeat_arr.append(chr(index+ord('a')))#index+97을 문자로 바꿔 not_repeat_arr에 추가한다

    for char in string:            #문자열을 다시 돌려 not_repeat_arr(=>'c','d')가 존재하면
        if char in not_repeat_arr:
            return char            #바로 반환=>'d'


result = find_not_repeating_character(input)
print(result)