"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbour in node.neighbors:
                copy.neighbors.append(dfs(neighbour))
            return copy
        return dfs(node) if node else None
        

# Helper function to print the graph
def print_graph(node):
    visited = set()
    
    def dfs(node):
        if node not in visited:
            visited.add(node)
            print(f"Node {node.val} -> Neighbors: {[n.val for n in node.neighbors]}")
            for neighbor in node.neighbors:
                dfs(neighbor)
    
    dfs(node)

if __name__ == '__main__':
    obj = Solution()
     # Construct the graph manually
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    # Setting up neighbors
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    cloned_graph = obj.cloneGraph(node1)
    # Print the original and cloned graphs
    print("Original Graph:")
    print_graph(node1)
    
    print("\nCloned Graph:")
    print_graph(cloned_graph)