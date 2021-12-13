class Solution:
	def get_neighbors(self, graph, i, count):
		for k in graph[i]:
			if k not in visited:
				visited.add(k)
				count+=1
				count = self.get_neighbors(graph, k, count)
		return count


	def maximumDetonation(self, bombs: List[List[int]]) -> int:
		graph = {i:[] for i in range(len(bombs))}
		for i in range(len(bombs)):
			c_x, c_y, c_r = bombs[i][0], bombs[i][1], bombs[i][2]
			for j in range(len(bombs)):
				x, y = bombs[j][0], bombs[j][1]
				if ((c_x-x)**2 + (c_y - y)**2) <= c_r**2:
					graph[i].append(j)


		tot_detonate_bombs=1
		for i in range(len(graph)):
			visited=set()
			visited.add(i)
			count=1
			tot_detonate_bombs = max(tot_detonate_bombs, self.get_neighbors(graph, i, count))
		return tot_detonate_bombs
