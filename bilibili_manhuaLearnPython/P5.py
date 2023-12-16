print("提示：score < 60 积0分，60 <= score < 90 积1分，score >= 90 积2分")
score1 = int(input("请输入你的第一门成绩："))
score2 = int(input("请输入你的第二门成绩："))
score3 = int(input("请输入你的第三门成绩："))
sumScore = score1 + score2 + score3

# 修正逻辑运算符为and，并使用正确的括号顺序
jifen1 = (score1 < 60) * 0 + (60 <= score1 < 90) * 1 + (score1 >= 90) * 2
jifen2 = (score2 < 60) * 0 + (60 <= score2 < 90) * 1 + (score2 >= 90) * 2
jifen3 = (score3 < 60) * 0 + (60 <= score3 < 90) * 1 + (score3 >= 90) * 2
sumJifen = jifen1 + jifen2 + jifen3

print("您的分数为{}，您的总积分为{}".format(sumScore, sumJifen))
