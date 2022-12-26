import pandas as pd

data = pd.read_excel('./personal_thing/son_data.xlsx')

data_input = data[['home','away','left','center','right','big6','weak']].to_numpy()
data_target = data['goal'].to_numpy()
# print(data_input)

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(
    data_input, data_target, random_state=42
)

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(max_depth=4, random_state=42)
dt.fit(train_input, train_target)
# print(dt.score(train_input, train_target))
# print(dt.score(test_input, test_target))

# print(dt.predict([[0,1,1,0,0,0,1]]))

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=5, include_bias=False)
poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

dt.fit(train_poly, train_target)
print(dt.score(train_poly, train_target))
print(dt.score(test_poly, test_target))