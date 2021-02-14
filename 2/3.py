def main():
    arr=[1,2,3,4,4,5]
    target = 5
    pairs(arr, target)

'''
def find_pairs(target, arr, index):
    if target==1:
        return True
    if index == 0 or target < 1:
        return False

    returnval1=0
    returnval2=0
    if(find_pairs(target/arr[index], arr, index-1)):
        returnval1 =1
    if(find_pairs(target, arr, index-1)):
        returnval2 =1
    
    return returnval1 or returnval2
'''
def pairs(arr,target):
    sorted(arr)
    i=0
    j=len(arr)-1
    returnval = False
    while i<j:
        if arr[i]*arr[j] == target:
            print("("+str(arr[i]) + "," +str(arr[j])+")" )
        if arr[i]*arr[j] < target:
            i+=1
        else:
            j-=1
    
    return returnval



main()
