import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# 디스플레이 옵션 설정
pd.set_option('display.width', 320)
pd.set_option('display.max_columns', 20)


# xlsx 파일 불러와서 dataframe 으로 저장
df_covid = pd.read_excel('./access_data/corona_data.xlsx')
# print(df_covid)


# 날짜, 확진자 데이터 추출
df_date = df_covid[['DATE', 'CONFIRM', 'DEATH']]
# df_date.index = df_date['DATE']
df_date = df_date.drop(['DATE'], axis=1)
confirm = df_date['CONFIRM']
# print(confirm)


# 일일 확진자
df_date['confirm_per_day'] = np.zeros((418,1))
for i in range(0, 417):
    df_date['confirm_per_day'][i] = confirm[i] - confirm[i+1]
df_date['confirm_per_day'][417] = 0
day_confirm = df_date['confirm_per_day']



# 사망률 구하기
df_date['DEATH RATE'] = 100*df_date['DEATH']/df_date['CONFIRM']
# print(df_date)

day = np.arange(0,418)

# plt.plot(df_date.index, confirm) # 가로, 세로
plt.plot(day, day_confirm) # 가로, 세로
plt.tick_params(size=5, labelsize=11) # 가로 세로 축 글자의 크기
plt.xlabel('DATE', fontsize=14)
plt.title('CONFIRM PER DATE', fontsize=14)
plt.grid(alpha=0.3) # alpha = 투명도
# plt.show()




# 예측 모델
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures # 특성을 새로 만들거나 데이터 전처리를 위한 도구 제공
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler # 표준점수를 위한 도구
from sklearn.linear_model import Ridge # 릿지
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso


day = np.arange(0,418)
day_confirm = day_confirm.to_numpy()
day = day.reshape(-1,1)


train_input, test_input, train_target, test_target = train_test_split(
    day, day_confirm, random_state=42
)



pf = PolynomialFeatures(degree=20,include_bias=False)
pf.fit(train_input)
train_poly = pf.transform(train_input)
test_poly = pf.transform(test_input)


ss = StandardScaler()
ss.fit(train_poly)
train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)


lr = LinearRegression()
lr.fit(train_scaled, train_target)
# print(lr.score(train_scaled, train_target))
# print(lr.score(test_scaled, test_target))
a = np.array([1000])
a = a.reshape(-1,1)
print(lr.predict(ss.transform(pf.transform(a))))