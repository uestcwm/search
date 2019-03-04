'''BFS:广度优先搜索'''
#eg:查看朋友网络谁是芒果经销商

from collections import deque  #导入双端队列函数

#第一：散列表实现图
graph = {}
graph['you'] = ['alice','bob','claire']
graph['bob'] = ['anuj','peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom','jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

#第二判断一个人是否芒果经销商:实际采用别的方式这里简略看最后字符
def person_is_seller(name):
    return name[-1] == 'm'

#第三广度优先搜索过程
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = [] #记录检查过的人
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person+' is a mango seller!')
                return True
            else:
                search_queue += graph[person] #将这个人的盆友假如搜索队列
                searched.append(person)  #标记为检查过
    return False
 
#检验算法
search('you')
