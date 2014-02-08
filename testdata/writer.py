
def writeToFile(graph, filename):
    f = open(filename, 'w')
    for node_i, neighbors in graph.iteritems():
        f.write('NodeId:%s\t1.0,0.0' % node_i)
        for node_j in neighbors:
            f.write(',%s' % node_j)
        f.write('\n')
    f.close()
