# 정규 표현식(Regular Expressions)
정규 표현식이란 특정한 규칙을 가친 문자열의 집합을 표현하는데 사용하는 형식 언어이다.

# 정규 표현식의 필요성
정규 표현식의 필요성은 다음과 같은 상황에서 알 수 있다.

    ○ 회원가입과 같은 input 폼이 있는 웹페이지를 만들 때 형식이 맞게 작성되었는지 확인할 때

    ○ 소스코드에서 단어를 조건에 맞게 치환하려고 할 때

    ○ 특정 텍스트가 포함된 파일을 걸러낼 때

이 밖에 많은 상황들이 있지만 생략하겠다.

상황들을 보아 알 수 있는 것은 정보를 찾거나, 찾아서 치환할 때 쓰인다는 것이다.

정규 표현식 없이 문제를 해결하려 한다면 해결은 할 수 있겠으나, 많은 노력이 필요할 것이다.

하지만 정규 표현식이 이를 간단하게 할 것이다.

# 파이썬에서의 정규 표현식 기본 사용법

<b>파이썬에서 정규 표현식을 지원하는 re모듈</b>

파이썬은 정규 표현식을 지원하기 위해 re(regular expression의 약어) 모듈을 제공한다. 

re 모듈은 파이썬을 설치할 때 자동으로 설치되는 표준 라이브러리로 사용 방법은 다음과 같다.

        >>> import re
        >>> p = re.compile('ab*')

<b>메타 문자</b>

정규 표현식에서 메타문자에는 다음과 같은 것들이 있다.

    . ^ $ * + ? { } [ ] | \ ( )
    
<b>Dot(.)</b>

정규 표현식의 Dot(.) 메타 문자는 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨을 의미한다.

예시

    정규 표현식이 a.b일 때, 문자열 "aab", "a0b", "abc"가 어떻게 매치 되는지 보자.
    "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치된다.
    "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치된다.
    "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는있어야 하는 이 정규식과 일치하지 않으므로 매치되지 않는다.

<b>^</b>

^ 메타 문자는 문자열의 맨 처음과 일치함을 의미한다.

예시

    정규 표현식이 ^Life일 때, 'Life is too short'와 'My Life'가 어떻게 매치 되는지 보자.
    'Life is too short'는 'Life'가 맨 처음에 오므로 Life가 매치된다.
    'My Life'는 'My'가 맨 처음에 오므로 매치되지 않는다.

<b>$</b>

$ 메타 문자는 ^ 메타 문자와 반대의 경우이다. 즉 $는 문자열의 끝과 매치함을 의미한다.

예시

    정규 표현식이 short$일 때, 'Life is too short'와 'Life is too short, you need python'이 어떻게 매치 되는지 보자.
    'Life is too short'는 'short'가 맨 마지막에 오므로 short가 매치된다.
    'Life is too short, you need python'은 'python'이 맨 마지막에 오므로 매치되지 않는다.
    
<b>반복(*)</b>

정규 표현식의 * 메타 문자는 * 바로 앞에 있는 문자가 0부터 무한대로 반복될 수 있다는 의미이다.

예시

    정규 표현식이 ca*t일 때, 문자열 "ct", "cat", "caaat"가 어떻게 매치 되는지 보자.
    "ct"는 "a"가 0번 반복되어 매치된다.
    "cat"는 "a"가 1번 반복되어 매치된다.
    "caaat"는 "a"가 3번 반복되어 매치된다.

<b>반복(+)</b>

정규 표현식의 + 메타 문자는 + 바로 앞에 있는 문자가 최소 1번이상 반복될 수 있다는 의미이다.

예시

    정규 표현식이 ca+t일 때, 문자열 "ct", "cat", "caaat"가 어떻게 매치 되는지 보자.
    "ct"는 "a"가 0번 반복되어 매치되지 않는다.
    "cat"는 "a"가 1번 반복되어 매치된다.
    "caaat"는 "a"가 3번 반복되어 매치된다.

<b>?</b>

? 메타 문자는 ?앞에 있는 문자가 0번 혹은 1번 사용될 경우 매치된다.

예시
  
    ab?c 정규 표현식이 있을 때, "abc", "ac"가 어떻게 매치 되는지 보자.
    "abc"는 b가 1번 사용되어 매치된다.
    "ac"는 b가 0번 사용되어 매치된다.
    
<b>{ }</b>

{ } 메타 문자는 반복을 의미한다. A{3}은 A가 3번 반복되는 문자열과 일치한다.

<b>문자 클래스 [ ] </b>

문자 클래스로 만들어진 정규 표현식은 "[ ] 사이의 문자들과 매치" 라는 의미를 갖는다.

예시

    정규 표현식이 [acd]일 때, 문자열 "after", "bread", "use"가 어떻게 매치 되는지 보자.
    "after"는 정규 표현식과 일치하는 문자인 "a"가 있으므로 매치
    "bread"는 정규 표현식과 일치하는 문자인 "d"가 있으므로 매치
    "use"는 정규 표현식과 일치하는 문자가 없으므로 매치되지 않음
    
[ ] 안의 두 문자 사이에 -(하이픈)을 사용하면 범위를 의미하게 된다

예를 들어 [0-5]라는 정규 표현식은 [012345]와 동일하다.

<b>|</b>

| 메타 문자는 or과 동일한 의미로 사용된다 A|B라는 정규 표현식이 있다면 A 또는 B라는 의미가 된다.

예시

    Crow|Servo가 정규 표현식일 때, 문자열 'CrowHello'와 일치하는 것은 'Crow'뿐이다.
    
<b>( )</b>

( ) 메타 문자는 그룹을 만들어 주는 문자이다.

<h1>자주 사용하는 문자 클래스</h1>

\d - 숫자와 매치, [0-9]와 동일한 표현식이다.

\D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.

\s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.

\S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.

\w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.

\W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.

대문자로 사용된 것은 소문자의 반대임을 추측할 수 있다.

<h1>정규 표현식에 사용되는 메서드</h1>

match()	문자열의 처음부터 정규식과 매치되는지 조사한다.

search()	문자열 전체를 검색하여 정규식과 매치되는지 조사한다.

findall()	정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다.

finditer()	정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 리턴한다.

<b>match 객체의 메서드</b>

group()	매치된 문자열을 리턴한다.

start()	매치된 문자열의 시작 위치를 리턴한다.

end()	매치된 문자열의 끝 위치를 리턴한다.

span()	매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴한다.

# Example questions

<code>
    import re
</code>
    <b>기본</b>
<code>    
    text = 'abc'
    regex = re.compile('[d]')
    matchobj = regex.match(text)
    print(matchobj)
</code>
    <b>기본2</b>
<code>
    text = 'bed'
    regex = re.compile('[a-c]')
    matchobj = regex.match(text)
    print(matchobj)
</code>
    <b>문자열 대체</b>
<code>
    text = 'My Life is too short'
    replace = 'leg'
    regex = re.compile(r'^Life')
    result = re.sub(regex, replace, text)
    print(result)
</code>
    <b>전화번호 발췌</b>
<code>
    text = '우리집 전화번호는 031-397-7319 입니다.'
    regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    matchobj = regex.search(text)
    tellnum = matchobj.group()
    print(tellnum)
</code>


자료 출처 : https://wikidocs.net/4308#mn
