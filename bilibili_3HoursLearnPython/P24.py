def calcuBMI(shengao,tizhong):
    print(f"您的身高是：{shengao}，您的体重是：{tizhong}")
    BMI=tizhong / (shengao**2)
    fenlei=''
    if BMI <= 18.3:
        fenlei = '偏瘦'
    elif BMI <= 25:
        fenlei = '正常'
    elif BMI <= 30:
        fenlei = '偏胖'
    else:
        fenlei = '肥胖'
    print(f"您的BMI是{BMI},BMI分类是{fenlei}")
calcuBMI(1.6,53)