n = int(input())

for x in range(n):
    if x == 0:
        print(x * "  ", end='')
        print("+-+")
        print(x* "  ", end='')
        print("| |")
        print(x * "  ", end='')
        print("+-+", end='')
    elif x == n - 1:
        print("-+")
        print(x * "  ", end='')
        print("| |")
        print(x * "  ", end='')
        print("+-+")
    else:
        print("-+")
        print(x* "  ", end='')
        print("| |")
        print(x * "  ", end='')
        print("+-+", end='')