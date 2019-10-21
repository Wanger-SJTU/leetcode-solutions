"""
Definition for a directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: nodes: a array of Directed graph node
    @return: a connected set of a directed graph
    """
    def connectedSet2(self, nodes):
        # write your code here
        res = []
        if not nodes or len(nodes) == 0:
            return res
        record = {}
        for item in nodes:
            record[item.label] = record.get(item.label, item.label)
        
        for node in nodes:
            for neighbor in node.neighbors:
                root_node = self.unionFind(record, node)
                root_neighbor = self.unionFind(record, neighbor)
                if root_node != root_neighbor:
                    record[item] = record[record[item]]
                    
    def unionFind(self, record, item):
        while record[item] != item:
            record[item] = record[record[item]]
            item = record[item]
        return item

class UnionFind:
    def __init__(self):
        pass