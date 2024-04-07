import unittest
import sys
sys.path.append(".")
from shortest_path_algo.AStar import AStar


class TestAStar(unittest.TestCase):
   
    def testRunAlgo_BMH(self):

        adjMatrix = ([0, 196, 670, 355, 461],
                     [196, 0, 479, 164, 270],
                     [670, 479, 0, 350, 228],
                     [355, 164, 350, 0, 163],
                     [461, 270, 228, 163, 0])
        
        myAStar = AStar(adjMatrix)

        shortestPath =  myAStar.runAlgo()
        
        self.assertEqual(shortestPath, [0, 4])
    
    def testRunAlgo_LL(self):
        
        adjMatrix = ([0, 196, 670, 355, 461],
                     [196, 0, 479, 164, 270],
                     [670, 479, 0, 350, 228],
                     [355, 164, 350, 0, 163],
                     [461, 270, 228, 163, 0])
        
        myAStar = AStar(adjMatrix, 'linked list')

        shortestPath =  myAStar.runAlgo()

        self.assertEqual(shortestPath, [0, 4])


if __name__ == "__main__":
    unittest.main()