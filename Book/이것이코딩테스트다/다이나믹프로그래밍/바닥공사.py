# 가로길이가 N, 세로길이가 2인 직사각형을
# 1*2/2*1/2*2 크기의 사각형으로 채우고자 할때
# 사각형을 채우는 모든 경우의 수

n = 5
di = [0] *100

di[1] = 1
di[2] = 3
for i in range(3, n+1):
    di[i] = (di[i-1] + 2 * di[i-2])

for i in range(n+1):
    print(d[i], di[i])

# 이전의 값에서 추가 될수있는 값만을 고려한다
