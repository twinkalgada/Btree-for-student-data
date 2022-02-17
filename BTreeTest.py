import unittest
import Btree as BTree


class BTreeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BTree.BTree(3)
        self.tree[1] = 2
        self.tree[12] = 3
        self.tree[4] = 16
        self.tree[20] = 88
        self.tree[6] = 9
        self.tree[16] = 36
        self.tree[19] = 43
        self.tree[50] = 18
        self.tree[25] = 0
        self.tree[17] = 14

    def test_setitem(self):
        self.tree[13] = 28
        self.assertTrue(self.tree[13])


    def test_item_not_found(self):
        self.tree[1] = 2
        self.assertFalse(self.tree[5])

    def test_get_item(self):
        self.assertTrue(self.tree[50])

    def test_toString(self):
        self.assertEqual("(12, 3)(4, 16)(1, 2)(6, 9)(19, 43)(25, 0)(16, 36)(17, 14)(20, 88)(50, 18)", str(self.tree))


    def test_update_mapping(self):
        data = {1:2, 2:3, 3:4, 4:5, 0:2, 5:6, 22:7, 20:8, 9:5}
        self.tree = BTree.BTree(3, data)
        self.assertTrue(self.tree[20])


    def test_strategy(self):
        treeData = {1:2, 2:3, 3:4, 4:5, 0:2, 5:6, 22:7, 20:8, 9:5}
        strategyDecreasing = lambda key1, key2: key1 > key2
        BtreebyDecreasing = BTree.BTree(3, treeData, strategyDecreasing)
        BtreeItems = "{" + ", ".join(f"{k}: {v}" for k, v in BtreebyDecreasing.items()) + "}"
        self.assertEqual("{22: 7, 20: 8, 9: 5, 5: 6, 4: 5, 3: 4, 2: 3, 1: 2, 0: 2}",BtreeItems)

    def test_iterator(self):
        BtreeIterator = iter(self.tree)
        self.assertEqual(1,next(BtreeIterator))
        self.assertEqual(4,next(BtreeIterator))
        self.assertEqual(6,next(BtreeIterator))
        next(BtreeIterator)  #12
        self.assertEqual(16,next(BtreeIterator))

    def test_nullNode(self):
        nullNode = BTree._NullBtreeNode()
        self.assertTrue(nullNode.isNull())

    def test_nonNullNode(self):
        rootNode = self.tree.root
        self.assertFalse(rootNode.isNull())


if __name__ == '__main__':
    unittest.main()