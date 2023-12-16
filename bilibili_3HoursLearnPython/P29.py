class employSystem():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def print_info(self):
        print(f"{self.name}的工号是{self.id}")
    def calculate_monthly_pay(self):
        pass
class FullTimeEMployee(employSystem):
    def __init__(self,name,id,monthly_salary):
        super().__init__(name,id)
        self.monthly_salary=monthly_salary
    def calculate_monthly_pay(self):
        print(f"{self.name}（工号：{self.id}）的月薪为:{self.monthly_salary}")

class PartTimeEMployee(employSystem):
    def __init__(self,name,id,daily_salary,work_days):
        super().__init__(name,id)
        self.monthly_salary=daily_salary * work_days
    def calculate_monthly_pay(self):
        print(f"{self.name}（工号：{self.id}）的月薪为:{self.monthly_salary}")

full = FullTimeEMployee("chen","0001",25000)
full.calculate_monthly_pay()

part = PartTimeEMployee("Cathy","0002",1000,20)
part.calculate_monthly_pay()

# 结果：
# chen（工号：0001）的月薪为:25000
# Cathy（工号：0002）的月薪为:20000