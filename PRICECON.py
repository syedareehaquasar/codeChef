def sol(n, k, ele):
    ir= sum(ele)
    if ir <= k * n:
        return 0
    fr = ir
    for i in ele:
        if i > k:
            fr -= (i-k)
    return ir - fr

tc = int(input())
for i in range(tc):
    n, k = [int(x) for x in input().split()]
    ele = [int(e) for e in input().split()]
    print(sol(n, k, ele))