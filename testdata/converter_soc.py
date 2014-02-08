#!/usr/bin/env python

import writer

graph = {}
f = open('soc-Epinions1.txt')
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

writer.writeToFile(graph, 'epinions.txt')
    
