#Classe Vertex: Onde é montado nossos Vertices
class Vertex:
    #__init__ = Inicialzação das arestas setando o id e o vertice adjacente
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
    #__str__ = Retorna uma string mostrando os nós e arestas
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    #add_neighbor = O nó do grafo recebe um novo vizinho de peso 0
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    #get_connections = retorna as chaves das arestas
    def get_connections(self):
        return self.adjacent.keys()  
    #get_id = retorna o id do nó
    def get_id(self):
        return self.id
    #get_weight = retorna o peso da aresta
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

#Classe Graph = classe na qual é montado nosso grafo
class Graph:
    
    # __init__ = inicialização do vertice e o numero de vertices
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
    
    # __iter__ = função para iterar os valores dos vertices
    def __iter__(self):
        return iter(self.vert_dict.values())
    
    # add_vertex = se adciona um novo vertice no grafo com as ligações já existentes
    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    #get_vertex = retorna (se existir) um nó do vertice
    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    #add_edge = adciona uma nova aresta no grafo
    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
    # get_vertices = retorna todos os vertices do grafo
    def get_vertices(self):
        return self.vert_dict.keys()

if __name__ == '__main__':
    '''
    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)
    print(g.get_vertices())

    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

    print('--------------------------')
    for v in g:
        print ('VERTICE[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))
'''