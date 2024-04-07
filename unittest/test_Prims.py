import unittest
import sys
sys.path.append(".")
from shortest_path_algo.Prims import Prims

class TestPrims(unittest.TestCase):
   
    def testRunAlgo_BMH(self):

        adjMatrix = ([0,2,3,3,0,0,0],
                     [2,0,4,0,3,0,0],
                     [3,4,0,0,1,6,0],
                     [3,0,0,0,0,7,0],
                     [0,3,1,0,0,8,0],
                     [0,0,6,7,8,0,9],
                     [0,0,0,0,0,9,0])
        
        myPrims = Prims(adjMatrix)

        path =  myPrims.runAlgo()
        
        print(path)
        self.assertEqual(path, [(0,1),(1,4),(4,2),(0,3),(2,5),(5,6)])
    
    def testRunAlgo_LL(self):
        
        adjMatrix = ([0,2,3,3,0,0,0],
                     [2,0,4,0,3,0,0],
                     [3,4,0,0,1,6,0],
                     [3,0,0,0,0,7,0],
                     [0,3,1,0,0,8,0],
                     [0,0,6,7,8,0,9],
                     [0,0,0,0,0,9,0])
        
        myPrims = Prims(adjMatrix, 'linked list')

        path = myPrims.runAlgo()

        print(path)
        self.assertEqual(path, [(0,1),(0,2),(2,4),(0,3),(2,5),(5,6)])


if __name__ == "__main__":
    unittest.main()