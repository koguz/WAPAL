# WAPAL: Weighted Adjacency Propagation Algorithm 

This is WAPAL by Kaya Oğuz and Osman Doluca, presented at IISEC 2022, International Informatics and Software Engineering Conference. 

The paper is available at https://ieeexplore.ieee.org/document/9998238. Please cite as

Oğuz K, Doluca O, (2022) "Extending APAL to Detect Overlapping Communities in Weighted Networks," 2022 3rd International Informatics and Software Engineering Conference (IISEC), 2022, pp. 1-4, doi: 10.1109/IISEC56263.2022.9998238

WAPAL is based on APAL. You can access source code at https://github.com/koguz/APAL/ and the APAL paper at https://www.sciencedirect.com/science/article/abs/pii/S0020025521008318 

## Running WAPAL

WAPAL uses its own implementation of the Graph ADT with weights. It is very straightforward to use this Graph class. 

```python
from Graph import *

g = Graph()
# add a vertex, the type can be anything, int, string or any other class
g.add_vertex(1) 
# or a list of vertices
g.add_vertices([1, 2, 3, 4])
# then, add an edge, say between 1 and 3 with a weight of 2.1
g.add_edge(1, 3, 2.1)
```

Once a graph is populated with vertices and weighted edges, you can use it in WAPAL. 

To run WAPAL, create a WAPAL object, assign your graph to it. Then, run `run_wapal(f)` with the fitness value `f`, between 0 and 1. The fitness value is defined as the expected intraconnectivity times expected normalized average of weights. 

```python
from WAPAL import *

wapal = WAPAL()
wapal.graph = g # the graph we have defined above
wapal_clusters = wapal.run_wapal(0.75)
```

The overlapping communities found in Graph `g` will be in the `wapal_clusters` variable. This repository also includes the `CompareClusters` class so that you can compare the result to a ground truth, if you have one. Assuming that the real clusters are in `clusters` variable, use it as follows for normalised mutual information (NMI) metric that is extended for overlapping communities as detailed in 

Andrea Lancichinetti et al 2009 New J. Phys. 11 033015, https://iopscience.iop.org/article/10.1088/1367-2630/11/3/033015

The result has a range of [0,1] where values closer to 1 are of communities that are more alike, therefore represent better results.

```python
from CompareClusters import CompareClusters as CC

cc = CC(g.vertices, clusters, wapal_clusters)
wapal_result = cc.nvi_overlapping()
