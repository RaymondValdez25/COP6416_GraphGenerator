import matplotlib.pyplot as plt
import networkx as nx
import PySimpleGUI as sg
import matplotlib.animation
from functools import partial
from shortest_path_algo.Prims import Prims
from shortest_path_algo.AStar import AStar

sg.theme('DarkBlue2')   # Add a theme
#Create GUI layout
layout = [
    [
        sg.Text('Node 1 label', pad=(10, 10), font=("Roboto", 12)), sg.InputText(size=(23, 1), font=("Roboto", 12)),
        sg.Text('Node 2 label', pad=(10, 10), font=("Roboto", 12)),
        sg.InputText(size=(23, 1), font=("Roboto", 12)), sg.Text('Weight', pad=(10, 10), font=("Roboto", 12)),
        sg.InputText(size=(23, 1), font=("Roboto", 12))
    ],
    [ sg.Push(),
        sg.Button('Add Edge', font=("Roboto", 12)), sg.Button('Default Edges', font=("Roboto", 12)),
        sg.Button('Show', font=("Roboto", 12)),
        sg.Push()
    ],
    [   
        sg.Push(),
        sg.Button('Set PQ-LinkedList', font=("Roboto", 12)),
        sg.Push()
    ],
    [   
        sg.Text('source', pad=(10, 10), font=("Roboto", 12)), 
        sg.InputText(size=(23, 1), font=("Roboto", 12)), sg.Text('destination', pad=(10, 10), font=("Roboto", 12)), 
        sg.InputText(size=(23, 1), font=("Roboto", 12)), sg.Button('Run AStar', font=("Roboto", 12)),
        sg.Button('Run Prims', font=("Roboto", 12))
    ],
    [
        sg.Push(),
        sg.Button('Cancel', font=("Roboto", 12)), sg.Button('Clear', font=("Roboto", 12)),
        sg.Push()
    ]
        ]

#Create the graph
G = nx.Graph()

#Create keyDictionary
key_index_dict = dict()

def get_index(key):
    if(key not in key_index_dict):
        print("index doesn't exist")
        return None
    return key_index_dict[key]

def get_key(index):
    for key in key_index_dict:
        if (key_index_dict[key] == index):
            return key
    print("key doesn't exist")
    return None

#display GUI
window = sg.Window('Graph Generator', layout)

def convertPathToanimationNodes(inputPath):
    print("inputPath", inputPath)
    animationNodes = []
    innerNodes = []

    for node1,node2 in inputPath:
        innerNodes.append(node1)
        innerNodes.append(node2)
        animationNodes.append(innerNodes[:])

    return animationNodes

def convertPathToEdgeList(inputPath):
    outerOuterlist = []
    outputlist = []
    innerlist = []

    for node1,node2 in inputPath:
        innerlist = []
        innerlist.append(node1)
        innerlist.append(node2)
        outputlist.append(innerlist[:])
        outerOuterlist.append(outputlist[:])
    
    return outerOuterlist

def clear():

    # PQ_type is declared global so it can be changed across these methods run_prims() and set_PQ()
    global PQ_type
    PQ_type = None
    print(PQ_type, "PQ switch to default BinaryMinHeap")

    G.clear()
    key_index_dict.clear()
    plt.clf()
    plt.close()

def update(num, animationNodes, animationEdgeList, ax, isDijkstra):

    # num is the current iteration
    print(num)

    # Print the paths
    print('animationNodes', animationNodes[num])
    print('animation edges', animationEdgeList[num])

    # Background nodes
    addGraphToPlot()

    # Query nodes and edges
    pos = nx.spring_layout(G,seed=7)
    query_nodes = nx.draw_networkx_nodes(G, pos=pos, nodelist=animationNodes[num], node_color="blue", edgecolors= "white")
    query_nodes.set_edgecolor("white")
    nx.draw_networkx_labels(G, pos=pos, labels=dict(zip(animationNodes[num],animationNodes[num])),  font_color="white")
    nx.draw_networkx_edges(G, pos=pos, edgelist=animationEdgeList[num], edge_color="red")

    toPrint = []
    currentEdgePath = animationEdgeList[num]
    for src, dest in currentEdgePath:
        toPrint.append(src)
        toPrint.append("->")
        toPrint.append(dest)
        toPrint.append(", ")
    if(isDijkstra):
        ax.set_title("A* Shortest Path: " +  ''.join(toPrint), fontweight="bold")
    else:
        ax.set_title("Prim's MST : " +  ''.join(toPrint), fontweight="bold")

def add_edge():
    node1 = values[0]
    node2 = values[1]
    weight = values[2]

    if(node1 == '' or node2 == '' or weight == ''):
        sg.popup("All fields must be populated")
        return
    
    try:
        float(weight)
    except ValueError:
        sg.popup("Weight must be a number")
        return

    G.add_edge(node1,node2,weight=float(weight))
    if(node1 not in key_index_dict):
        key_index_dict[node1] = len(key_index_dict)
    if(node2 not in key_index_dict):
        key_index_dict[node2] = len(key_index_dict)

