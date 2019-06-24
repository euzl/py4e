# 연습문제 6.5
text = "X-DSPAM-Confidence:    0.8475" # 주어진 숫자만 추출할 문장
tnum = text[text.find(':')+1:] # ':' 다음 문자열부터 자른다.

output = float(tnum.strip()) # 공백제거
print(output)
