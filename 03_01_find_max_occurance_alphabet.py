#for문이용하여 list를 만들어서 빈도수 구하기
#for문 이용하여 빈도수 많은 알파벳 나타내기
input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    alphabet_list=[0]*26
    for alpha in string:
        if alpha.isalpha():
            alphabet_list[ord(alpha)-ord('a')]+=1


    max=0
    max_alpha=''
    for num in alphabet_list:
        if alphabet_list[num]>max:
            max=num
            max_alpha=chr(num+ord('a'))
    return max_alpha


result = find_max_occurred_alphabet(input)
print(result)