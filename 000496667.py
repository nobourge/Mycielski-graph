# INFO-F103 - Algorithmique - Exercice côté 3
#
# Prénom : Noe
# Nom : Bourgeois
# Matricule : 000496667

# N'oubliez pas de modifier le nom du fichier 000496667.py en VotreMatricule.py


from graphs import DynamicUndirectedGraph


def mycielski(n):
    """
    Calcule le nème graphe de Mycielski.

    Args:
        n (int): entier naturel >= 0

    Returns:
        DynamicUndirectedGraph: M_n
    """
    vertices_nb = 3 * (2 ** n) - 1
    M_n = DynamicUndirectedGraph(vertices_nb)

    M_n.link(0, 1)

    linked_nb = 2

    origin_neighbours = [set() for i in range(vertices_nb)]
    origin_neighbours[0].add(1)
    origin_neighbours[1].add(0)

    while linked_nb < vertices_nb:
        duplicated_nb = linked_nb * 2
        blue_pill_idx = duplicated_nb


        for i in range(linked_nb,
                       duplicated_nb):
            origin = i - linked_nb
            for neighbour in origin_neighbours[origin]:
                M_n.link(i,
                         neighbour)
            M_n.link(i,
                     blue_pill_idx)
        linked_nb = duplicated_nb + 1

        for origin_vertice in range(linked_nb):
            for neighbour in M_n.vertex(origin_vertice).neighbours:
                origin_neighbours[origin_vertice].add(neighbour.idx)

    return M_n


####### Tests ########

def max_deg(G):
    return max(map(lambda v: v.nb_neighbours,
                   (G.vertex(i) for i in range(G.n))))


if __name__ == '__main__':

    Vk = 2
    Ek = 1
    max_deg_k = 1

    for k in range(5):
        Mk = mycielski(k)
        assert Mk.n == Vk and Mk.m == Ek and max_deg(Mk) == max_deg_k
        max_deg_k = Vk
        Ek *= 3
        Ek += Vk
        Vk *= 2
        Vk += 1
