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


def postorder(node, traversal):
    if node is None:
        return
    postorder(node.l, traversal)
    postorder(node.r, traversal)
    traversal.append(node.id)


def solution(nodeinfo):
    VERBOSE = True
    def log(*msg):
        if VERBOSE: print(*msg)
    # -----------------------------

    # 1. Name nodes
    info = [(id, x, y) for id, (x, y) in enumerate(nodeinfo, start=1)]


    # 2. Construct BST
    nodes = {}
    for id, e, _ in sorted(info, key=lambda x: x[2], reverse=True):
        node = Node(id, e)

        i = 1
        if i not in nodes:
            nodes[i] = node
            continue

        while True:
            parent = nodes[i]
            i = (2*i+1) if node.e > parent.e else (2*i)
            if i not in nodes:  # current node
                nodes[i] = node
                if node.e > parent.e:
                    parent.r = node
                else:
                    parent.l = node
                break


    # 3. Traversal
    preorder_traversal = []
    postorder_traversal = []

    preorder(nodes[1], preorder_traversal)
    postorder(nodes[1], postorder_traversal)
    return [preorder_traversal, postorder_traversal]


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))
