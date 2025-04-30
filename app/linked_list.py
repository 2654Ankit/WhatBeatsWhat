class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.values_set = set()

    def add(self, value):
        if value in self.values_set:
            return False  # Already exists
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.values_set.add(value)
        return True

    def history(self):
        current = self.head
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return result
