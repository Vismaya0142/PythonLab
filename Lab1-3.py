n = 5
alph = 65
for i in range(0, n):
    print(" " * (n-i), end=" ")
    for j in range(0, i+1):
        print(chr(alph), end=" ")
        alph += 1
    alph = 65
    print()
    

print()
def half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print("")

n = 5
half_pyramid(n)
