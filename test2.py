def 보조함수(month, day):
    month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    total=0;
    for i in range(month-1):
        total +=month_list[i]
    total +=i
    return total-1

#def solution
