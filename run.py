# Search methods

import search

ab = search.GPSProblem('O', 'E'
                       , search.romania)

print("----------------------------------------------------------------------------------------------")
print("Busqueda en amplitud:")
print(search.breadth_first_graph_search(ab).path())
print("----------------------------------------------------------------------------------------------")
print("Busqueda en profundidad:")
print(search.depth_first_graph_search(ab).path())
print("----------------------------------------------------------------------------------------------")
print("Busqueda en ramificación y acotación:")
print(search.branch_and_bound_graph_search(ab).path())
print("----------------------------------------------------------------------------------------------")
print("Busqueda en ramificación y acotación subestimada:")
print(search.branch_and_bound_subestimated_graph_search(ab).path())
print("----------------------------------------------------------------------------------------------")

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
