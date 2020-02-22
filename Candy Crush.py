class StackList:
    """
    Stack ADT implementation using Python List, i.e. a dynamic array
    """
    def __init__(self):
        self._items = []

    def getTop(self):
        """ Return the top item of stack. None if stack is empty."""
        if not self.isEmpty():
            return self._items[-1]    #negative index = count from the end of list
        else:
            return None

    def push(self, newItem):
        """ Push (i.e. add) [newItem] on top of stack."""
        self._items.append(newItem)

    def pop(self):
        """ Pop (i.e. pop) [newItem] from top of stack."""
        if not self.isEmpty():
            self._items.pop()         #last item is removed
            return True
        else:
            return False

    def size(self):
        """ Return size of the Stack, i.e. number of items"""
        return len(self._items)
    
    def isEmpty(self):
        """ Return True if Stack is empty. False otherwise"""
        return len(self._items) == 0


def candyCrush( L ):
    """ L is a list of candies, represented as number [1..4]"""
    #Using only one stack s to solve the problem
    s = StackList()
    if L == []:
        return 0
    s.push(L[0])

    def _newCandy(num): #get new more powerful candy
        newCandy = (s.getTop() + 1)
        if newCandy == 5:
            newCandy = 1
        return newCandy
    for i in range(1, len(L)):
        
        if s.getTop() != L[i]:
            s.push(L[i])
        
        else:
            candy = _newCandy(s.getTop())
            s.pop()
            while s.getTop() == candy:
                candy = _newCandy(s.getTop())
                s.pop()
            s.push(candy)
    output = []
    while not s.isEmpty():
        output.append( s.getTop())
        s.pop()
    
    return output


def main():
    print(candyCrush([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
