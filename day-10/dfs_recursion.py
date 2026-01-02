def dfs(graph,node,visited=None):
    if visited is None:
        visited=set()
    visited.add(node)
    print(node,end=" ")
    
    for neighbours in graph[node]:
        if neighbours not in visited:
            dfs(graph,neighbours,visited)
            
graph={
    '1':['2','3'],
    '2':['4','5'],
    '3':['6','7'],
    '4':[],
    '5':[],
    '6':[],
    '7':[]
}
dfs(graph,'1')