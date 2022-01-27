# ai-bin
깡통 api  
이 프로젝트는 사내에 세팅된 api 를 호출하기 위해 브릿지 역할로 열어두는 깡통 api 입니다.  
파라미터로 정의한 url, param, method 데이터를 가지고 호출하고, 해당 응답을 그대로 반환합니다.

```python
# 아래와 같은 형태로 api 호출
{
    "url": "https://search.naver.com/search.naver", # request 날릴 url
    "param": { # 필요한 파라미터를 dictionary 형태로 정의
        "query": "대한통운 파업"
    },
    "method": "GET" # request method
}
```
