# 파이썬 정리
파이썬을 공부하며 C++과 다르거나 헷갈리는 개념 위주로 정리하고자 함

### 목록
 1. [기본 (기타)](https://github.com/euzl/py4e/blob/master/basic_note.md#%EA%B8%B0%EB%B3%B8)
 2. [함수](https://github.com/euzl/py4e/blob/master/basic_note.md#%ED%95%A8%EC%88%98-function)
 3. [반복문](https://github.com/euzl/py4e/blob/master/basic_note.md#%EB%B0%98%EB%B3%B5%EB%AC%B8)
 4. [파일](https://github.com/euzl/py4e/blob/master/basic_note.md#%ED%8C%8C%EC%9D%BC)
 5. [리스트](https://github.com/euzl/py4e/blob/master/basic_note.md#%EB%A6%AC%EC%8A%A4%ED%8A%B8-list)  
 6. [딕셔너리](https://github.com/euzl/py4e/blob/master/basic_note.md#%EB%94%95%EC%85%94%EB%84%88%EB%A6%ACdictionary---%EC%97%B0%EA%B4%80-%EB%B0%B0%EC%97%B4-associative-arrays)
---            
## 기본 (기타)
- 주석 : `#`기호사용
- 문장의 끝에 세미콜론(;)을 붙히지 않는다!!
- 논리연산자
	- `&&` 대신 `and` 사용 `||` 대신 `or` 사용
	- `not` 도 있다!
- True/False 로 표기 (첫글자 대문자!)
- `cnt++` <- 사용불가. `cnt += 1` <- 사용가능
- `==`은 값만 비교하지만 /  `is`, `is not`은 자료형과 값 모두 비교
- `print()` 함수사용하면 개행문자('\n') 추가됨
- [최단평가] A or B 이면 A먼저 확인하고 B확인
- string 초기화 할 때 `None` 이용! 숫자는 적절히..? 0이나 -1로..?

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
- startswith : 시작 문자열 찾기. 필요할까? ex)line.startswith('Hi') # true
- split() 메소드 : <문자열>.split() => 띄어쓰기를 기준으로 문장을 단어들의 리스트로 만들어줌

##### 구분자
- split() 의 기본 구분자는 빈칸.
- split(';') ';'을 구분자로 지정. 구분자는 문자열 가능

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
## 함수 (function)
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
## 반복문
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
## 파일
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
## 리스트 (List)
- **컬렉션** : 하나의 변수에 여러 값을 넣는 것이 가능하도록 하는 것
- **리스트** : 순서대로 정리된 컬렉션

사용방법
```python
friend = list()          # 빈 리스트 생성
# friend = [] 로도 생성가능했다.
 
friend.append('Joseph')  # 항목 추가
friend.sort()            #항목 정렬

print('Glenn' in friend)  # in을 활용해 리스트에 'Glenn'이 있는지 확인 --> false 반환


# words.append([a, b, c]) #[a, b, c]그대로 리스트 단위로 들어감..!
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
---
## 딕셔너리(dictionary) - 연관 배열 (Associative Arrays)
- 순서가 없음
- 키(key)가 존재

생성
`store = dict()` 또는 `store = {}`

키(key)에 값(value) 연결
```python
store['money'] = 3     #'money'라는 키에 3이라는 값 연결
store['candy'] = 8

print(store)           #{'money': 3, 'candy': 8} 라고 출력. 항상 순서대로X

print(store['candy'])  #8 출력. candy라는 키에 저장된 값에 접근

store['candy'] = store['candy'] + 2
# 'candy'에 저장된 값이 8+2=10 로 갱신됨. 그냥 store['candy']=5 이렇게 해도 되고 
# store['candy']가 value 그 자체라서 '='도 대입연산자 그대로 사용!!
```
#### get 메소드 (유용한듯)
`<딕셔너리>[key] = <딕셔너리>.get(<key>, <값>)`
- 딕셔너리에 key가 존재할 경우 key에 대한 값을 불러온다.
- 존재하지 않으면 key에 값이 들어간 데이터를 딕셔너리에 추가한다.

(예)
```python
counts = dict()	 # 생성 
names = ['aa', 'bb', 'cc', 'aa']
for name in names :
counts[name] = counts.get(name, 0) + 1
```
#### 루프 적용
```python
counts = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for key in counts:	         # "key값"을 돌게 됨
    print(key, counts[key])
```
#### key나 value를 별도로 저장하려면
1. **키로만 구성된 리스트 만들기** 
	- list(<딕셔너리명>) 또는 <딕셔너리명>keys()
2. **값으로만 구성된 리스트 만들기** 
	- <딕셔너리명>values()
3. **튜플(tuple)에 쌍을 이루어 만든 리스트** 
	- <딕셔너리명>.items() 
	- ex) [('jan', 100), ('chuck', 1), ('fred', 42)]

예시
```python
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}

# 1. 키로만 구성된 리스트
print(list(jjj))             # ['jan', 'chuck', 'fred']
print(jjj.keys())            # ['jan', 'chuck', 'fred']

# 2. 값으로만 구성된 리스트
print(jjj.values())          # [100, 1, 42]

# 3. 튜플에 쌍을 이루어 리스트로 저장
print(jjj.items())           # [('jan', 100), ('chuck', 1), ('fred', 42)]
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for aaa,bbb in jjj.items() : # key, value
    print(aaa, bbb)          # chuck 1 / fred 42 / jan 100
```

### 튜플(Tuple)
- 컬렉션
- 순서 O
- 소괄호`()` 사용
	- cf) 소괄호를 사용하지않아도 파이썬에서는 여러 값을 컴마로 나열하면 튜플로 인식함. 
	- 예) `x, y = 1, 10`
- **변경불가능!** 값을 변경할 수 없다. 
	- => 용량을 적게 먹고 접근속도가 빠름. 정렬 불가능
	- 단, 튜플로 이루어진 리스트는 sorted 가능!
- `(x, y) = (4, 'fred')` 같이 여러변수에 간단하게 값을 넣을 수 있다.
- 여러 값에 대해 비교 가능
	- 가장 왼쪽 값끼리 비교 -> 큰지 작은지 여부(나머지 값 비교 X)
	- 두 값이 같으면 -> 다음 값을 비교

* sorted()함수를 이용하면 정렬한 객체를 반환한다.

### 딕셔너리 정렬 - 튜플이용
1. 딕셔너리에서 items메소드를 실행 : 튜플로 이루어진 리스트 형태로 만듦 (값을 기준으로 정렬하려면 키와 값의 위치를 바꾼 리스트 생성)
2. sorted 함수로 정렬.

키를 기준으로 정렬
```python
d = {'b':1, 'a':10, 'c':22}
for k, v in sorted(d.items()):
    print(k, v)
```
값을 기준으로 정렬
```python
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) ) # 키와 값의 위치를 바꿔서 tmp에 추가!

tmp = sorted(tmp)
print(tmp)
```
내림차순으로 정렬하고 싶다면?
```python
tmp = sorted(tmp, reverse=True) 
#reverse 옵션을 True로 설정
```
#### 리스트 컴프리헨션 (List Comprehension)
- 딕셔너리를 값을 기준으로 정렬해서 출력하는 코드와 동일한 역할
- 아래와 같은 방식으로 리스트를 만드는 방식을 리스트 컴프리헨션이라고 한다.

```python
c = {'a':10, 'b':1, 'c':22}
print( sorted( [ (v,k) for k,v in c.items() ] ) )
# [(1, 'b'), (10, 'a'), (22, 'c')]
```


~ 추가추가 ~ 
