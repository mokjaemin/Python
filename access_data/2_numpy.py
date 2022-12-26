

from matplotlib.pyplot import axes, axis
import numpy as np
from numpy.core.function_base import linspace
from numpy.lib.arraysetops import setdiff1d

# 리스트 정리 및 연산에 좋은 넘파이
# 엑셀이나, csv 파일 정돈에 아주 좋겠군
# 기본적으로 연산은 각 해당 행열 끼리 연산함.



# input 은 리스트 또는 튜플로 주자
# x = np.array([10,20,30])
# y = x**2
# print(y)



# 1 부터 10 까지
# x = np.arange(10)
# print(x)


# 개수 == a.size
# print(x.shape)



# 차원의 개수
# print(x.ndim)



# 데이터 타입
# print(x.dtype)



# 바이트크기 
# x.itemsize


# n 차원
# 2 차원
# [[], [], []] 형태
# x = np.array([[10,20,30],
#             [40,50,60],
#             [70,80,90]])
# print(x.ndim)


# 3 차원
# x = np.array(
#     [
#         [
#             [10,20,30],
#             [40,50,60],
#             [70,80,90]
#         ]
#     ]
#     )
# print(x.ndim)


# (+) metrix는 2차원, numpy array는 다차원


# insert
# a = np.array([10,20,30])
# a = np.insert(a,0,5) # a라는 리스트의 0번째 자리에 5 삽입



# delete
# a = np.delete(a,0) # a라는 리스트의 0번째 자리 삭제
# print(a)



# 2행 3열의 0으로 채워진 리스트 만들기
# a = np.zeros((2,3))
# print(a)
# 1은 ones



# 연산 함수
# a = np.array([1,2,3])
# b = np.array([1,2,3])
# print(np.add(a,b)) # 더하기
# print(np.subtract(a,b)) # 빼기
# print(np.multiply(a,b)) # 곱하기
# print(np.divide(a,b)) # 나누기
# print(np.divmod(a,b)) # 나눗셈한 값과 나머지
# print(np.exp(a)) # e의 1승, 2승, 3승
# print(np.sqrt(a)) # 제곱근(루트) 계산



# 통계 함수
# a = np.array([10,20,30])
# print(np.mean(a)) # 평균
# print(np.average(a, weights=[1,2,1])) # 가중치를 넣은 평균
# print(np.median(a)) # 중간값
# print(np.cumsum(a)) # 10, 10+20, 10+20+30


# 그외 연산함수
# a = np.array([10,20,30])
# print(a.sum()) # 합
# print(a.min()) # 최솟값
# print(a.argmin()) # 최솟값이 위치한 인덱스
# print(a.max()) # 최댓값
# print(a.argmax()) # 최댓값이 위치한 인덱스
# print(a.ptp()) # 최솟값과 최대값의 차이
# print(a.sort()) # 작은순으로 정리



# sort 예시
# x = np.array([10,20,30,15,14])
# y = np.sort(x)
# idx = np.argsort(x)
# print(x)
# print(y)
# print(idx) # 정돈된 리스트의 원래 위치 인덱스


# searchsorted
# a = np.array([10,20,30])
# b = np.array([-10,15,50])
# print(np.searchsorted(a,b))
# b리스트를 a의 어디 인덱스에 삽입해야 정돈된 리스르로 만들 수 있는지 인덱스 번호를 알려줌


# reshape
a = np.arange(1,7,1) # 1부터 6까지 1씩 증가
b = a.reshape(6,1) # 6행 1열로 모양 변화
print(b)
# a = linspace(1,10,3) # 1부터 10까지 3개로 리스트화
# b = linspace(1,10,10).reshape(2,5)


# repeat 반복
# a = np.array([[1,2],[4,5]])
# b = np.repeat(a,2, axis=0) # axis = 정렬 기준 (가로, 세로) 2는 3차원
# c = np.repeat(a,[1,2]) # 첫번째 줄은 한번 반복 두번째 줄은 두번 반복


# 두 리스트 연결 concatenate
# a = np.array([[1],[2],[3]])
# b = np.array([[1],[2],[3]])
# print(np.concatenate((a,b), axis=0))


# 가로, 세로 방향 연결
# a = np.array([[1],[2],[3]])
# b = np.array([[1],[2],[3]])
# print(np.vstack((a,b))) # 세로방향 연결
# print(np.hstack((a,b))) # 가로방향 연결


# 리스트 자르기
# a = np.array(
#     [
#         [10,20,30],
#         [40,50,60]
#     ]
# )
# print(np.hsplit(a,3)) # 10-40, 20-50, 30- 60으로 나눠서 리스트 자름
# print(np.vsplit(a,2))


# 10-40, 20-50, 30-60으로 만들어줌
# a = np.array([[10,20,30], [40,50,60]])
# print(a.transpose())


