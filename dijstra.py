'''dijstra算法：有向，加权，无环'''
#1：实现图
graph = {}
graph['start'] = {}  #初始化
graph['start']['a'] = 6  #起点终点权值
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}  #终点没有任何邻居

#2:开销表
infinity = float('inf')  #python无穷大的表示
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

#3存储父节点
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

#4记录处理过的节点
processed = []

#5找出代价最低的节点
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')  #定义无穷大
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

#6实现狄克斯特拉算法
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost+neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
