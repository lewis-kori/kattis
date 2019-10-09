# https://open.kattis.com/problems/bijele

required = [1,1,2,2,2,8]
have   = [int(x) for x in input().split()]

difference = []
for i in range(len(required):
    difference.append(required[i] - have[i])

print(" ".join([str(x) for x in difference]))
