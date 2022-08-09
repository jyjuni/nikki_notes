#!/usr/bin/python
# -*- coding:utf-8 -*-

"""UnionFind.py: 并查集代码template(路径压缩)"""

__author__ = "Yijia Jin"
__copyright__ = "Copyright 2022, Yijia Jin"
__version__ = "1.0.0"
__email__ = "yj2682@columbia.edu"

class UnionFind:
    
    def __init__(self, n):
        self.parent = range(n)
        self.rank = [1] * n
        
    
    def find(self, x):
        """find root"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, p, q):
        """cnnect p,q"""  
        rootP, rootQ = self.find(p), self.find(q)
        if rootP == rootQ:
            return
        # 深度小的root接在深度大的root下
        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else: #深度相同
            self.parent[rootP] = rootQ
            self.rank[rootP] += 1
    
    
