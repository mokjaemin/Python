import numpy as np
from numpy.core.fromnumeric import partition
import pandas as pd
import matplotlib.pyplot as plt




# data = {'name' :['s1','s2','s3'],
#         'age': [25, 28, 22],
#         'score' : np.array([95,80,75])
#         }

# df = pd.DataFrame(data, index=['row1', 'row2','row3'])
# print(df)

# data = [['s1',25,95],
#         ['s2',28,80],
#         ['s3',22,75]]
# df = pd.DataFrame(data, index=['row1','row2','row3'], columns=['name','age','score'])
# print(df)





# 자료추출

# subset
# print(df['score'])
# print(df[['name','score']])
# print(df.loc['row1']) # 가로줄 뽑기
# print(df.loc[['row1', 'row2']])
# print(df.loc['row1', 'name']) # 가로, 세로 둘다 조건 부여
# print(df.loc[:,'name'])
# print(df.loc[:,['name', 'score']])


#iloc
# print(df.iloc[0,0]) # 위치를 통해 출력
# print(df.iloc[:,[0,2]])
# print(df.iloc[::2, [0,2]])
# print(df.iloc[-1,:])


#head
# print(df.head(2)) # 첫번째 두줄

#tail
# print(df.tail(1)) # 마지막 줄





# summurizing data

# df.info() # 정보 출력
# print(df.describe()) # 통계 정보 출력
# print(df.nunique()) # 열에 속한 요소 중 서로 비슷한 타입의 개수
# print(df['score'].value_counts()) # 특정 값에 해당하는 요소의 개수
# print(df['score'].count()) # 데이터의 개수
# print(df['score'].sum()) # 합계
# print(df['score'].max()) # 최고점
# print(df['score'].std()) # standard deviation, 표준편차




# col exchange 칼럼의 위치 바꾸기
# df = df.iloc[:,[0,2,1]] # 2와 1의 자리를 바꿈
# print(df)





# 논리 연산
data = {
    'class' : ['a','b','c','a','b','c','c'],
    'name' : ['s1','s2','s3','s4','s5','s6','s7'],
    'age' : [20,19,21,22,23,24,25],
    'score' : [90,80,75,70,95,90,80]
}

df = pd.DataFrame(data)
# print(df.loc[df['score']>=80]) # 80 점 이상인 인덱스만 뽑아옴
# print(df.loc[df['score']>=80, 'name']) # 80 점 이상인 인덱스의 이름만 뽑아옴
# print(df.loc[df['score']>=80, ['name', 'age']]) # 이름과 나이도 출력



df['result'] = 'none' # 새로운 열 추가
df.loc[df['score']>=80, 'result'] = 'pass' # 80점을 넘은 사람들의 result를 pass로 변경
df.loc[df['score']<80, 'result'] = 'fail' # 80점 이하의 사람들의 result를 fail로 변경
# print(df)


idx = df['result']=='pass' # result 가 pass 인 사람만 추출
# print(df.loc[idx].sort_values('score')) # 낮은 점수 순으로 분류
# print(df.loc[idx].sort_values('score', ascending=False)) # 높은 점수 순으로 분류


# 엑셀로 저장
# df_sorted = df.loc[idx].sort_values('score', ascending=False)
# df_sorted.to_excel('df_sorted.xlsx', index=False)

# csv로 저장
# df.to_csv('df.text', sep='\t', index=False) # 탭으로 분류해서 저장 스페이스는 '\ '

# pickle로 저장
# df.to_pickle('df.pkl')


# 엑셀 불러오기
# df_import = pd.read_excel('df_sorted.xlsx')
# print(df_import)

# csv 불러오기
# df_import = pd.read_csv('df_sorted.txt', delimeter='\t') # delimeter = csv피일이 무엇으로 구분 되었는지










# grouping
# print(df.groupby(by='class').mean()) # 클래스의 따른 분류와 평균 출력
# print(df.groupby(by='class').count()) # 클래스의 따른 분류와 개수 출력
# print(df.groupby(by='class').std()) # 클래스의 따른 분류와 표준편차 출력




# pandas plotting
# df.plot.bar('name', 'score')
# plt.show()
# df.plot.bar('name', ['score','age'])
# plt.show()




# handling missing data
df.loc[[0,2], 'score'] =np.NaN
# print(df.isnull()) # 널이면 트루 반환
# print(df.dropna()) # 널이면 버리고 나머지 출력
# value = 0
# print(df.fillna(value)) # 데이터가 없는 곳에 원하는값 대입
# print(df.replace(np.nan, -1)) # 해당 데이터를 다른 데이터로 대체
# print(df.interpolate()) # 널이면 위아래의 값의 평균으로 채워줌



# Function
# def add_one(a):
#     return a+1

# # print(df['age'].apply(add_one)) # 위에서 만든 함수를 바로 요소에 적용
# print(df['score'].apply(np.square)) # np 함수활용하여 적용



# regulat esxpression 정규 표현식
# 필터에 용이하다
# print(df.filter(regex='[nr]')) # n,r이 들어간 칼럼만 출력


# 데이터 프레임 합치기
# df_vertical = pd.concat([df,df]) # 두개의 프레임 위아래로 합침
# print(df_vertical)
df_horizontal = pd.concat([df,df],axis=1) # 두개의 프레임 양 옆으로 합침
print(df_horizontal)