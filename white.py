def minsubFaster(B):
    n = len(B)
    k = -1
    j = -1
    m = 0
    start = 0
    curMinSum = 0
    for i in range(0, n):
        curMinSum += B[i]
        if curMinSum < m:
            m = curMinSum
            j = start
            k = i
        if curMinSum > 0:
            curMinSum = 0
            start = i + 1
    return (m, j + 1, k + 1)
   
B = [-2, -4, -3, -1, 5, -6, -7, 2, -4, -3, -2]
print("B = ", B)
ret = minsubFaster(B)
print("(m, j, k) = ", ret)
