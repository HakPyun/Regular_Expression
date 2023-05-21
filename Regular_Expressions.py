import re

#기본
text = 'abc'
regex = re.compile('[d]')
matchobj = regex.match(text)
print(matchobj)

#기본2
text = 'bed'
regex = re.compile('[a-c]')
matchobj = regex.match(text)
print(matchobj)

#문자열 대체
text = 'Life is too short'
replace = 'leg'
regex = re.compile(r'^Life')
result = re.sub(regex, replace, text)
print(result)

#전화번호 발췌
text = '우리집 전화번호는 031-397-7319 입니다.'
regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchobj = regex.search(text)
tellnum = matchobj.group()
print(tellnum)