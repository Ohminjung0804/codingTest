

#1단계 . 리스트에 들어있는 각 자연수의 개수를 센다.

arr=[1,2,3,3,1,3,3,2,3,2]
count=[0]*4

for x in arr:
    count[x]+=1


#2단계 . 가장 많이 등장하는 수의 개수를 구한다.
counter=[0,2,3,5]

def 최대값(arr):
    large=0
    for x in arr:
        if x>large:
            large=x
    return large

#3단계 . 가장 적게 등장한느 수의 개수를 구한다.
def 최소값(arr):
    기존값=1001
    for x in arr:
        if x < 기존값 and x != 0:
            기존값=x
    최소 = 기존값
    return 최소

#4단계 . 가장 많이 등장하는 수가 가장 적게 등장하는 수보다 몇배 더 많은지 구한다.

def solution(arr):
    max_cnt=최대값(arr)
    min_cnt=최소값(arr)
    return max_cnt // min_cnt



#Press Run button to receive output.
ret = solution(arr)
print("Solution: return value of the function is", ret, ".")