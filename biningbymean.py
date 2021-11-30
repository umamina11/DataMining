def meanSmoothing(arr1, m):   
    a = len(arr1)
    n = int(a / m)
    for i in range(0, m):
        arr = []
        arr2=[]
        for j in range(i * n, (i + 1) * n):
            if j > a:
                break
            arr = arr + [arr1[j]]
        print("equal frequency binning", arr)
        size=len(arr)
        mean=int(sum(arr)/size)
        for i in range(0,size):
            arr[i]=mean
        print("Smoothing by mean",arr)
                
n=int(input("Enter the no. of data you want to add: "))
data=[]
for i in range(0,n):
    ele=int(input())
    data.append(ele)
print("Data before sorting: " ,data)
data.sort()
print("Data after sorting: ",data)
bn=int(input("Enter the number of bins according to the size of data so that data can be divided equally: "))
meanSmoothing(data, bn)