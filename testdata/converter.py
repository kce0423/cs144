#!/usr/bin/env python

import writer


def converter(input_filename, output_filename):
    graph = {}
    f = open(input_filename)
    for line in f:
        if line.startswith('#'):
            continue
        v, w = line.strip().split('\t')
        if graph.get(v) is None:
            graph[v] = []
        if graph.get(w) is None:
            graph[w] = []
        graph[v].append(w)
    f.close()
    writer.writeToFile(graph, output_filename)


converter('soc-Epinions1.txt', 'data_Epinion')
converter('web-BerkStan.txt', 'data_BerkStan')
converter('web-Google.txt', 'data_Google')
converter('web-NotreDame.txt', 'data_NotreDame')
converter('web-Stanford.txt', 'data_Stanford')
    
