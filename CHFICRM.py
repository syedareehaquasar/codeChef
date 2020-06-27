def sol(ele):
    a5, a10, a15 = 0, 0, 0
    flag = 0
    for e in ele:
        if e == 5:
            a5 += 1
        elif e == 10:
            if a5 != 0:
                a5 -= 1
                a10 += 1
            else:
                flag = 1
        elif e == 15:
            if a10 != 0:
                a10 -= 1
                a15 += 1
            else:
                flag = 1
    if flag == 1:
        return 'NO'
    return "YES"

tc = int(input())
while tc > 0:
    n = int(input())
    ele = [int(x) for x in input().split()]
    print(sol(ele))
    tc -= 1