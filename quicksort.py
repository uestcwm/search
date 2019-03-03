'''
快排
用了分治思想：
基线条件；
递归条件
'''
def quicksort(array):
    if len(array) < 2:
        return array   #基线条件：为空或只包含一个元素
    else:
        pivot = array[0]  #将第一个元素作为基准值
        less = [i for i in array[1:] if i <= pivot]   #小于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]   #大于基准值的元素组成的子数组
        return quicksort(less) + [pivot] + quicksort(greater)  

