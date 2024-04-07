"""Implements the A* heuristic variation of Dijkstra's shortest path algorithm using a binary min heap (default) or linked list."""
import sys
sys.path.append(".")
import math
from pq.priority_queue_bmh import BinaryMinHeap
from pq.priority_queue_ll import LinkedList

class AStar:

    def __init__(self,  adjMatrix, heap=None):
        
        self.adjMatrix = adjMatrix

        # decide which priority queue to use
        if heap is None:
            self.PQ = BinaryMinHeap()
        else:
            self.PQ = LinkedList()
        self.path = []

    def euclideanDistance(self, nodeA, nodeB, adjMatrix):
        """Heuristic used in this implementation: Euclidean distance (straight-line distance) between two nodes."""

        # get the coordinates of nodeA and nodeB from the adjacency matrix
        a = adjMatrix[nodeA]
        b = adjMatrix[nodeB]

        # count how many nodes we have
        numNodes = len(adjMatrix)

        sum = 0

        # iterate through each coordinate 
        for i in range(numNodes):
            
            # calculate the difference between coordinates (e.g. x2 - x1)
            value = adjMatrix[nodeB][i] - adjMatrix[nodeA][i]

            # square it
            value = value * value

            # add the value to the sum
            sum += value
        
        # square root the sum to get the distance
        dist = math.sqrt(sum)

        return dist

    def runAlgo(self, start=None, goal=None):

        # count how many nodes we have
        numNodes = len(self.adjMatrix)

        # auto-populate start and goal nodes if they weren't input
        if start is None:
            start = 0

        if goal is None:
            goal = numNodes - 1

        # calculate start node total cost using cost to self + heuristic
        total_cost = 0 + self.euclideanDistance(start, goal, self.adjMatrix)

        # insert the first node into the priority queue as a key-value pair: ( (node, path list), total_cost )
            # key is a tuple: (node, path list)
            # value is the total cost
        self.PQ.insert((start, [start]), total_cost)

        # create a set of nodes already visited
        visited = set()

        # loop until the queue is empty, or the goal is reached
        while not self.PQ.is_empty():

            # pop the node with the lowest total cost (cost + euclideanDistance) from the queue
            node_path, cost = self.PQ.delete_min()

            # parse out the node and path tuple
            node, path = node_path

            # check if the node is the goal
            if node == goal:

                #print("\nRunning A* algorithm with start node " + str(start) + " and goal node " + str(goal) + ".")
                #print("The shortest path is: " + str(path))
                
                return path

            # check if the node was already visited; if so, skip the node
            if node in visited:
                continue

            # mark the node as visited
            visited.add(node)

            # loop through the neighbors of the node
            for neighbor in range(numNodes):

                # check if there's an edge from node to neighbor
                if self.adjMatrix[node][neighbor] > 0:

                    # calculate the cost of reaching the neighbor
                    neighbor_cost = cost + self.adjMatrix[node][neighbor]

                    # calculate the Euclidean distance to the neighbor
                    neighbor_euc = self.euclideanDistance(neighbor, goal, self.adjMatrix)

                    # append the neighbor to the path
                    neighbor_path = path + [neighbor]

                    # calculate neighbor total cost: cost + Euclidean distance heuristic
                    neighbor_total_cost = neighbor_cost + neighbor_euc

                    # push (neighbor, path) and total_cost to the queue
                    self.PQ.insert((neighbor, neighbor_path), neighbor_total_cost)

def main():
    """Examples / Testers"""

    # Example 1: fully connected (actual shortest path is direct). Graph is from homework quiz with cities.
    astar = AStar(([0, 196, 670, 355, 461],
                [196, 0, 479, 164, 270],
                [670, 479, 0, 350, 228],
                [355, 164, 350, 0, 163],
                [461, 270, 228, 163, 0])) 

    shortest_path = astar.runAlgo()

    # Example 2: sparsely conected (actual shortest path is 0, 1, 6). 
    # Link to graph, subtract 1 from each node due to index starting at 0: https://ds055uzetaobb.cloudfront.net/brioche/uploads/CFxGshOrnl-graph1.png?width=1200
    astar = AStar(([0, 3, 0, 0, 0, 12, 0],
        [3, 0, 5, 0, 0, 0, 4],
        [0, 5, 0, 6, 0, 0, 3],
        [0, 0, 6, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 10, 7],
        [12, 0, 0, 0, 10, 0, 2],
        [0, 4, 3, 0, 7, 2, 0]))

    shortest_path = astar.runAlgo()

    # Example 3: very simple (actual shortest path is 0, 1, 3)
    astar = AStar(([0, 1, 3, 0],
                [1, 0, 0, 1],
                [3, 0, 0, 1],
                [0, 1, 1, 0]))

    shortest_path = astar.runAlgo()

    # Example 4: very simple (actual shortest path is 0, 2, 3)
    astar = AStar(([0, 3, 1, 0],
                [3, 0, 0, 1],
                [1, 0, 0, 1],
                [0, 1, 1, 0]))

    shortest_path = astar.runAlgo()

    # Example 5: complex; this one is good to play around with
    # Actual shortest path from 0 to 6 is 0, 3, 6
    # Link to graph: https://iq.opengenus.org/content/images/2021/10/dGhARBAUrLfUYhso.png
    astar = AStar(([0, 0, 15, 46, 40, 0, 0],
                [0, 0, 0, 0, 17, 40, 29],
                [15, 0, 0, 0, 53, 0, 0],
                [46, 0, 0, 0, 0, 11, 3],
                [40, 17, 53, 0, 0, 0, 31],
                [0, 40, 0, 11, 0, 0, 8],
                [0, 29, 0, 3, 31, 8, 0]))

    shortest_path = astar.runAlgo()

if __name__ == '__main__':
    main()