# 파이썬 정리(C++과의 차이점을 중점으로)
파이썬을 공부하며 C++과 다르거나 헷갈리는 개념 위주로 정리하고자 함
            
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
        
          
### 입력 및 출력

    name = input()     # 값을 입력받을 수 있다. -- 문자열로 받음
    print(name)        # name에 저장된 값 출력
    
    name = input('What your name?')   # What your name? 이라고 물어보면 입력할 수 있다.
    print('Hi ', name)                # Hi 라는 문자열과 함께 출력

     
           
### 타입 변환 및 확인
    i = 42
    type(i)      # int 반환
    j = 1.5
    type(j)      # float
    j = int(j)   # int 형으로 바뀜
    type(j)      # int 반환
    print(j)     # '1' 출력

 - type(<변수명>) -> 타입 반환 
 - float(<변수명>) -> 타입 변환 // float, int 등.  단, 변환이 될 때만! str에서 int 는 변환 불가!
          
### 문자열
- input()으로 입력받으면 문자열로 저장
- 타입변환 후 사용
- len(<변수명>)	-> 글자 수 반환
               
### 들여쓰기
- 들여쓰기 = [Tab] = [Space]*4번
- C++에서 {...} 대신 들여쓰기를 사용함
- 들여쓰기가 제대로 되지 않으면 조건에 해당하는 코드를 실행시키지 않거나 error 발생
         
           
### 조건문(if, else)
    if <조건> :             # 콜론(:) 필수!!
    elif <조건> :           # else if 역할
    else :                  # else
    <들여쓰기>실행할 코드    # 들여쓰기 필수!!

### 예외처리
	try:
	    ...<코드>
	except:
	    <error가 발생하면 실행될 코드>
	    print("Error!")
	
예시

    try:
        fval = float(sval)		# sval이 number인지 체크
    except:
        print('Invalid input')		# number이 아니면 에러 띄워줌!
        continue


---
### 함수 (function)
#### 선언

    def <함수이름>(<파라미터>):
	     <함수내용>
	     return "Hi"	#[선택]반환값이 있을 때만!


#### 호출
    <함수이름>(<인자>)

#### 예시
    def greeting(lang):
    	print(lang)
    	return 12
    
    greeting("Hello World")    # Hello World 출력
    print(greeting("hello"))   #12 출력

---
### 반복문
#### for 루프
    for 루프
    for <변수명> in <리스트>:
    	<코드>

이런것도 가능하다!

    friends = ['Connect', 'Korea', 'NHN']
    for friend in friends:
    	print('Happy New Year!', friend)
    
    # [출력]
    # Happy New Year! Connect
    # Happy New Year! Korea
    # Happy New Year! NHN
    
    for i in range(1, 4):	# range(1,4) 는 1이상 4미만 !!
    	print(i)
    
    # [출력}
    # 1
    # 2
    # 3

	




~ 추가추가 ~ 
