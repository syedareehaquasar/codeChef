tc = int(input())
while tc > 0:
    s = input()
    ans = 0
    for i in range(len(s) -1):
        if s[i] != s[i+1]:
            ans += 1
    print(ans)
    tc -= 1