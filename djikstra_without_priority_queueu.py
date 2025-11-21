import math
graph_1 = {}
graph_1["start"] = {
    "A":5,
    "B":2
}
graph_1["A"]= {
    "D":2,
    "C":4
}
graph_1["B"]={
    "A":8,
    "D":7
}
graph_1["C"]={
    "finish":3,
    "D":6
}
graph_1["D"]={
    "finish":1
}
graph_1["finish"]={}

def find_cheapest_node(node_costs, processeds):
    cheapest_node_cost = math.inf
    cheapest_node = None
    if not node_costs:
        print("dict of node's cost must no be empty")
        return
    for node in node_costs:
        cost = node_costs[node]
        if cost < cheapest_node_cost and node not in processeds:
            cheapest_node_cost = cost
            cheapest_node = node
    return cheapest_node


def cheapest_path(graph, source_node):
    if source_node not in graph.keys():
        print(f"node called '{source_node}' dont exist on graph")
        return []
    costs = {}
    for node in graph:
        if node == source_node:
            costs[source_node] = 0
        else:
            costs[node] = math.inf
    parents = {}
    processed = set()
    node_to_process = find_cheapest_node(costs, processeds=processed)
    while node_to_process:
        child_nodes = graph[node_to_process]
        for child_node in child_nodes:
            new_cost = costs[node_to_process] + graph[node_to_process][child_node]
            if new_cost < costs[child_node]:
                costs[child_node] = new_cost
                parents[child_node] = node_to_process
        processed.add(node_to_process)
        node_to_process = find_cheapest_node(costs, processeds=processed)
    return [costs,parents]

graph_1_result = cheapest_path(graph_1,"start")

def describe_path(costs_node_result, parent_node_result, node_source, final_node=None):
    result_dict = {}
    for node_x in costs_node_result:
        result_dict[node_x] = {}
        result_dict[node_x]["cost"] = costs_node_result[node_x]
        path = []
        if node_x != node_source:
            if costs_node_result[node_x] != math.inf:
                neighbor = parent_node_result.get(node_x)
                while neighbor:
                    path.insert(0,neighbor)
                    new_neighbor = parent_node_result.get(neighbor)
                    neighbor = new_neighbor
                path.append(node_x)
            else:
                path=[]
        else:
            path.append(node_x) 
        result_dict[node_x]["path"] = path
    final_result = result_dict
    if final_node:
        final_result = result_dict[final_node]
    return final_result 

print(describe_path(graph_1_result[0],graph_1_result[1],"start","finish"))

                