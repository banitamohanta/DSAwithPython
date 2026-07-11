class Solution(object):
    def countCompleteComponents(self, n, edges):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        complete = 0

        def dfs(node):
            visited[node] = True
            nodes.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
        for i in range(n):
            if not visited[i]:
                nodes = []
                dfs(i)
                node_count = len(nodes)
                edge_count = 0
                for node in nodes:
                    edge_count += len(graph[node])

                edge_count //= 2   

                if edge_count == node_count * (node_count - 1) // 2:
                    complete += 1

        return complete
        