# 한줄로 정렬
# print(a.ravel())
# print(a.reshape(-1))
# print(a.ravel(order='C')) # 가로 방향으로 읽어서 한줄 정렬
# print(a.ravel(order='F')) # 세로 방향으로 읽어서 한줄 정렬
# print(a.flatten())


# 차원 줄이기
# a = np.array([[1,2,3]])
# b = a.squeeze()
# print(b)


# 차원 추가
# a = np.array([[1,2,3]])
# b = a[:, np.newaxis]
# print(b)


# copy 할때 아래와 같이 작성시 카피 되지않고 a=b 형태가 됨
# a = np.array([10,20,30])
# b=a
# b[0] = 30
# print(b)
# print(a)


# shallow copy
# 결과는 위와 동일하지만 b의 차원이 변경될 시 a는 변하지 않음
# a = np.array([10,20,30])
# b = a.view()
# b[0] = 30
# print(b)
# print(a)


# deep copy
# b 요소 변경시 a 변경 되지 않음.
# a = np.array([10,20,30])
# b = a.copy()
# b[0] = 99
# print(b)
# print(a)


# logic function
# a = np.array([1,0,2,3])
# a의 모든값이 모두 참인가?(모두 0이 아닌가?)
# print(a.all())

# a의 요소 중 하나라도 참인가?(하나라도 0이 아닌것이 있는가?)
# print(a.any())


# a의 값들 중 0 이 아닌것만 저장
# b=a.nonzero()
# print(b)


# 해당 조건을 만족하는 요소의 인덱스 값을 반환
# print(np.where(a>0))



# 뒤에서 부터 요소값 부르기
# print(a[-1]) # 맨뒤의 값
# print(a[-2]) # 맨뒤에서 두번째 값



# 두개 이상의 요소 불러오기 [[ ]] 활용
# print(a[[1,2]])



# 해당 범위의 요소 불러오기
# print(a[1:3])


# 0부터 3전까지 두번씩 건너뜀
# a = np.array([1,0,2,3,4,5])
# print(a[0:3:2])


# 뒤에서 부터 시작하는데 두번씩 감소하면서 출력
# print(a[::-2])


# 시작하는 점이 끝에서 두번재 자리인데 두번씩 감소
# print(a[-2::-2])


# 2차원 요소 slicing 
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# print(a[0][0])
# print(a[0,0]) # 위와 결과 동일
# print(a[0,:]) # 천번째 가로줄 전체
# print(a[:,0]) # 첫번째 세로줄 전체


# slicing 하면 일차원 출력이 나오는데 2차원출력으로 바꿔줌
# b = a[:,0]
# c = b[:,np.newaxis]
# print(c)


# 모든 가로줄에서 인덱스 0과2
# : 는 모든이라고 생각
# print(a[:,[0,2]])


# 끝에서부터 모든 줄
# print(a[:,::-1])


# 3차원 slicing
# a = np.array(
#     [
#         [
#             [1,2,3,4],
#             [5,6,7,8]
#         ],
#         [
#             [2,2,3,4],
#             [5,6,7,8]
#         ]
#     ]
# )


# 가장 바깥쪽 괄호가 첫번째 요소라고 생각하자.
# print(a[0,0,0])
# print(a[0,:,:])


# idx = np.where(a==1) # 위치 출력
# idx = (a==1) # true or falsse 출력
# print(idx)


# ex 이미지
# Image = np.array([[255,0,255],[255,0,255],[255,0,255]])
# idx = np.where(Image==255)
# Image[idx] = 0
# print(Image)


# linear algebra 선형 대수
# a = np.array([[10,20],[30,40]])
# b = np.array([[1,2],[3,4]])


# 요소끼리의 곱
# print(a*b)


# 행렬 계산
# 1행*1열, 1행*2열...
# print(a@b)
# print(a.dot(b))


# 대각선끼리 더해줌
# a = np.zeros((3,3))
# b = np.ones((3,3))
# print(np.trace(b))


# 함수 계산
# x@z = y
# x = np.array([[1.,-3.],[2.,4.]])
# y = np.array([[1.],[3.]])
# inv_x = np.linalg.inv(x)
# z = inv_x@y
# ==
# z = np.linalg.solve(x,y)
# print(z)


# 고유값 고유벡터
# print(np.linalg.eig(x))

# 특이값 분해
# print(np.linalg.svd(x))



# 활용1
# a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# b = np.array([[1],[2],[3]])
# b = b.repeat(3, axis=1) # axis 1이면 세로
# print(b*a)

# 활용2
# 함수 활용
# def f(x,y):
#     return x*y
# a = np.fromfunction(f, (5,4), dtype=int)
# print(a)


# 활용3
# set를 활용해 두 리스트의 차이를 출력
# a = np.array([10,20,30,40,50])
# b = np.array([20,30,40])
# print(np.setdiff1d(a,b))


# column_stack
# 두 배열을 나란히 붙여줌
# a = np.array([1,2,3,4,5])
# b = np.column_stack((a**2, a))
# print(b)

