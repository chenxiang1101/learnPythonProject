class Student():
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.scoreYu = 0
        self.scoreMath = 0
        self.scoreEnglish = 0
    def set_score(self,scoreYu,scoreMath,scoreEnglish):
        self.scoreYu = scoreYu
        self.scoreMath = scoreMath
        self.scoreEnglish = scoreEnglish
    def print_scores(self):
        print(f"{self.name}(学号{self.id})的语文成绩为{self.scoreYu},数学成绩为{self.scoreMath}，英文成绩为{self.scoreEnglish}")

chen = Student("chen","0001")
chen.set_score(100,90,85)
chen.print_scores()