def collatz(number):
    result = 0
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    if number % 2 == 1:
        result = 3*number+1
        print(result)
        return result

inputNum = int(input("请输入一个正整数："))
try:
    if  type(inputNum) == int and (inputNum > 0):
        while inputNum != 1:
            inputNum = collatz(inputNum)
except ValueError:
    print("你输入的不是正整数，程序结束！")

