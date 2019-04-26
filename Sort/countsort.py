#! /usr/bin/env python
#coding=utf-8
'''
 桶排序
 复杂度O(n)
 '''
def countsort( A, d ):  #A待排数组， d位数 如果位置需要先修改一下知道A中最多位数
    for k in range(d):  #k轮排序
        s[ [] for i in range(10) ]  #数字0~9，建10个桶
        '''对于数组中的元素，首先按照最低有效数字进行
           排序，然后由低位向高位进行'''
        for i in A:
            s[ i//(10**k)%10 ].append(i)
        A = [j for i in s for j in i]  #977/10=97(小数舍去),87/100=0
    return A

from random import randint
a = [randint(1,999) for i in range(10)]  #产生10个随机3位数
a = countsort(a,3)
print(a)

[181, 263, 893, 705, 566, 727, 801, 310, 589, 783]  #随机数
[181, 263, 310, 566, 589, 705, 727, 783, 801, 893]  #排序后
