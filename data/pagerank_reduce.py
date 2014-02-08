#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

graph = {}

for line in sys.stdin:
    key_part, value_part = line.strip().split('\t')
    
    if key_part == '#':
        sys.stdout.write(line)
    else:
        node_i = key_part
        value_list = value_part.split(',')
        node_j = value_list[0]
        rank = float(value_list[1])
        if graph.get(node_i) is None:
            graph[node_i] = {'rank': 0, 'neighbors': []}
        graph[node_i]['rank'] += rank
        graph[node_i]['neighbors'].append(node_j)

for node_i, value in graph.iteritems():
    outline = '%s\t%f' % (node_i, value['rank'])
    sys.stdout.write(outline)
    for node_j in value['neighbors']:
        sys.stdout.write(',%s' % node_j)
    sys.stdout.write('\n')

