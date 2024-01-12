# a0.py

# Starter code for assignment 0 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Audrey Chen
# audrelc1@uci.edu
# 20284228


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
