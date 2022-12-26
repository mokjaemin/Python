import numpy as np
import matplotlib.pyplot as plt

# x = np.array([10,20,30])
# y = np.array([1,2,10])
# plt.plot(x,y, 'r') 
# 선색이 빨간색 'b' 는 파랑
# plt.show()


# plt.plot(x,y, 'b--') # 점선 
# plt.show()


# plt.plot(x,y, 'bo') # 동그라미 표현
# plt.show()


# 라벨 추가
# plt.plot(x,y, 'b', label='Data')
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.legend() # label = 'Data' 추가
# plt.show()


# 여러줄 표현
# x = np.linspace(0,2,100)
# y1 = 0.5*x # 0.5x
# y2 = 0.5*x**2 # 0.5 x의 제곱
# y3 = 0.5*x**3 # 0.5 x의 세제곱
# plt.plot(x,y1, label = '1')
# plt.plot(x,y2,label = '2')
# plt.plot(x,y3,label = '3')
# plt.legend()
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('Graphs')
# plt.show()


# 위와 동일한 결과를 출력하는 oop 스타일
# 객체화를 하여 변경사항이 생길 시 용이하게 사용
# hf, ha = plt.subplots()
# hp1, = ha.plot(x,y1)
# hp2, = ha.plot(x,y2)
# hp3, = ha.plot(x,y3)
# ha.set_xlabel('x')
# ha.set_ylabel('y')
# ha.set_title('Graph')
# hp1.set_label('1')
# hp2.set_label('2')
# hp3.set_label('3')
# ha.legend()
# hp1.set_color('r')
# hp2.set_color('g')
# hp3.set_color('b')
# ha.grid() # 점선 추가
# plt.show()


# decay sin example
# t = np.linspace(0,100,1000)
# tau = 10
# y = np.sin(t)*np.exp(-t/tau)
# plt.plot(t,y)
# plt.ylabel('meter')
# plt.ylabel('second')
# plt.show()

# 오일러 공식
# t = np.linspace(0,1,100)
# f = 1  # frequency
# y_euler = np.exp(1j*2*np.pi*f*t)
# y_cos = np.real(y_euler) # 실수부분
# y_sin = np.imag(y_euler) # 허수부분
# hfig, hax = plt.subplots()
# hax.plot(t, y_cos, '-r',label='cos')
# hax.plot(t, y_sin, '--b',label='sin')
# hax.grid()
# hax.legend()
# plt.show()


# 그래프 나눠주기
# hfig, hax = plt.subplots(2,1)
# hax[0].plot(t, y_cos, '-r',label='cos')
# hax[1].plot(t, y_sin, '--b',label='sin')
# hax[0].grid()
# hax[0].legend()
# hax[1].grid()
# hax[1].legend()
# plt.show()


# histogram
# data = np.random.randn(10000)
# plt.hist(data, 100, density=True) # 숫자 - 막대개수, density - 확률 밀도 그래프
# # plt.show()


# 정규 분포 그래프
# x = np.linspace(-4,4,100)
# sigma = 1
# mean = 0
# nd = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-mean)/sigma)**2)
# # sqrt - 루트
# plt.plot(x,nd,'r')
# plt.show()

# 3D plot
# x = np.linspace(0, 2*np.pi, 20)
# y = np.linspace(0, 2*np.pi, 20)
# grid_x, grid_y = np.meshgrid(x,y) # 2차원 격자를 만들어줌
# z = np.sin(grid_x)*np.sin(grid_y)
# hfig = plt.figure()
# hax = hfig.gca(projection='3d') # 3d 만들기
# hax.plot_surface(grid_x, grid_y, z, cmap='jet') # cmap='jet' - 위로 갈수록 빨간색으로 아래로 갈수록 파란색으로 표현
# hax.set_xlabel('x')
# hax.set_ylabel('y')
# hax.set_zlabel('z')
# plt.show()


# animation
# 여기서는 잘안되고 주피터로 하면 되는거 같음
# fig, ax = plt.subplots()
# x = np.array([1,2,3,4,5])
# y = np.array([1,1,1,1,1])

# hp, = ax.plot(x,y)
# ax.set_ybound([0,11]) # y축 고정

# for i in range(0,10,1):
#     hp.set_ydata(i*y)
#     plt.pause(0.5)
# plt.show()