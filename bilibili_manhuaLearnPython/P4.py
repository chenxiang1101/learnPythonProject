scoreALL={'xiaoming':[85,96,88],'xiaoliang':[83,69,75],'xiaohong':[72,80,91]}
maxSum=0
maxSumName=''
minSum = float('inf')  # 设置初始最小总分为正无穷大
minSumName=''
for key,value in scoreALL.items():
    #计算个人总分：
    sum=0
    for i in range(len(value)):
        sum += value[i]
        #检查最大总分
        if sum >= maxSum:
            maxSum = sum
            maxSumName = key
    # 检查最小总分：放到循环外，确保在迭代完所有人后再进行比较
    if sum <= minSum:
        minSum = sum
        minSumName = key

    print("{}的总分是：{}".format(key,sum))
print('总分最高的是：{}，ta的分数是：{}'.format(maxSumName,maxSum))
print('总分最低的是：{}，ta的分数是：{}'.format(minSumName,minSum))
