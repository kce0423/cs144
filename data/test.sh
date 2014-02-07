#!/bin/bash

cp input.txt input1.txt
((j = 0))
for i in {1..50}
do
    echo "Iteration $i..."
    ((j = i + 1))
    ./pagerank_map.py <input$i.txt | sort | ./pagerank_reduce.py | ./process_map.py | sort | ./process_reduce.py >input$j.txt
    rm input$i.txt    
done
mv input$j.txt output.txt