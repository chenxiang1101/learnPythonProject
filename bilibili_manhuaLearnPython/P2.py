rabbit=3
print('请输入N的值：')
N = int(input())
print('您输入的N为：{}'.format(N))
for i in range(0,N):
    rabbit = rabbit * 2
print('{} 年后的兔子数量为 {}'.format(N,rabbit))

sum=0
for i in range(1,N+1):
    sum += i
print('1+2+3+……+{}的总和为:{}' .format(N,sum))