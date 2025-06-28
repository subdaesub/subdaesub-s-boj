cnt = 0
credit = 0
for _ in range(20):
    k = input()
    if k[-1] != 'P':
        if k[-1] == 'F':
            score = int(k[-5])
            credit += score
            grade = k[-2:]
        else:
            score = int(k[-6])
            credit += score
            grade = k[-2:]
        if grade == 'A+':
            cnt += score * 4.5
        elif grade == 'A0':
            cnt += score * 4.0
        elif grade == 'B+':
            cnt += score * 3.5
        elif grade == 'B0':
            cnt += score * 3.0
        elif grade == 'C+':
            cnt += score * 2.5
        elif grade == 'C0':
            cnt += score * 2.0
        elif grade == 'D+':
            cnt += score * 1.5
        elif grade == 'D0':
            cnt += score * 1.0
print(cnt / credit)