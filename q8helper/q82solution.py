import cProfile
from graph_goody import random_graph, spanning_tree
import pstats
import random

# Put script below to generate data for Problem #2
# In case you fail, the data appears in sample8.pdf in the helper folder
num = random_graph(15000, lambda n: 10*n)

cProfile.run('spanning_tree(num)', 'profile15K')
p = pstats.Stats('profile15K')
p.sort_stats('ncalls').print_stats(10)
p.sort_stats('tottime').print_stats(10)
