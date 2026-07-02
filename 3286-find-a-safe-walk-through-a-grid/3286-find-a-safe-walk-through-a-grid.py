class Solution(object):
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]

        dq = deque([(0, 0)])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while dq:
            x, y = dq.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    cost = dist[x][y] + grid[nx][ny]

                    if cost < dist[nx][ny]:
                        dist[nx][ny] = cost
                        if grid[nx][ny] == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))

        return dist[m-1][n-1] < health
        