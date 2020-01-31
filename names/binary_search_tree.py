import sys


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
            if value < self.value:
                if not self.left:
                    self.left = BinarySearchTree(value)
                else:
                    return self.left.insert(value)
            else:
                if not self.right:
                    self.right = BinarySearchTree(value)
                else:
                    return self.right.insert(value)
    #greater than or less than root?
    #if less than, go left
    #if greater, go right

        # if < or = go to right child



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value and self.left != None: 
            return self.left.contains(target)
        elif target > self.value and self.right != None:
            return self.right.contains(target)
        else:
            return False
        #target is value we seek
        #compare target to root
        # go left if less than
        #go right if greater
        #compare to next node down on proper side
        #if greater than child of root, go right
        # if less than, go left

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)        
        if self.right != None:
            self.right.for_each(cb)
        


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node != None:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.size != 0:
            temp = queue.dequeue()
            print(temp.value)
            if temp.left is not None:
                queue.enqueue(temp.left)
            if temp.right is not None:
                queue.enqueue(temp.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.size != 0:
            temp = stack.pop()
            print(temp.value)
            if temp.left is not None:
                stack.push(temp.left)
            if temp.right is not None:
                stack.push(temp.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass