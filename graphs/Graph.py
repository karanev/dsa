import Vertex

class Graph:
    def __init__ (self):
        self.numVertices  = 0
        self.verticesList = {}
    
    def addVertex (self, key):
        vertex                  = Vertex.Vertex (key)
        self.verticesList [key] = vertex
        self.numVertices       += 1
        return vertex
    
    def getVertex (self, n):
        if n not in self.verticesList:
            return None
        else:
            return self.verticesList [n]
    
    def getVertices (self):
        return self.verticesList.keys ()
    
    def __contains__ (self, n):
        return n in self.verticesList
    
    def addEdge (self, f, t, weight = 0):
        if f not in self.verticesList:
            self.addVertex (f)
        if t not in self.verticesList:
            self.addVertex (t)
        self.verticesList[f].addNeighbour (self.verticesList[t], weight)
    
    def __iter__(self):
        return iter(self.verticesList.values())