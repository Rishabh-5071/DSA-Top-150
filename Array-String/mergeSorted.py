def merge(num1, num2, m, n):
    x, y = m - 1, n - 1

    for z in range(m + n - 1, -1, -1):
        if x < 0:
            num1[z] = num2[y]
            y -= 1
        elif y < 0:
            break
        elif num1[x] > num2[y]:
            num1[z] = num1[x]
            x -= 1
        else:
            num1[z] = num2[y]
            y -= 1

    return num1

num1 = [1, 4, 6, 0, 0, 0]
m = 3

num2 = [1, 3, 9]
n = 3

print(merge(num1, num2, m, n))
