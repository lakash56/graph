class Graph:

    g=[]
    def __init__(self,v,e):
        self.v=v
        self.e=e
        Graph.g= [[0 for i in range(v)]
                  for j in range(v)]
        
    def addEdges(self, s, e):
        Graph.g[s][e] =1
        Graph.g[e][s] =1
            
    def dfs(self,s,visited):
        print(s,'-->', end = ' ')
        visited[s] = True
            
        for i in range(self.v):
            if(Graph.g[s][i] == 1 and 
               (not visited[i])):
                self.dfs(i,visited)
                    
v, e = 7, 6
 
# Create the graph


gr = Graph(v,e)
gr.addEdges(0, 1)
gr.addEdges(0, 4)
gr.addEdges(1, 2)
gr.addEdges(4, 3)
gr.addEdges(3, 6)
gr.addEdges(3, 5)

visited =[False]*v
gr.dfs(0,visited)