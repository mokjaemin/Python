import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures # 특성을 새로 만들거나 데이터 전처리를 위한 도구 제공
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler # 표준점수를 위한 도구
from sklearn.linear_model import Ridge # 릿지
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso

df = pd.read_csv('./personal_thing/samsung.csv')

df_date = df[['Date', 'Open']]
df_date.index = df_date['Date']
open = df_date['Open']
a = np.arange(249).reshape(-1,1)


plt.plot(a, open) # 가로, 세로
plt.tick_params(size=5, labelsize=11) # 가로 세로 축 글자의 크기
plt.xlabel('DATE', fontsize=14)
plt.title('OPEN', fontsize=14)
plt.show()

train_input, test_input, train_target, test_target = train_test_split(a, open, random_state=42)


poly = PolynomialFeatures(degree=5 ,include_bias=False)
poly.fit(a)
train_poly = poly.transform(train_input)

# train_poly 가 만들어진 방식 알기
# print(poly.get_feature_names())

# test도 적용
test_poly = poly.transform(test_input)


lr = LinearRegression()
lr.fit(train_poly, train_target)
# print(lr.score(train_poly, train_target))
# print(lr.score(test_poly, test_target))


# 표준점수를 통한 데이터 전처리
ss = StandardScaler()
ss.fit(train_poly)
# 표준점수로 변환됨
train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)

# alpha 변수를 통해 계수를 줄이는 양 조절
# 적절한 alpha 값 찾아보기
train_score = []
test_score = []

alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
for alpha in alpha_list:
    ridge = Ridge(alpha=alpha)
    ridge.fit(train_scaled, train_target)
    train_score.append(ridge.score(train_scaled, train_target))
    test_score.append(ridge.score(test_scaled, test_target))


# 그래프를 통해 확인
# 로그 함수를 통해 x축의 간격을 일정하게 맞춰줌
plt.plot(np.log10(alpha_list), train_score)
plt.plot(np.log10(alpha_list), test_score)
plt.xlabel('alpha')
plt.ylabel('socre')
plt.show()

ridge = Ridge(alpha=10**-3)
ridge.fit(train_scaled, train_target)
print(ridge.score(train_scaled, train_target))
print(ridge.score(test_scaled, test_target))

