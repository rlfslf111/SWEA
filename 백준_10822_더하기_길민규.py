num = input().split(',')
ans = 0
for i in range(len(num)):
    ans += int(num[i])
print(ans)