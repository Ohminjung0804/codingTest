#숫자를 입력하고 입력받는 숫자가 몇 번 박수를 치는지 알아보자

#방법 2 : 컴퓨터가 생각하는 방법
a= 31
문자열 = str(a)

카운트 = 0

while a:
    if a % 10 in [3,6,9]:
        카운트 += 1
        a=a // 10
print(카운트)

