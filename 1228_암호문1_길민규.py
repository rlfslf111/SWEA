# import sys
# sys.stdin = open('input.txt','r')

for t in range(10):
    origin_len = int(input())
    origin = list(input().split())
    order_gesu = int(input())
    order = list(input().split())

    for x in range(len(order)):
        if order[x] == 'I':
            limint = int(order[x+2])
            for i in range(x+3+limint-1,x+2,-1):
                origin.insert(int(order[x+1]),order[i])

    ans = []
    for x in range(10):
        ans.append(origin[x])
    print('#{} {}'.format(t+1,' '.join(ans)))