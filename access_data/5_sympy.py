from mpmath.functions.functions import im
from sympy import symbols
from sympy import diff
from sympy import sin
from sympy import integrate
from sympy import limit, Function, Eq, dsolve
import numpy as np


# x = symbols('x')
# x에 관한 미분 적분 등 계산


# differentiation 미분

# 기본 미분
# f = x**3
# dif1 = diff(f,x) # 1차미분 f라는 함수를 x에 관하여 미분
# print(dif1)
# dif2 = diff(dif1, x) # 2차 미분
# print(dif2)
# dif3 = diff(dif2, x) # 3차 미분
# print(dif3)


# sin 함수
# f = sin(x)
# df1 = diff(f, x)
# print(df1)


# integrate 적분
# print(integrate(f, (x, 0, np.pi)))


# limit
# y = limit(f/x, x, 0) # limit x가 0으로 갈때 f의 값
# print(y)


# 상미분 방정식
# t = symbols('t')
# x = Function('x')
# ode = Eq(x(t).diff(t,t) + x(t))
# print(dsolve(ode, x(t)))