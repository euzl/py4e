# 10장 실습
# clown.txt 에서 자주 나오는 단어 상위 5개 출력
name = input('Enter file:')
if len(name) < 1 : name = "clown.txt"
hand = open(name) # 파일 열기

# 딕셔너리 생성
di = dict()
for lin in hand:
    lin = lin.rstrip() #\n제거
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w, 0) + 1

lst = list()
for k, v in di.items():
    lst.append((v, k))

lst = sorted(lst, reverse=True)
print("상위5개단어:", lst[:5])
