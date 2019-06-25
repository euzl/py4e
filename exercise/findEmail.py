# 'mbox-short.txt' 에서 이메일만 추출하는 프로그램
# 2019-06-26
# email만 뽑아내는 데는 성공했지만, '<'나 '>;'와 같은 이메일과 붙어있는 친구들을 제거하지 못했다.

fhand = open('mbox-short.txt') # 파일 열기
email = list() # email 이라는 리스트 생성

for line in fhand: # fhand를 한 줄씩 읽기
    if '@' in line: # @가 있으면
        word = line.split() # 빈칸을 구분자로 word에 저장
    else:
        continue

    for dvd in word: # word를 한 값씩
        if '@' in dvd: # @가 있으면
            email.append(dvd) # email에 추가!
            
print(email) # email만 출력.
