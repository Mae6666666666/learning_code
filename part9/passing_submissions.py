

class ExamSubmission:
    def __init__(self, examinee_temp: str, points_temp: int):
        self.examinee = examinee_temp
        self.points = points_temp

    def __str__(self):
        return str(self.examinee)





def passed(submissions: list, lowest_passing: int):
    lowest_passed = ExamSubmission("fake", 50)
    for submission in submissions:
        if submission.points > lowest_passed.points or submission.points > lowest_passing:
            lowest_passed.points = submission.points
    return lowest_passed












if __name__ == "__main__":
    sub_1 = ExamSubmission("Peter", 12)
    sub_2 = ExamSubmission("Pippa", 19)
    sub_3 = ExamSubmission("Paul", 15)
    sub_4 = ExamSubmission("Phoebe", 9)
    sub_5 = ExamSubmission("Persephone", 17)

# passes = passed([sub_1, sub_2, sub_3, sub_4, sub_5], 15)
calling_the_grade = passed([sub_1, sub_2, sub_3, sub_4, sub_5], 15)
print(calling_the_grade)
