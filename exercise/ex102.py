# 연습문제 10.2
# mbox-short.txt 에서 메일을 받은 시각(hour)별로 카운트하고 sort해서 프린트!
name = input('Enter file:')
if len(name) < 1 : name = "mbox-short.txt"
hand = open(name) # 파일 열기

# 딕셔너리 생성
di = dict()
for lin in hand:
    if not lin.startswith("From "):
        continue
    lin = lin.rstrip() #\n제거
    wds = lin.split()
    # 시간 추출
    hr = wds[5].split(':') #':'기준 시간 짜르기
    di[hr[0]] = di.get(hr[0], 0) + 1 # 카운트

for h, c in sorted(di.items()):
    print(h, c)
