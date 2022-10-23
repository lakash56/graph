#adjency list
graph={
    '1' : ['2'],
    '2' : ['7','4',],
    '3' : ['4'],
    '4' : ['6'],
    '5' : ['4','3'],
    '6' : [],
    '7' : ['5']
}
def bfs (graph,s):
    visited =set()
    
    queue = set() # list in python is a queue
    visited.append(s) #make it black
    queue.append(s)
    
    while queue: #as long as queue is non empty
        u= queue.pop() #pop the first index from the queue
        print(u, '-->',end=" ")
        for neighbor in graph[u]: #for every emelement that is connected with u
            if neighbor not in visited:
                visited.add(neighbor) #add them to visited
                queue.add(neighbor)      #add them to queue

               
bfs(graph,'1')
