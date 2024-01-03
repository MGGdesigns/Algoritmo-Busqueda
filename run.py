# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print("----------------------------------------------------------------------------------------------")
print("Busqueda en amplitud:")
result_path = search.breadth_first_graph_search(ab).path()
print("Coste total:", str(result_path[0].path_cost))
print(result_path)
print("----------------------------------------------------------------------------------------------")
print("Busqueda en profundidad:")
result_path = search.depth_first_graph_search(ab).path()
print("Coste total:", str(result_path[0].path_cost))
print(result_path)
print("----------------------------------------------------------------------------------------------")
print("Busqueda en ramificación y acotación:")
result_path = search.branch_and_bound_graph_search(ab).path()
print("Coste total:", str(result_path[0].path_cost))
print(result_path)
print("----------------------------------------------------------------------------------------------")
print("Busqueda en ramificación y acotación subestimada:")
result_path = search.branch_and_bound_subestimated_graph_search(ab).path()
print("Coste total:", str(result_path[0].path_cost))
print(result_path)
print("----------------------------------------------------------------------------------------------")


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
