n = int(input())

for i in range(n):
    word = list(input())
    # list는 입력받은 문자열을 문자들의 리스트로 변환
    # str은 input()과 같이 문자열 그대로  반환
    # list는 문자열을 문자 리스트로 변환하여 더 많은 문자 단위 조작 가능

    print(word[0] + word[-1])
