import sys

N = int(sys.stdin.readline())
stack = []
start = 1
operator = []

for _ in range(N):
    end = int(sys.stdin.readline())
    while start <= end:  # 시작지점부터 입력받은 지점까지
        stack.append(start)  # 스택에 1씩 저장
        operator.append('+')
        start += 1

    if stack[-1] == end:  # 만약 스택 마지막 항이 end랑 같을 경우
        stack.pop()  # 마지막 부분 꺼냄
        operator.append('-')

    else:  # end랑 다를 경우
        print("NO")
        break

else:
    for i in operator:
        print(i)
