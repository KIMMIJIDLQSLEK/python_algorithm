#반복문을 이용해 20번 돌림
#자신의 숫자를 제외한 이전 숫자로 나눌떄 나머지가 0이면 소수임
#자신의 숫자 전까지 num=1(나머지가 0이다/나눠진다/약수)이면 소수가 아님
#num=0(나눠지지않는다/1,자기자신만)일때만 소수

input = 20


def find_prime_list_under_number(number):
    prime_list=[]
    for i in range(number+1)[2:]:
        num=0
        for j in range(i+1)[2:]:
            if i!=j:
                if i%j!=0:
                   continue
                else:
                    num=1

            if i==j and num==0:
                prime_list.append(i)
                break

    return prime_list


result = find_prime_list_under_number(input)
print(result)