def default_edges():
    G.clear()
    key_index_dict.clear()
    elist = [('a', 'b', 2.0), ('b', 'c', 3.0), ('a', 'c', 7.0), ('c', 'd', 7.3), ('d','a',10.0), ('c', 'e', 5.0), ('e', 'f', 3.0), ('f', 'd', 5.1)]
    key_index_dict['a'] = 0
    key_index_dict['b'] = 1
    key_index_dict['c'] = 2
    key_index_dict['d'] = 3
    key_index_dict['e'] = 4
    key_index_dict['f'] = 5
    G.add_weighted_edges_from(elist)

def addGraphToPlot():
    pos = nx.spring_layout(G, seed=7)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_nodes(G, pos, node_color= "white", edgecolors="black")
    nx.draw_networkx_edges(G, pos, edge_color="gray")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

def getAdjMatrix():
    return nx.adjacency_matrix(G).todense()

def show():
    if(nx.is_empty(G)):
        sg.popup("Graph is empty")
        return
    plt.close()
    print(getAdjMatrix())
    addGraphToPlot()
    plt.show()

def run_Dijkstras():
    """If no source and destination are given, assumes the first node is the source and the last is the destination."""

    print("run AStar")
    if(nx.is_empty(G)):
        sg.popup("Graph is empty")
        return

    global PQ_type # 
    plt.close()
    fig, ax = plt.subplots()
    plt.axis('off')
    addGraphToPlot()

    #Run A* algorithm
    myAStar = AStar(getAdjMatrix(), PQ_type) # add the set PQ-LinkedList
    # print("debugging from run astar ", type(set_PQ())) # remove for debugging

    # check if the source and destination are populated, and only include them if they are
    if values[3] != "" and values[4] != "":

        # convert the values to integers with the dictionary
        start = get_index(values[3])
        goal = get_index(values[4])
        if(start is None or goal is None):
            sg.popup("Source or destination doesn't exist")
            return

        Indexpath = myAStar.runAlgo(start, goal)

    else:
        Indexpath = myAStar.runAlgo()

    # convert A* index path to the Prim format
    tempIndexpath = []

    # loop through the shortest path list
    for i in range(len(Indexpath) - 1):

        # get the current and the next element
        a = Indexpath[i]
        b = Indexpath[i + 1]

        # create a tuple of the two elements
        pair = (a, b)

        # append the pair to the new index path
        tempIndexpath.append(pair)

    # set the Indexpath to the new Indexpath
    Indexpath = tempIndexpath

    indexToKeyPath = []

    for src,dest in Indexpath:
        newSrc = get_key(src)
        newDest = get_key(dest)
        indexToKeyPath.append((newSrc, newDest))

    animationNodes = convertPathToanimationNodes(indexToKeyPath)
    animationEdgeList = convertPathToEdgeList(indexToKeyPath)

    print("full node path", animationNodes)
    print("full edge path", animationEdgeList)

    frames = len(animationEdgeList[-1])
    anim = matplotlib.animation.FuncAnimation(fig, partial(update, animationNodes=animationNodes, animationEdgeList=animationEdgeList, ax=ax, isDijkstra = True), frames=frames, interval=1000, repeat=False)
    plt.show()


PQ_type = None

def set_PQ(default=None):
    """ 
    A method to set the type of PQ to either none which will run Prims PQ Binary Min heap 
    else it will run PQ LinkedList
    """
    print("----------- set PQ clicked")
    if default is None:
        return None
    else:
        # print("----------- set PQ clicked")
        return default

def run_Prims():
    print("run Prims")
    if(nx.is_empty(G)):
        sg.popup("Graph is empty")
        return

    global PQ_type # 
    plt.close()
    fig, ax = plt.subplots()
    plt.axis('off')
    addGraphToPlot()

    #Run Prims algorithm
    myPrims = Prims(getAdjMatrix(), PQ_type) # add the set PQ-LinkedList
    # print("debugging from run prims ", type(set_PQ())) # remove for debugging
    Indexpath = myPrims.runAlgo()

    indexToKeyPath = []

    for src,dest in Indexpath:
        newSrc = get_key(src)
        newDest = get_key(dest)
        indexToKeyPath.append((newSrc, newDest))

    animationNodes = convertPathToanimationNodes(indexToKeyPath)
    animationEdgeList = convertPathToEdgeList(indexToKeyPath)

    print("full node path", animationNodes)
    print("full edge path", animationEdgeList)

    frames = len(animationEdgeList[-1])
    anim = matplotlib.animation.FuncAnimation(fig, partial(update, animationNodes=animationNodes, animationEdgeList=animationEdgeList, ax=ax, isDijkstra = False), frames=frames, interval=1000, repeat=False)
    plt.show()


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == 'Add Edge':
        add_edge()
    elif event == "Default Edges":
        default_edges()
    elif event == "Show":
        show()
    elif event == "Run AStar":
        run_Dijkstras()
    elif event == "Run Prims":
        run_Prims()
    elif event == "Set PQ-LinkedList":
        PQ_type = set_PQ("LL")  # Update the PQ_type attribute
        print(PQ_type)
    elif event =='Clear':
        clear()
window.close()