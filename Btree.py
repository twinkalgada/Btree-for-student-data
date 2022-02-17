from collections.abc import MutableMapping

class BTree(MutableMapping):
    def __init__(self, order, mapping={},strategy=None):
        if order <= 2:
            raise ValueError("B-tree order must be at least 3")
        self.strategy = strategy
        if strategy is None:
            self.strategy = lambda key1, key2: key1 < key2  # Setting strategy to increasing order if no strategy was passed
        self.order = order
        self.max_values = order - 1
        self.root = _BTreeNode(None, None, self.strategy)
        self.update(mapping)    #Updates the tree with elements added together

    def __delitem__(self, key):
        del self.root[key]

    def __getitem__(self, key):
        value = self.root.search(key)[2]
        if value is not None:
            return value
        else:
           return False

    def __iter__(self):
        stack = []
        stack.append([self.root, 0])
        while len(stack) > 0:
            node, i = stack.pop()
            if len(node.children) == 0:
                for key,val in node.values:
                    yield key
            elif i < len(node.children):
                if (i > 0):
                    yield node.values[i - 1][0]
                stack.append([node, i + 1])
                stack.append([node.children[i], 0])

    def __setitem__(self, key, value):
        node, slot, val = self.root.search(key)
        return node.insert(self, key, value, slot)

    def __str__(self):
        stringVal = ""
        for val in self.root.values:
            stringVal += str(val)
        if len(self.root.children) > 0:
            for child in self.root.children:
                for val in child.values:
                    stringVal += str(val)
                stringVal = child.StringRecursive(stringVal)
        return stringVal


    def __len__(self):
        count = 0
        for i in enumerate(self):
            count += 1
        return count

    def toArray(self):
        ArrayCollection = []
        for element in self.items():
            ArrayCollection.append(element)
        return ArrayCollection

    # Used for internal iterator
    def foreach(self, function, data):
        for item in data:
            function(item)

    def externalIterator(self):
        dataIterator = iter(self)
        while True:
            try:
                key = next(dataIterator)
                print(key, self[key])
            except StopIteration:
                return

class _NullBtreeNode():
    def __init__(self):
        self.parent = None
        self.values = []
        self.children = []
        self.strategy = None

    def __iter__(self):
        yield None

    def isNull(self):
        return True

    def __str__(self):
        return " "

    def __len__(self):
        return 0

class _BTreeNode(object):

    def __init__(self, values=None, children=None,strategy=None):
        self.parent = _NullBtreeNode()
        self.values = values or []
        self.children = children or _NullBtreeNode()
        self.strategy = strategy
        if len(self.children) > 0:
            for i in self.children:
                i.parent = self

    def __len__(self):
        return len(self.values)

    def __str__(self):
        return '%r' % (
            self.values)

    # Recursively visit each node and get its string values
    def StringRecursive(self, strVal):
        if len(self.children) > 0:
            for i in self.children:
                for val in i.values:
                    strVal += str(val)
                i.StringRecursive(strVal)
        return strVal

    def pretty_print(self, level=0, tab=' '):
        print('Level %s%s%s' % (level, tab, self))
        if len(self.children) > 0:
            level += 1
            for i in self.children:
                i.pretty_print(level, tab + '   ')

    def isNull(self):
        return False

    """
    Return the index where to insert item x in list a, assuming a is sorted.
    The return value lo is such that all e in a[:lo] have e < x, and all e in
    a[lo:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    def _bisect_left_custom(self, a, key, lo=0, hi=None):
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.strategy(a[mid][0], key):
                lo = mid + 1
            else:
                hi = mid
        return lo

    """
    Search where the value can be inserted. Move down from the tree and return
    the leaf node and the insertion position where the value can be placed.
    """
    def search(self, key):
        i = self._bisect_left_custom(self.values, key)  #Find where the value can be inserted
        if (i != len(self.values) and not key < self.values[i][0]):
            if self.values[i][0] == key:
                # a value was found
                return (self, i, self.values[i][1])

        if len(self.children) > i and self.children[i]:
            # recursively search down the appropriate child node
            return self.children[i].search(key)

        return (self, i, None)

    """
    Split a B-tree node in two. Insert val into the resulting node. If additionally childNodes are passed
    then the _split_node function  is called recursively.
    """
    def _split_node(self, tree, key, val, slot=0, childNodes=_NullBtreeNode()):
        midList = [(key, val)]
        # get the median of self.values and val
        splitValues = self.values[0:slot] + midList + self.values[slot:]
        medianIdx = len(splitValues) // 2

        lv = splitValues[0:medianIdx]  # Get all values to the left of median
        medianVal = splitValues[medianIdx]
        rv = splitValues[medianIdx + 1:]  # Get all values to the right of median

        if self.children:
            # ChildNodes represent the nodes separated by val
            splitChildren = (self.children[0:slot] +
                             list(childNodes) +
                             self.children[slot + 1:])
            lc = splitChildren[0:len(lv) + 1]
            rc = splitChildren[len(lv) + 1:]
        else:  # If it is not an internal node it will not have any children
            lc = None
            rc = None

        leftNode = _BTreeNode(lv, lc, self.strategy)
        rightNode = _BTreeNode(rv, rc, self.strategy)
        if self.parent:
            self.parent.insert(tree,
                               medianVal[0],
                               medianVal[1],
                               None,
                               (leftNode, rightNode))
        else:
            newRoot = _BTreeNode([medianVal], [leftNode, rightNode], self.strategy)
            leftNode.parent = newRoot
            rightNode.parent = newRoot
            tree.root = newRoot

    """
    Insertions start from leaf node and if we need to insert in parent
    it is called recursively using split node function
    """
    def insert(self, tree, key, val, slot=None, childNodes=_NullBtreeNode()):
        if slot is None:
            slot = self._bisect_left_custom(self.values, key)  # Find where the value can be inserted

        if len(self.values) < tree.max_values:
            self.values.insert(slot, (key, val))
            if len(childNodes) > 0:
                # update the parent reference in the nodes we are about to add
                for i in childNodes:
                    i.parent = self
                self.children[slot:slot + 1] = childNodes
            return val

        # To check for childNodes
        self._split_node(tree, key, val, slot, childNodes)
        return val
