# 연습문제 3.1
## Rewirte your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
## 40시간을 초과한 시간에는 1.5배 더 지급하는 급여계산 프로그램작성
hour = input('Enter Hours: ')
rate = input('Enter Rate: ')

fh = float(hour)
fr = float(rate)

if fh> 40:
    pay = fh*fr + (fh-40)*(fr*0.5) #기본급여 + 40시간초과에만 0.5배 더주기
else :
    pay = fh*fr

print('Pay: ', pay)
