def knapsack(W,v,w):    
    arr =[]
    n = len(v)
    for i in range(W + 1):#initialize array
        arr.append(0);
    for i in range(W + 1):
        for j in range(n):
            if(w[j]<=i):
                arr[i]=max( arr[i], arr[i-w[j]]+v[j])
    #print(arr)
    return arr[W]
 
###########################################
W = 9
v = [3, 4,10]
w = [2,4,5]

print(knapsack(W,v, w))
