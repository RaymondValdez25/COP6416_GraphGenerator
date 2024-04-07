import sys
sys.path.append(".")
from pq.priority_queue_bmh import BinaryMinHeap
from pq.priority_queue_ll import LinkedList
class Prims:
    def __init__(self, adjMatrix, heap=None):
        self.adjMatrix = adjMatrix
        # self.PQ = BinaryMinHeap()
        if heap is None:
            self.PQ = BinaryMinHeap()
        else:
            self.PQ = LinkedList()
        self.path = []

    def runAlgo(self):
        self.PQ.insert(((0, 0), 0), 0)
        visited = set()

        while not self.PQ.is_empty():
            currRecord = self.PQ.delete_min()
            (src, dest), priority = currRecord
            if dest in visited:
                continue

            visited.add(src)
            visited.add(dest)

            self.path.append((src, dest))
            curreNeighbors = self.getNeighbors(dest)
            self.addNeighborsToPQ(curreNeighbors)

            #print("current path", self.path)
            #print("priority queue", self.PQ.__str__())

        return self.path[1:]

    def getNeighbors(self, node):
        outList = []

        for column in range(len(self.adjMatrix[node])):
            currentValue = self.adjMatrix[node][column]
            if currentValue != 0:
                key = (node, column)
                outList.append((key, currentValue))

        return outList

    def addNeighborsToPQ(self, listOfNeighbors):
        for item in listOfNeighbors:
            node, priority = item
            self.PQ.insert(node, priority)

def main():

    """Examples / Testers"""
    # create a matrix and an instance of the Prims class 
    adj_matrix = [[0, 2, 0, 6, 0],
                [2, 0, 3, 8, 5],
                [0, 3, 0, 0, 7],
                [6, 8, 0, 0, 9],
                [0, 5, 7, 9, 0]]

    #prims = Prims(adj_matrix)
    prims = Prims(adj_matrix, LinkedList)

    min_spanning_tree_path = prims.runAlgo()

    # Print the minimum spanning tree path
    #print("Minimum Spanning Tree Path:")
    #for edge in min_spanning_tree_path:
        #print(edge)
    
if __name__ == '__main__':
    main()