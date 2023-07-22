# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None


from dataclasses import dataclass

@dataclass
class Node:
    v: 'value'       = None
    l: 'left child'  = None
    r: 'right child' = None


class BST:
    def __init__(self):
        self.head = None

    def insert(self, v):
        if not self.head:
            self.head = Node(v)
            return True

        cn = self.head  # current node
        while cn:
            if v < cn.v:
                if cn.l:
                    cn = cn.l
                else:
                    cn.l = Node(v)
                    return True
            else:
                if cn.r:
                    cn = cn.r
                else:
                    cn.r = Node(v)
                    return True

    def delete_max(self):
        if self.head is None:
            return False  # empty
        elif (not self.head.l) and (not self.head.r):
            self.head = None
            return True # head
        elif self.head.l and (not self.head.r):
            self.head = self.head.l
            return True # head
        else:  # self.head.l and self.head.r
            p  = self.head  # parent node
            cn = self.head

            # tracking max value until cn is leaf node
            while cn.r:
                p  = cn
                cn = cn.r

            if cn.l:
                p.r = cn.l
            else:
                p.r = None
            return True

    def delete_min(self):
        if self.head is None:
            return False  # empty
        elif (not self.head.l) and self.head.r:
            self.head = self.head.r
            return True
        elif (not self.head.l) and (not self.head.r):
            self.head = None
            return True
        else:  # self.head.l and self.head.r
            p  = self.head
            cn = self.head

            while cn.l:
                p  = cn
                cn = cn.l

            if cn.r:
                p.l = cn.r
            else:
                p.l = None
            return True

    def search(self):
        cn = self.head
        if cn is None:
            return [0, 0]

        # find min value
        cn = self.head
        while cn.l:
            cn = cn.l
        min_v = cn.v

        # find max value
        cn = self.head
        while cn.r:
            cn = cn.r
        max_v = cn.v

        return [max_v, min_v]

def solution(operations):
    tree = BST()
    for op, val in map(lambda x: x.split(), operations):
        if op == 'I':
            tree.insert(int(val))
        elif op == 'D' and val == '1':
            tree.delete_max()
        elif op == 'D' and val == '-1':
            tree.delete_min()
    return tree.search()


args = [
    # ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]
    # ["I 2","I 4","D -1", "I 1", "D 1"]
    # ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    # ["I 3", "I 2", "I 1", "D 1", "D 1", "I 3", "D -1"]
    ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]
]
print(solution(*args))
