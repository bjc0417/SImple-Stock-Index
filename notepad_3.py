# 분수 찾기
# n = n번째
n = int(input())
x = 1
i = 2

cnt = 1

# n번째는 몇번째 그룹에 포함되는가?
while True:
    if n == 1:
        break

    elif x <= n <= x+i:
        cnt += 1
        break    
    else:
        x = x + i
        i += 1 
        cnt += 1

# 그룹안에서 n번째 유추
seq = n - x
frac_lst = []
a = cnt
b = 1

for i in range(cnt):
    frac_lst.append("{}/{}".format(a,b))
    if n == 1:
        frac_lst[0] = '1/1'
        break
    elif n == 2:
        frac_lst.insert(0,'1/2')
        
        
    elif n == 3:
        frac_lst.append('2/1')
    elif a >= 1 and b <= cnt:
        a -= 1
        b += 1
print(frac_lst[seq-1])
