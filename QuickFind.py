class QuickFind(object):
    graph=[]
    n=0

    def __init__(self,m):
        x=0
        self.n=m
        while x<self.n:
            self.graph.insert(x,x)
            x=x+1
    def CheckConnection(self,p,q):
        return self.graph[p]==self.graph[q]

    def Unite(self,p,q):
        p_graph=self.graph[p]
        x=0
        while x<self.n:
            if self.graph[x]==p_graph:
                self.graph[x]=self.graph[q]

            x=x+1
                

obj=QuickFind(5)
obj.Unite(0,1)
obj.Unite(2,3)
obj.Unite(3,4)
print(obj.CheckConnection(0,1))
print(obj.CheckConnection(1,2))

