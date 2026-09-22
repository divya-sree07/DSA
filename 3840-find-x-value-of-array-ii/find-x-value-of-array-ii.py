from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        class Node:
            def __init__(self):
                self.prod = 1
                self.cnt = [0] * k
        seg = [Node() for _ in range(4 * n)]
        def merge(left: Node, right: Node) -> Node:
            res = Node()
            res.prod = (left.prod * right.prod) % k
            res.cnt = left.cnt[:]
            for r in range(k):
                if right.cnt[r]:
                    nr = (left.prod * r) % k
                    res.cnt[nr] += right.cnt[r]
            return res
        def build(idx: int, l: int, r: int):
            if l == r:
                v = nums[l] % k
                seg[idx].prod = v
                seg[idx].cnt = [0] * k
                seg[idx].cnt[v] = 1
                return
            mid = (l + r) // 2
            build(idx * 2, l, mid)
            build(idx * 2 + 1, mid + 1, r)
            seg[idx] = merge(seg[idx * 2], seg[idx * 2 + 1])
        def update(idx: int, l: int, r: int, pos: int, val: int):
            if l == r:
                v = val % k
                seg[idx].prod = v
                seg[idx].cnt = [0] * k
                seg[idx].cnt[v] = 1
                return
            mid = (l + r) // 2
            if pos <= mid:
                update(idx * 2, l, mid, pos, val)
            else:
                update(idx * 2 + 1, mid + 1, r, pos, val)
            seg[idx] = merge(seg[idx * 2], seg[idx * 2 + 1])
        def query(idx: int, l: int, r: int, ql: int, qr: int) -> Node:
            if ql <= l and r <= qr:
                return seg[idx]
            mid = (l + r) // 2
            if qr <= mid:
                return query(idx * 2, l, mid, ql, qr)
            if ql > mid:
                return query(idx * 2 + 1, mid + 1, r, ql, qr)
            left = query(idx * 2, l, mid, ql, qr)
            right = query(idx * 2 + 1, mid + 1, r, ql, qr)
            return merge(left, right)
        build(1, 0, n - 1)
        ans = []
        for index, value, start, x in queries:
            nums[index] = value
            update(1, 0, n - 1, index, value)
            node = query(1, 0, n - 1, start, n - 1)
            ans.append(node.cnt[x])
        return ans