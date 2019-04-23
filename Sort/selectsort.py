'''
选择排序，速度不是很快
O(n^2)
'''
def selectsort(seq):
    for fillslot in range(len(seq)-1,0,-1):
        pos = 0
        for loc in range(1,fillslot):
            if seq[loc] > seq[pos]:
                pos = loc
        seq[pos], seq[fillslot] = seq[fillslot], seq[pos]
    return seq

selectsort([5,3,6,2,9])
