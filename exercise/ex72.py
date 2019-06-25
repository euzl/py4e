# 연습문제 7.2
# 대충 mbox-short.txt 에서 'X-DSPAM ~ :' 으로 시작하는 줄이 SPAM인데, SPAM값의 평균을 출력하라는 문제!
fname = input("Enter file name: ")
fh = open(fname)
cnt = 0
sm = 0

for line in fh: # 한 줄씩 읽기
    if not line.startswith("X-DSPAM-Confidence:") : continue
    cnt += 1
    valueofline = line[line.find(':')+1:] # ':'숫자만 추출
    sm += float(valueofline) # float형으로 바꿔서 합산

print("Average spam confidence:", round(sm/cnt, 13)) # 소수점 13번째에서 반올림
