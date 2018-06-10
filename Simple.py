#Laixian Wan
#wanlx@bu.edu
#CS591 C1 Spring 2018

def main():
    '''
    main;
    here I demostrate a simple example of graph containing 3 nodes.
    the relationship between nodes are:
     1--2
      \ |
       \|
        3
    1 -> 2, 1 -> 3 and 2 -> 3. 3 is terminal position.
    
    To modify this test case, go to edges.txt and nodes.txt.
    '''
    graph = input_process('nodes.txt', 'edges.txt')
    graph = g_calculator(graph)
    print('for the following graph: ')
    print(graph)
    print()
    for k, v in graph.items():
        print('for node ' + str(k))
        print('g-value: ' + str(v[1]))
        print()
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

def g_calculator(graph):
    '''
    accepts an uncomputed graph and returns g-value for each node.
    '''
    for res in graph:
        graph[res][1] = g_value(graph[res], graph)
        
    return graph

def g_value(node_info, graph):
    '''
    calculates the g-value for a single node in a given graph using recursion.
    '''
    followers = node_info[0]
    gVal = node_info[1]
    if gVal != -1: #g_value has already been computed!
        return gVal
    elif followers == []: #base case!
        return 0
    else:
        temp = []
        for follower in followers:  #find out all the follower in the graph
            temp.append([follower, graph[str(follower)]])
        return mex([g_value(node[1], graph) for node in temp]) 
        
