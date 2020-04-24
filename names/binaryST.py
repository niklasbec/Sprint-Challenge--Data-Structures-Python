class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value >= value:
            
            if self.left == None:
                self.left = BinarySearchTree(value)

            else:
                self.left.insert(value)

        elif value > self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
    
        if self.value > target:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        elif self.value < target:
            if self.right != None:
                return self.right.contains(target)
            else:
                return False
        elif target == self.value:
            return True
        else:
            return False