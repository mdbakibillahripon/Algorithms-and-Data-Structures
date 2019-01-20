#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, vertex, parent, D):
    if D[vertex] == float('inf'):
        if not tree[vertex].children:
            D[vertex] = tree[vertex].weight
        else:
            m1 = tree[vertex].weight
            for child in tree[vertex].children:
                if child != parent:
                    for grand in tree[child].children:
                        if grand != vertex:
                            m1 += dfs(tree, grand, child, D)
            m0 = 0
            for child in tree[vertex].children:
                if child != parent:
                    m0 += dfs(tree, child, vertex, D)
            D[vertex] = max(m1, m0)
    return D[vertex]

def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    D = [float('inf') for _ in range(len(tree))]
    return dfs(tree, 0, -1, D)


def main():
    tree = ReadTree();
    weight = MaxWeightIndependentTreeSubset(tree);
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
