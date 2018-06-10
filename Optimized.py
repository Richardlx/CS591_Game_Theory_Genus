#Laixian Wan
#wanlx@bu.edu
#CS591 C1 Spring 2018

import functools

def main():
    '''
    Run to solve a more general problem.
	Optimaized by init. a list memorizing previous results to aviod duplicate calculation.
    '''
    graph = input_process('Vertices.txt', 'DirectedEdges.txt')
    graph = g_calculator(graph)
    for k, v in graph.items():
        print('for position ' + str(k))
        print('g-value: ' + str(v[1]))
        print()
    temp = []
    for k, v in graph.items():
        temp.append((int(k), v[1]))
    print('Here is a sorted group of tuples showing the positions and corresponding g-value.')
    temp.sort(key=lambda tup:tup[0])
    print(temp)
    print('We can see the pattern of g-function here.')
    print('g(x) = 0 if x = 0')
    print('g(x) = x if (x mod 4 = 1 or 2)')
    print('g(x) = x + 1 if (x mod 4 = 3)')
    print('g(x) = x - 1 if (x mod 4 = 0) except the case that x = 0')
        
    return 

def input_process(node_file, edge_file):
    '''
    processes two text files which store info about node id and edges, and returns a dictionary representation of the graph in the following format:
    {'node_id':[[follower1, follower2, ... , followerN], g-value init. to -1]}
    '''
    nodefile = open(node_file, 'r')
    nodes = []
    while True:
        node_id = nodefile.readline()
        if node_id != "":
            nodes.append(node_id[:-1]) #drop off the '\n' char!
        else:
            break
    graph = {} #init. graph
    nodefile.close()
    for node_id in nodes:
        graph[node_id] = [[], -1]


    edgefile = open(edge_file, 'r')
    edges = []
    while True:
        edge = edgefile.readline()
        if edge != "":
            edges.append(edge.split())
        else:
            break
    edgefile.close()
    for source_dest in edges:
        graph[source_dest[0]][0] = graph[source_dest[0]][0] + [source_dest[1]]

    return graph

def mex(num_list):
    '''
    returns the smallest non-negative integer not in num_list.
    '''
    i = 0
    while i in num_list:
        i += 1
    return i

def NimSum(num1, num2):
    '''
    returns the nim-sum of num1 and num2.
    '''
    return num1 ^ num2

def g_calculator(graph):
    '''
    accepts an uncomputed graph and returns g-value for each node.
    '''
    for res in graph:
        graph[res][1] = g_value(res, graph[res], graph)
        
    return graph

def g_value(res, node_info, graph):
    '''
    calculates the g-value for a single node in a given graph using recursion.
    '''
    res = int(res)
    followers = node_info[0]
    gVal = node_info[1]
    if gVal != -1: #g_value has already been computed!
        return gVal
    elif followers == []: #base case!
        return 0
    else:
        i = 1
        gVal_Nim = []
        while i <= res // 2: #all cases that pile is split into to two smaller pile!
            j = res - i
            x1 = g_value(i, graph[str(i)], graph)
            graph[str(i)][1] = x1 #actually shouldn't update here but just to make sure the code don't break the memory
            x2 = g_value(j, graph[str(j)], graph)
            graph[str(j)][1] = x2 #same. correct this part later if time is available!
            gVal_Nim.append(NimSum(x1, x2))
            i += 1
        temp = []
        for follower in followers:  #find out all the follower in the graph
            temp.append([follower, graph[str(follower)]])
        return mex([g_value(node[0], node[1], graph) for node in temp] + gVal_Nim) 
        
