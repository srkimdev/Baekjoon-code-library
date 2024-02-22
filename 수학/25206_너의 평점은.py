time_sum = 0
sum = 0

hakjeom = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
jeomsu = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

for _ in range(20):
    subject, time, grade = input().split() # 과목, 학점, 평점

    if grade != 'P':
        sum = sum + float(time) * jeomsu[hakjeom.index(grade)]
        time_sum = time_sum + float(time)

print('{:.6f}'.format(sum / time_sum))