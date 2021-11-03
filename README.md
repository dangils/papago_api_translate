# papago_api_translate
파파고 api를 이용한 번역기 툴


1) 네이버 개발자 센터에서 파파고 api 어플리케이션 등록
    https://developers.naver.com/main/
    
2)  발급 받은 api의 id 와 pw를 papago.py 에 기입 (무료 버전 : 일일 1만자 번역가능)  
    client_id = "" # 개발자센터에서 발급받은 Client ID 값  
    client_secret = "" # 개발자센터에서 발급받은 Client Secret 값  
    
3) papago.py
    data = "source=en&target=ko&text=" + encText
    #번역할 언어 수정가능 ( en -> ko 번역 중)
