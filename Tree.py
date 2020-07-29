class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insertsim(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# Insert complex leafs to node
    def insertC (self,r):

        if self.data:
            if r.high < self.data.high:
                if self.left is None:
                    self.left = Node(r)
                else:
                    self.left.insertC(r)
            elif r.high >= self.data.high:
                if self.right is None:
                    self.right = Node(r)
                else:
                    self.right.insertC(r)

        else:
            self.data = r


# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

    def PrintTreeC(self):
        if self.left:
            self.left.PrintTreeC()
        print((self.data.low),(self.data.high))
        if self.right:
                self.right.PrintTreeC()
class Range:
    def __init__(self,low,high):
        self.low=low
        self.high=high
def order(tr):
    if tr:
        if tr.left:
            if((tr.left.data.low==tr.data.low)and(tr.left.data.high<=tr.data.high)):
                return order(tr.left)
            else:
                return False
        elif tr.right:
            if((tr.right.data.high==tr.data.high)and(tr.right.data.low>=tr.data.low)):
                return order(tr.right)
            else:
                return False
        else:
            return True
    else:
        return True

#main
tr=Node (Range(1,10))
tr.insertC(Range(1,4))
tr.insertC(Range(5,10))
tr.insertC(Range(1,3))
tr.insertC(Range(5,6))
tr.right.right=Node(Range(8,10))
tr.PrintTreeC()
print(order(tr))
tr1=None
tr2=Node(Range(None,None))



