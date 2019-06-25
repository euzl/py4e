# 파이썬 정리(C++과의 차이점을 중점으로)
파이썬을 공부하며 C++과 다르거나 헷갈리는 개념 위주로 정리하고자 함
 1. 기본
 2. 함수
 3. 반복문
 4. 파일
 5. 
            
---            
### 기본
- 주석 : `#`기호사용
- 문장의 끝에 세미콜론(;)을 붙히지 않는다!!
- 논리연산자
	- `&&` 대신 `and` 사용 `||` 대신 `or` 사용
	- `not` 도 있다!
- True/False 로 표기 (첫글자 대문자!)
- `cnt++` <- 사용불가. `cnt += 1` <- 사용가능
- `==`은 값만 비교하지만 /  `is`, `is not`은 자료형과 값 모두 비교
- `print()` 함수사용하면 개행문자('\n') 추가됨

#### 반올림
```python
round(실수, n)     #소수점 n번째 까지만 표현하고 반올림
round(실수)        # 소수점 첫번째자리를 반올림. (정수만 남음)
round(실수, -1)    # 첫번째자리에서 반올림. (정수도 가능)
```

#### 소수점 올림, 내림, 버림
```python
import math      # math 클래스에서 사용해야됨!
math.ceil(실수)   #올림
math.floor(실수)  #내림
math.trunc(실수)  #버림
```
          
### 입력 및 출력
```python
name = input()     # 값을 입력받을 수 있다. -- 문자열로 받음
print(name)        # name에 저장된 값 출력

name = input('What your name?')   # What your name? 이라고 물어보면 입력할 수 있다.
print('Hi ', name)                # Hi 라는 문자열과 함께 출력
```
           
### 타입 변환 및 확인
```python
i = 42
type(i)      # int 반환
j = 1.5
type(j)      # float
j = int(j)   # int 형으로 바뀜
type(j)      # int 반환
print(j)     # '1' 출력
```

 - `type(<변수명>)` -> 타입 반환 
 - `float(<변수명>)` -> 타입 변환 // float, int 등.  단, 변환이 될 때만! str에서 int 는 변환 불가!
 - 띄어쓰기는 무시되는 듯. (float('        0.23') => 0.23)
          
### 문자열
- `input()`으로 입력받으면 문자열로 저장
- 타입변환 후 사용 (처음엔 무조건 str)
- `len(<변수명>)`	-> 글자 수 반환
- 문자열 합치기 : `+` 기호 이용
- `<확인하고자하는 문자(열)> in <변수명>` # 있으면 true 없으면 false
- `<변수명>.find(<찾을 문자열>)` # <찾을 문자열>의 시작위치 반환
- strip 메소드 : 공백 제거 (필요시 검색)
- startswith : 시작 문자열 찾기. 필요할까? ex)line.startswith('Hi') #true

#### 문자열 슬라이싱
`변수명[a:b]`을 이용한다.
**범위 : [a,b)** a는 포함 b는 불포함!!!
```python
myString = [Myname is Yujin]
print(myString[0:4])   # Myn 출력. [0] ~ [3]
print(myString[5:])    # [5] ~ 출력
print(myString[:3])    # ~ [2] 출력
print(myString[:])     # 전체출력
```
               
### 들여쓰기
- 들여쓰기 = [Tab] = [Space]*4번
- C++에서 {...} 대신 들여쓰기를 사용함
- 들여쓰기가 제대로 되지 않으면 조건에 해당하는 코드를 실행시키지 않거나 error 발생
         
           
### 조건문(if, else)
```python
if <조건> :             # 콜론(:) 필수!!
elif <조건> :           # else if 역할
else :                  # else
<들여쓰기>실행할 코드    # 들여쓰기 필수!!
```

### 예외처리
```python
try:
    ...<코드>
except:
    <error가 발생하면 실행될 코드>
    print("Error!")
```
	
예시
```python
try:
    fval = float(sval)		# sval이 number인지 체크
except:
    print('Invalid input')		# number이 아니면 에러 띄워줌!
    continue
```
---
### 함수 (function)
#### 선언
```python
def <함수이름>(<파라미터>):
     <함수내용>
     return "Hi"	#[선택]반환값이 있을 때만!
```

#### 호출
```python
<함수이름>(<인자>)
```

#### 예시
```python
def greeting(lang):
    print(lang)
    return 12

greeting("Hello World")    # Hello World 출력
print(greeting("hello"))   #12 출력
```

---
### 반복문
#### for 루프
```python
for 루프
for <변수명> in <리스트>:
	<코드>
```

이런것도 가능하다!
```python
friends = ['Connect', 'Korea', 'NHN']
for friend in friends:
	print('Happy New Year!', friend)

# [출력]
# Happy New Year! Connect
# Happy New Year! Korea
# Happy New Year! NHN

for i in range(1, 4):	# range(1,4) 는 1이상 4미만 !!	range(5) : [0,5)
    print(i)

# [출력]
# 1
# 2
# 3
```
	
---
### 파일
#### 파일 열기
`open(<파일명>, <모드선택>)`
- 파일명 : 문자열, 확장자 포함
- 모드 : 읽기 'r' 쓰기 'w'
- 반환 : handle
	- 파일에 대한 작업을 수행하기 위해 사용됨
	- 다른 방식으로 저장되어 있는 텍스트를 처리하는 표준화된 방식
	- 발생할 수 있는 성능의 문제 방지해줌

- '\n'도 하나의 문자.

#### 파일 읽기
```python
fhand = open("haha.txt")

for line in fhand:
    print(line)      # 한 줄씩 띄워져서 출력됨

inp = fhand.read()     # 파일 전체 읽기
```

#### 파일 이름 입력받기 & 예외처리
```python
fname = input('Enter the file name:  ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()
```

---
### 리스트 (List)
- **컬렉션** : 하나의 변수에 여러 값을 넣는 것이 가능하도록 하는 것
- **리스트** : 컬렉션의 한 종류

사용방법
```python
friend = list()          # 빈 리스트 생성
# friend = [] 로도 생성가능했다.
 
friend.append('Joseph')  # 항목 추가
friend.sort()            #항목 정렬

print('Glenn' in friend)  # in을 활용해 리스트에 'Glenn'이 있는지 확인 --> false 반환
```

#### 특징
- 병합, 슬라이싱 가능 (문자열과 같은 방식)
- dir() 메소드 : 특정 타입에서 사용할 수 있는 메소드의 목록들을 보여줌

#### 문자열과 리스트
`<리스트이름> = <기존문자열>.split()` 하면 <기존문자열>을 띄어쓰기 단위로 나눠서 <리스트이>의 리스트로 만든다. 
(이미 값이 있는 리스트라면 기존의 것은 사라지고 갱신됨)
```python
abc = 'With three words'
stuff = abc.split()
print(stuff)

# ['With', 'three', 'words'] 로 출력됩니다.
```
##### 구분자
- split() 의 기본 구분자는 빈칸.
- split(';') ';'을 구분자로 지정. 구분자는 문자열 가능

~ 추가추가 ~ 
