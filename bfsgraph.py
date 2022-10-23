from pickle import TRUE
class Graph:
  
            #0 1 2 3 4 5 6
    gra= [  [0,1,0,0,1,0,0], #0
            [1,0,1,0,1,0,0], #1
            [0,1,1,0,0,0,0], #2
            [0,0,1,0,1,1,1], #3
            [1,1,0,1,0,0,0], #4
            [0,0,0,1,0,0,0], #5
            [0,0,0,1,0,0,0]  #6
            ]
    for i,node in enumerate(gra):
        print("Node " +str(i)+ "is connected to folling node")
        for index,edge in enumerate(node):
            if edge ==1:
                print(index)
    
    g =[]
    
    def __init__(self,v,e): 
        self.v= v #object
        self.e= e #object
        #print('in init')
        
        Graph.g = [[0 for i in range(v)]
                      for j in range(v)]
    def addEdges(self, s, e):
        Graph.g[s][e]=1
        Graph.g[e][s]=1
    def bfs(self,s):
        
        visited=[False]*self.v
        queue=[s]
        visited[s] = TRUE
        
        while queue:
            u=queue[0]
            queue.pop(0)
            print (u,'-->', end = ' ')
            for i in range(self.v):
                if(Graph.g[u][i] == 1 and (not visited[i])):
                    queue.append(i)
                    visited[i] = True



v, e = 7, 6
 
# Create the graph


gr = Graph(v,e)
gr.addEdges(0, 1)
gr.addEdges(0, 4)
gr.addEdges(1, 2)
gr.addEdges(4, 3)
gr.addEdges(3, 6)
gr.addEdges(3, 5)

gr.bfs(0)

