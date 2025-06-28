import sys

input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def update_range(self, node, start, end, left, right):

        if self.lazy[node]:
            self.tree[node] = (end - start + 1) - self.tree[node]
            if start != end:
                self.lazy[node * 2] ^= 1
                self.lazy[node * 2 + 1] ^= 1
            self.lazy[node] = 0

        if start > right or end < left:
            return
 
        if start >= left and end <= right:
            self.tree[node] = (end - start + 1) - self.tree[node]
            if start != end:
                self.lazy[node * 2] ^= 1
                self.lazy[node * 2 + 1] ^= 1
            return
        
        mid = (start + end) // 2
        self.update_range(node * 2, start, mid, left, right)
        self.update_range(node * 2 + 1, mid + 1, end, left, right)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, node, start, end, left, right):

        if self.lazy[node]:
            self.tree[node] = (end - start + 1) - self.tree[node]
            if start != end:
                self.lazy[node * 2] ^= 1
                self.lazy[node * 2 + 1] ^= 1
            self.lazy[node] = 0

        if start > right or end < left:
            return 0

        if start >= left and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        return self.query(node * 2, start, mid, left, right) + \
               self.query(node * 2 + 1, mid + 1, end, left, right)

n, m = map(int, input().split())
seg_tree = SegmentTree(n)

for _ in range(m):
    o, s, t = map(int, input().split())
    if o == 0:
        seg_tree.update_range(1, 0, n-1, s-1, t-1)
    else:
        print(seg_tree.query(1, 0, n-1, s-1, t-1))