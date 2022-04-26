def minsubFaster(A):
    n = len(A)
    k = -1
    j = -1
    m = 0
    start = 0
    curMinSum = 0
    for i in range(0, n):
        curMinSum += A[i]
        if curMinSum < m:
            m = curMinSum
            j = start
            k = i
        if curMinSum > 0:
            curMinSum = 0
            start = i + 1
    return (m, j + 1, k + 1)
   
A = [-2, -4, 3, -1, -5, 6, -7, -2, 4, -3, 2]
print("A = ", A)
ret = minsubFaster(A)
print("(m, j, k) = ", ret)

 
        