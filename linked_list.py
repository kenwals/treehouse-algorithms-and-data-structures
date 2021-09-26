from typing import Counter


class Node:
    """
    an object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return "<Node data: %s>" %  self.data

class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes linear time - 0(n)
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        
        return count

    def add(self, data):
        """
        adds a new node containing data at the head of the list
        Take contant time - 0(1) 

        Args:
            data ([type]): [description]
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head =  new_node

    def search(self, key):
        """
        Search for the first node that contains data that matches the key
        
        Takes linear time - 0(n)
        Args:
            key ([type]): [description]

        Returns:
            the node or none if not find
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        inserts a new Node containing data at index position
        insertion takes contant time - 0(1)
        but finding the node at the insertion point takes linear time - 0(n)
        therefore it takes an overall linear time - 0(n)
        Args:
            data ([type]): [description]
            index ([type]): [description]
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)
            
            position = index
            current = self.head
            
            while position > 1:
                current = node.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node
            
            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Remove Node containing data that matchs the key
        returns the node or None if the key doesn't exist
        Takes linear time - 0(n)

        Args:
            key ([type]): [description]

        Returns:
            [type]: [description]
        """
        current = self.head
        previous = None
        found = False
        
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position +=1
            
            return current


    def __repr__(self):
        """
        Returns a string representation of the list
        Takes linear time - 0(n)
        """
        
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
        
            current = current.next_node
        return '-> '.join(nodes)

