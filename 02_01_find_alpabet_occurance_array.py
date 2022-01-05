#string의 length만큼 반복
#string의 글자가 나올떄마다 array에 +1을 해준다


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for alpha in string:
        if alpha.isalpha():
            alphabet_occurrence_array[ord(alpha)-ord('a')]+=1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))



