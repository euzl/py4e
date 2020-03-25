# 2-1 강의자료 마지막 연습문제
# input으로 받은 값을 int(a)로 변환하는 것의 중요성 때문에 올림!

def inputData():
    a = -1
    _listA = []
    while 1:
        a = input()
        # 꼭 필요한 부분! 
        # int형으로 바꾸지 않으면 a는 'str'이기 때문에 if문의 조건에 해당되지 않아 무한루프를 돌게 된다.
        a = int(a)
        if a == 0:
            break
        _listA.append(a)
    return _listA


listA = inputData()


def dataProcess(a):
    if len(a) == 2:
        print(a[0]*a[1])
        print((a[0] + a[1])*2)
    elif len(a) == 3:
        print(a[0]*a[1]*a[2])


dataProcess(listA)
