n = 5

left = 1
right = n * (n + 1)

for i in range(n):
    # leading spaces
    print(" " * i, end="")

    count = n - i

    # left side
    for j in range(count):
        print(left, end="*")
        left += 1

    # collect right side numbers
    temp = []
    for j in range(count):
        temp.append(right)
        right -= 1

    # print right side in correct order
    for j in range(len(temp)-1, -1, -1):
        print(temp[j], end="")
        if j != 0:
            print("*", end="")

    print()
