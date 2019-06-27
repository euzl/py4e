# 연습문제 8.4
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip() # 개행문자 제거
    word = line.split()
    for nw in word:
        if nw not in lst:
            lst.append(nw)

lst.sort()
print(lst)
