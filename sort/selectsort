'''
选择排序，速度不是很快
'''
def findsmallest(arr):  #返回最小元素的下标
    smallest = arr[0]  #存储最小的值
    smallest_index = 0   #存储最小元素的索引
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index  

def selectionsort(arr):
    newarr = []   #空列表用来存储排序后的
    for i in range(len(arr)):
        smallest = findsmallest(arr)  #此时smallest是下标
        newarr.append(arr.pop(smallest))   #pop(下标)将下标元素删除
    return newarr  

selectionsort([5,3,6,2,9])
