def calculationSum(A):
    arr = []
    for i in range(len(A[-1])):#length of last row
        arr.append(A[-1][i])#assigning bottom row
    #print(arr)
    for i in range(len(A) - 2, -1, -1):
        for j in range(len(A[i])):
            arr[j] = A[i][j] + min(arr[j], arr[j+1])
            #print(arr)
    return arr[0]

#############################################
A = [[2],[5,4],[1,4,7],[8,6,9,6]]

print(calculationSum(A))
