#price : 원가, grade : 회원등급
def solution(price, grade): #s 5프로, G 10프로, V 15프로
    reduced_price =0
    if grade == "S":
        return price - price *0.05
    elif grade == "G":
        return price - price *0.10
    elif grade == "V":
        return price - price *0.15


#testcase를 위한 output
price1 =5000
grade1="S"
ret1=solution(price1,grade1)

price1 =2500
grade1="V"
ret1=solution(price1,grade1)

price2 =96900
grade2="S"
ret2=solution(price2,grade2)