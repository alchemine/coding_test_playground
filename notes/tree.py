import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, id, e):
        self.id = id
        self.e  = e
        self.l  = None
        self.r  = None
    def __repr__(self):
        l = self.l.id if self.l is not None else None
        r = self.r.id if self.r is not None else None
        return f"[id: {self.id} | e: {self.e} | l: {l} | r: {r}]"


def preorder(node, traversal):
    if node is None:
        return
    traversal.append(node.id)
    preorder(node.l, traversal)
    preorder(node.r, traversal)


def inorder(node, traversal):
    if node is None:
        return
    preorder(node.l, traversal)
    traversal.append(node.id)
    preorder(node.r, traversal)


def postorder(node, traversal):
    if node is None:
        return
    postorder(node.l, traversal)
    postorder(node.r, traversal)
    traversal.append(node.id)
