class BinaryMinHeap:
    def __init__(self) -> None:
        self.size = 0
        self.Heap = [0]
        self.ROOT = 1

    def is_empty(self):
        return self.size == 0
    
    def parent(self, position):
        return position // 2
    
    def left_child(self, position):
        return 2 * position
    
    def right_child(self, position):
        return (2 * position) + 1
    
    def swap(self, first_position, second_position):
        temp = self.Heap[first_position]
        self.Heap[first_position] = self.Heap[second_position]
        self.Heap[second_position] = temp

    def heapify_down(self, position):
        while True:
            left_child_pos = self.left_child(position)
            right_child_pos = self.right_child(position)
            smallest = position

            if left_child_pos <= self.size and self.Heap[left_child_pos][-1] < self.Heap[smallest][-1]:
                smallest = left_child_pos

            if right_child_pos <= self.size and self.Heap[right_child_pos][-1] < self.Heap[smallest][-1]:
                smallest = right_child_pos

            if smallest == position:
                break

            self.swap(position, smallest)
            position = smallest

    def heapify_up(self, position):
        while position > self.ROOT and self.Heap[self.parent(position)][-1] > self.Heap[position][-1]:
            self.swap(self.parent(position), position)
            position = self.parent(position)

    def insert(self, key_value_pair: tuple, priority: int):
        self.Heap.append((key_value_pair, priority))
        self.size += 1
        self.heapify_up(len(self.Heap) - 1)



    def delete_min(self):
        """
        
        """
        if self.is_empty():
            return None
        
        min_value = self.Heap[self.ROOT]
        self.Heap[self.ROOT] = self.Heap[-1]
        self.Heap.pop()
        self.size -= 1
        self.heapify_down(self.ROOT)

        return min_value

def main():
    min_heap = BinaryMinHeap()
    min_heap.insert(('key1', 'key2'), 13)
    min_heap.insert(('key3', 'key4'), 54)
    min_heap.insert(('key5', 'key6'), 6)
    min_heap.insert(('key7', 'key8'), 23)
    min_heap.insert(('key9', 'key10'), 36)
    min_heap.insert(('key11', 'key12'), 74)
    min_heap.insert(('key13', 'key14'), 17)
    min_heap.insert(('key15', 'key16'), 11)
    min_heap.insert(('key17', 'key18'), 33)
    min_heap.insert(('key19', 'key20'), 53)

    # Display the entire heap
    print("Min Heap:")
    for i in range(1, min_heap.size + 1):
        print(str(min_heap.Heap[i]))

    print("deleting ... ")
    for i in range(min_heap.size):
        print(str(min_heap.delete_min()))

if __name__ == '__main__':
    main()
