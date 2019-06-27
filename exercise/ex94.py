# 연습문제 9.4
# 메일 제일 많이 보낸 사람 찾아서 출력
name = input('Enter file:')
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name) # 파일 열기

# 딕셔너리 생성
sender = dict() # 보낸사람 딕셔너리 생성
for line in handle:
    if line.startswith("From "):
        line = line.split()
        sender[line[1]] = sender.get(line[1], 0) + 1 #line[1]이 이메일주소 (처음 보냈으면 생성하고) ++1

# 제일 많이 보낸 사람 찾기
maddr = None
mcnt = 0
for aa, cc in sender.items(): #(aa,cc)에 쌍을 이루어 ~~
    if cc>mcnt:
        maddr = aa
        mcnt = cc

print(maddr, mcnt)
