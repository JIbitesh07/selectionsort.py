arr=[54,67,13,21,90,32]
def selectionsort(arr):
    for i in range(len(arr)):
        minidx=i
        for j in range(i+1,len(arr)):
            if arr[minidx]>arr[j]:
                minidx=j
        arr[i],arr[minidx]=arr[minidx],arr[i]


    for i in range(0,len(arr)):
            print(arr[i])
selectionsort(arr)
