# 연습문제 7.1
# 파일이름을 입력받아 한 줄씩 대문자로 출력

fname = input("Enter the file name:")
try:
    fhand = open(fname)
except:
    print("File cannot be opened: ", fname)
    quit()

for line in fhand:
    line.rstrip() # 오른쪽 개행문자('\n')제거
    print(line.upper()) # upper case 로 출력
