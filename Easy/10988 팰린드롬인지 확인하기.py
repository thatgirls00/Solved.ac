word = list(input())

word_reverse = list(reversed(word))

if word == word_reverse:
    print(1)
else:
    print(0)
