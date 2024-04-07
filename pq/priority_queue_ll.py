"""Implements a priority queue with a linked list."""

class LinkedList:
    def __init__(self) -> None:
        self.root = None

    # if there isn't a root, the list is empty
    def is_empty(self):
        return self.root == None

    # insert aka "push" method
    def insert(self, key_value_pair: tuple, priority: int):
        
        # make the new node
        node = Node(priority, key_value_pair)

        # if this is the first value in the list, it's the root
        if self.root is None:
            self.root = node
        
        # otherwise, add it to the appropriate place in the list
        else:
            currNode = self.root

            # if the priority is lower than the root
            if node.priority < currNode.priority:
                tempNode = self.root
                node.next = tempNode
                self.root = node

            # if not, go through each node and insert it where it belongs
            else:

                # make sure there's a node there
                while currNode.next:

                    # if the new node is lower priority, it'll be next, so break out to insert
                    if node.priority < currNode.next.priority:
                        break
                    
                    # otherwise, move to the next node
                    currNode = currNode.next

                # insert the node wherever we stopped, or at the end of the list
                temp = currNode.next
                currNode.next = node
                node.next = temp
    
    # delete aka "pop" method
    def delete_min(self):
   
        # if there's no list, there's nothing to return
        if self.root is None:
            return None
        
        # otherwise, return the lowest value
        min_value = (self.root.key_value_pair, self.root.priority)

        # delete the root
        self.root = self.root.next

        return min_value

class Node:
    def __init__(self, priority, key_value_pair) -> None:
        self.priority = priority
        self.key_value_pair = key_value_pair
        self.next = None

def main():
    ll = LinkedList()
    ll.insert(('key1', 'key2'), 13)
    ll.insert(('key3', 'key4'), 14)
    ll.insert(('key5', 'key6'), 6)
    ll.insert(('key7', 'key8'), 23)
    ll.insert(('key9', 'key10'), 36)
    ll.insert(('key11', 'key12'), 74)
    ll.insert(('key13', 'key14'), 17)
    ll.insert(('key15', 'key16'), 11)
    ll.insert(('key17', 'key18'), 33)
    ll.insert(('key19', 'key20'), 53)

    # print the entire list
    print("Printing the Linked List: ")

    # print the root first
    if ll.root is not None:

        print("\nPrinting root.")
        print("Priority is: " + str(ll.root.priority))
        print("KVP is: " + str(ll.root.key_value_pair))

        currNode = ll.root

        # then, print each node until there's none left
        while currNode.next is not None:
            
            print("\nPrinting next node.")
            print("Priority is: " + str(currNode.next.priority))
            print("KVP is: " + str(currNode.next.key_value_pair))
            currNode = currNode.next


    print("\nDeleting... ")

    while ll.root is not None:
        print(str(ll.delete_min()))


if __name__ == '__main__':
    main()