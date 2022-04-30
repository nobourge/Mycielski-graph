class Vertex:
    """
    Sommet d'un graphe
    """

    def __init__(self, vertex_idx):
        self.idx_ = vertex_idx
        self.neighbours_ = []

    def add_edge(self, v):
        self.neighbours_.append(v)

    @property
    def idx(self):
        return self.idx_

    @property
    def neighbours(self):
        return iter(self.neighbours_)

    @property
    def nb_neighbours(self):
        return len(self.neighbours_)


class DynamicUndirectedGraph:
    """
    Graphe
    """

    def __init__(self, n):
        self.vertices_ = [Vertex(i) for i in range(n)]
        self.nb_edges_ = 0

    @property
    def n(self):
        """
        Nombre de sommets
        """
        return len(self.vertices_)

    @property
    def m(self):
        """
        Nombre d'arêtes
        """
        return self.nb_edges_

    def add_vertex(self):
        """
        Ajoute un nouveau sommet au graphe
        """
        self.vertices_.append(Vertex(self.n))

    def vertex(self, i):
        """
        Récupère le ième sommet
        """
        return self.vertices_[i]

    def link(self, i, j):
        """
        Crée une arête non-dirigée entre les sommets i et j
        """
        self.vertex(i).add_edge(self.vertex(j))
        self.vertex(j).add_edge(self.vertex(i))
        self.nb_edges_ += 1
