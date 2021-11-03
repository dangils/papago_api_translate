from papago import trans0

import pandas as pd
#판다스로 엑셀 파일 읽기
'''
1)
pip install pandas
pip install openyxl
2)
판다스로 엑셀 파일 읽기
3)
읽은 데이터를 함수에 넣음
'''
data = pd.read_excel('english.xlsx', engine='openpyxl')

for n,row in data.iterrows():
    #n:행번호, row:행내용
    #iterrows(): 판다스에 있는 가로줄 하나씩 번역(리스트 형태)

    data.loc[n,'korean'] = trans0(row['english'])
    #data.loc -> 데이터 수정하는 함수 .loc[행,열]

print(data)

data.to_excel('output.xlsx')
data.to_csv('ddd.csv')
