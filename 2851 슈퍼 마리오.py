answer = 0
score = 0

for i in range(10):
    score += int(input())
    if 100 -answer >= abs(100-score):
        answer = score

print(answer)