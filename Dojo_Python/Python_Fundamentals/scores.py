import random

def scores(num):

    grade = ''
    i = 0
    # print grade, i
    while (i < num):
        score = random.randint(60,100)

        if (score < 70):
            grade = 'D'
            # print score, grade
        elif (70 < score < 80):
            grade = "C"
            # print score, grade
        elif (80<score<90):
            grade = "B"
            # print score, grade
        else:
            grade = "A"

        i += 1
        # print i
        print "Score #",i,"is", score,"; your grade is", grade

print scores(10)
