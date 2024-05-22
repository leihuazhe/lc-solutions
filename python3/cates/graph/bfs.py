from collections import deque

from python3.cates.graph.graph_adjacency_list import GraphAdjList
from python3.cates.module import Vertex

"""

时间复杂度：所有顶点都会入队并出队一次，使用 
 时间；在遍历邻接顶点的过程中，由于是无向图，因此所有边都会被访问 
 次，使用 
 时间；总体使用 
 时间。

空间复杂度：列表 res ，哈希集合 visited ，队列 que 中的顶点数量最多为 
 ，使用 
 空间。

"""


class BFS:

    def __init__(self, graph: GraphAdjList):
        self.graph = graph

    # 将遍历起始顶点 startVet 加入队列，并开启循环。
    # 在循环的每轮迭代中，弹出队首顶点并记录访问，然后将该顶点的所有邻接顶点加入到队列尾部。
    # 循环步骤 2. ，直到所有顶点被访问完毕后结束。
    #  防止重复遍历.

    def graph_bfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
        res = []
        # visited = set(start_vet)
        # set[Vertex] 是 Python 3.9 及更高版本中的类型提示语法，表明集合中的元素类型是 Vertex。
        visited = set[Vertex]([start_vet])
        # queue = deque()
        # queue.append(start_vet)
        queue = deque([start_vet])

        while queue:
            vet = queue.popleft()
            res.append(vet)
            # all adj vertex of the current vet.
            for adj_vet in graph.adj_list[vet]:
                if adj_vet in visited:
                    continue
                visited.add(adj_vet)
                queue.append(adj_vet)

        return res
