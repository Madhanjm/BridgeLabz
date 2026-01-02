def dfs(graph,start):
    visited=set()
    stack=[start]
    visited.add(start)
    
    while stack:
        node = stack.pop()
            
        print(node,end=" ")
        
        for neighour in reversed(graph[node]):
            if neighour not in visited:
                visited.add(neighour)
                stack.append(neighour)
                    
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