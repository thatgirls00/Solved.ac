while True:
    a, b, c = map(int, input().split())
    if a == 0 or b == 0 or c == 0:
        break

    a *= a
    b *= b
    c *= c
    if a+b == c or b+c == a or a+c == b:
        print("right")
    else:
        print("wrong")