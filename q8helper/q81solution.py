from performance import Performance
from goody import irange
from graph_goody import random_graph, spanning_tree

# Put script below to generate data for Problem #1
# In case you fail, the data appears in sample8.pdf in the helper folder


def create_random(size):
    global num
    num = random_graph(size, lambda n: 10*n)


if __name__ == '__main__':
    size = 1000
    while size <= 128000:
        p = Performance(lambda: spanning_tree(num), lambda: create_random(size), 5, '\nSpanning Tree of size ' + str(size))
        p.evaluate()
        p.analyze()
        size = 2 * size