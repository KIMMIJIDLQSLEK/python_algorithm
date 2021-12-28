input=[3,5,6,1,2,4]

def find_max_num(array):
    max=array[0]
    for arr in array:
        if max<arr: max=arr
    return max

result=find_max_num(input)
print(result)

ㄴㅇㅁㅇㅎ