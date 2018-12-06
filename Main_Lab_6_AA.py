"""
Alexis Aguirre
CS2302: Lab 6, Option A 
Due on: 12/4/18

"""
from GraphAL import DisjointSetForest, GraphAL

def main():
    
    
    graph_1_edges = []      # Graph for Kruskals
    graph_1_edges.append([0, 1, 15])
    graph_1_edges.append([0, 3, 6])
    graph_1_edges.append([1, 2, 9])
    graph_1_edges.append([1, 3, 12])
    graph_1_edges.append([1, 6, 14])
    graph_1_edges.append([1, 7, 10])
    graph_1_edges.append([2, 4, 16])
    graph_1_edges.append([3, 4, 8])
    graph_1_edges.append([4, 5, 20])
    
    graph_2_edges = []      # Graph for Kruskals
    graph_2_edges.append([0, 1, 5])
    graph_2_edges.append([0, 3, 3])
    graph_2_edges.append([1, 2, 4])
    graph_2_edges.append([2, 3, 1])
    graph_2_edges.append([2, 4, 10])
    graph_2_edges.append([3, 4, 20])
    graph_2_edges.append([4, 5, 6])
    graph_2_edges.append([4, 6, 7])
    graph_2_edges.append([5, 6, 11])
    graph_2_edges.append([5, 7, 9])

    graph_3_edges = []      # Graph for Kruskals
    graph_3_edges.append([0, 1, 4])
    graph_3_edges.append([0, 4, 3])
    graph_3_edges.append([1, 2, 4])
    graph_3_edges.append([1, 4, 2])
    graph_3_edges.append([1, 5, 5])
    graph_3_edges.append([2, 3, 8])
    graph_3_edges.append([2, 5, 6])
    graph_3_edges.append([2, 6, 9])
    graph_3_edges.append([3, 6, 13])
    graph_3_edges.append([3, 9, 20])
    graph_3_edges.append([4, 5, 12])
    graph_3_edges.append([4, 7, 1])
    graph_3_edges.append([5, 6, 17])
    graph_3_edges.append([5, 7, 21])
    graph_3_edges.append([5, 8, 11])
    graph_3_edges.append([6, 8, 10])
    graph_3_edges.append([6, 9, 15])
    graph_3_edges.append([7, 8, 14])
    graph_3_edges.append([8, 9, 16])

    print("Edges in Graphs")

    print(graph_1_edges)        # Checking list was populated correctly
    print()
    print(graph_2_edges)
    print()
    print(graph_3_edges)
    print()

    graph_1 = BuildGraph(graph_1_edges, False, 8)   # Graphs are built, non directed, and with corresponding vertices
    graph_2 = BuildGraph(graph_2_edges, False, 8)
    graph_3 = BuildGraph(graph_3_edges, False, 10)
        
    min_span_1 = KruskalsImplementation(graph_1, graph_1_edges)     # Min span using Kruskals
    min_span_2 = KruskalsImplementation(graph_2, graph_2_edges)
    min_span_3 = KruskalsImplementation(graph_3, graph_3_edges)
    
    print("Resulting Minimum Spanning Trees")

    print(min_span_1)       # Min Spans outputted
    print()
    print(min_span_2)
    print()
    print(min_span_3)
    print()
    
### TOPOLOGICAL SORT NOT COMPLETE
#    graph_4_edges = []
#    graph_4_edges.append([0, 1, 1])
#    graph_4_edges.append([0, 2, 1])
#    graph_4_edges.append([1, 5, 1])
#    graph_4_edges.append([2, 3, 1])
#    graph_4_edges.append([3, 5, 1])
#    graph_4_edges.append([4, 5, 1])
#    graph_4_edges.append([4, 6, 1])
#    graph_4_edges.append([5, 6, 1])
#    
#    graph_5_edges = []
#    graph_5_edges.append([0, 1, 1])
#    graph_5_edges.append([0, 4, 1])
#    graph_5_edges.append([1, 2, 1])
#    graph_5_edges.append([1, 5, 1])
#    graph_5_edges.append([2, 3, 1])
#    graph_5_edges.append([2, 6, 1])
#    graph_5_edges.append([4, 1, 1])   
#    graph_5_edges.append([4, 5, 1])
#    graph_5_edges.append([4, 7, 1])
#    graph_5_edges.append([5, 2, 1])
#    graph_5_edges.append([5, 6, 1])
#    graph_5_edges.append([5, 8, 1])
#    graph_5_edges.append([6, 3, 1])
#    graph_5_edges.append([7, 5, 1])
#    graph_5_edges.append([7, 8, 1])
#    graph_5_edges.append([8, 6, 1])
#    
#    print(graph_4_edges)
#    print()
#    print(graph_5_edges)
#    print()
#
#    graph_4 = BuildGraph(graph_4_edges, True, 7)
#    graph_5 = BuildGraph(graph_5_edges, True, 9)
#    
#    top_4 = TopologicalSortImplementation(graph_4, graph_4_edges)
#    top_5 = TopologicalSortImplementation(graph_5, graph_5_edges)
#
#    print(top_4)
#    print()
#    print(top_5)
#    print()

    
def KruskalsImplementation(graph, edges):
    edge_list = edges
    vertex_sets = DisjointSetForest(len(edges))
    result_list = []
    
    while vertex_sets.get_num_of_sets() > 1 and len(edge_list) > 0:     # While all vertices are not on one set and you still have vertices to check
        next_edge = edge_list[0]    # Next edge and index of edge are saved
        next_edge_ind = 0
        for i in range(len(edge_list)):     # For loop gets edge with smallest weight
            if edge_list[i][2] < next_edge[2]:
                next_edge = edge_list[i]
                next_edge_ind = i
        del edge_list[next_edge_ind]    # Lightest edge is delted from remaining unchecked edges
        if vertex_sets.find(next_edge[0]) != vertex_sets.find(next_edge[1]):    # Checks of vertices are already in same set
            result_list.append(next_edge)   # Valid edge added, and sets are combined
            vertex_sets.union(vertex_sets.find(next_edge[0]), vertex_sets.find(next_edge[1]))
    
    return result_list
    
    
def BuildGraph(edges, directed, vertices):  # Edges list, directed or not directed, and number of vertices
    graph = GraphAL(vertices, directed)     # Initialize empty graph with only vertices
    for i in range(len(edges)):     # Adds edges to graph
        graph.add_edge(edges[i][0], edges[i][1], edges[i][2])
    return graph

### TOPOLOGICAL SORT NOT COMPLETE
#def TopologicalSortImplementation(graph, edges):
#    result_list = []
#    no_incoming_vertices = []
#    for i in range(graph.get_num_vertices()):
#        if len(graph.get_vertices_that_point_to(i)) == 0:
#            no_incoming_vertices.append(i)
#    remaining_edges = graph
#    while no_incoming_vertices:
#        current_vertex = no_incoming_vertices.pop(0)
#        result_list.append(current_vertex)
#        outgoing_edges = graph.get_vertices_reachable_from(current_vertex)
#        while outgoing_edges:
#            graph.remove_edge(current_vertex, outgoing_edges.pop())
#        for j in range(len(outgoing_edges)):
#            in_vertices = graph.get_vertices_that_point_to(current_vertex)
#            in_count = len(in_vertices)
#            if in_count == 0:
#                no_incoming_vertices.append(outgoing_edges[j][1])
#    print(result_list)
#    print(no_incoming_vertices)
#    return result_list

main()

















        