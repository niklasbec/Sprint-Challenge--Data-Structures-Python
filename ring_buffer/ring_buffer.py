from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity > self.storage.length:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        else:
            if self.current == self.storage.head:
                self.storage.delete(self.storage.tail)
                self.storage.add_to_tail(item)
                self.current = self.storage.tail
            else:
                deleteable = self.current.prev
                self.storage.delete(deleteable)
                self.storage.insert_before(self.current, item)
                self.current = self.current.prev


    def get(self):
        list_buffer_contents = []
        x = self.storage.tail

        while x != None:
            list_buffer_contents.append(x.value)
            x = x.prev

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass
    def append(self, item):
        pass
    def get(self):
        pass
