def binary_search(list,item): #二分查找
    low=0
    high=len(list)-1

    while low <= high:
        mid = (low+high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
     return None
