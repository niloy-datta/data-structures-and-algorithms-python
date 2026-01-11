# Problem link: https://www.codingninjas.com/studio/problems/maximum-equal-stack-sum_1062571

def getsum(st):
    return sum(st)

def maxSum(st1: list, st2: list, st3: list) -> int:
    sum1 = getsum(st1)
    sum2 = getsum(st2)
    sum3 = getsum(st3)

    while True:
        if sum1 == sum2 and sum2 == sum3:
            break
        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= st1.pop()
        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= st2.pop()
        else:
            sum3 -= st3.pop()

    return sum1
