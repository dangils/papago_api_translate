import os
import sys
import urllib.request
import json

#코드 모듈화
def trans0(tra):
    client_id = "NdKBto_wCStv_mvA8eez" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "AEzFnD9BMz" # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(tra)
    data = "source=en&target=ko&text=" + encText
    #한국어를 영어로 
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

#json데이터를 딕셔너리로 변환
    if(rescode==200):
        response_body = response.read()
        dic = json.loads(response_body)
        # print(response_body.decode('utf-8'))
        return dic['message']['result']['translatedText']
    else:
        print("Error Code:" + rescode)





