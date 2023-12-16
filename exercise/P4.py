#在1-50中随机生成一个数字，你来猜，只有6次机会
import random

def guessNUmberGame():
    secretNum = random.randint(1,50)
    print(secretNum)
    print("请从1-50中猜出我心里的数字吧。")
    times=0
    guessNum = int(input("我猜是："))
    while times < 5:
        if guessNum == secretNum:
            print(f"恭喜你，你一共花了{times}次！")
            break
        elif guessNum > secretNum:
            guessNum = int(input("不对哦，你猜大了，再猜："))
            times += 1
        elif guessNum < secretNum:
            guessNum = int(input("不对哦，你猜小了，再猜："))
            times += 1
    if times == 5:
        print(f"你把游戏次数用完了都没有猜对哦，我心里的数字是{secretNum}，下次再接再厉吧！")

guessNUmberGame()