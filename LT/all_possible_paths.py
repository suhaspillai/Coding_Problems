class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        adj_list={}
        for i in range(len(graph)):
            for n in graph[i]:
                if i not in adj_list:
                    adj_list[i]=[]
                adj_list[i].append(n)
        q=[(0, [0])]
        end_node = len(graph)-1
        all_paths=[]
        while q:
            u, path_nodes = q.pop(0)
            if u in adj_list:        
                for v in adj_list[u]:
                    if v==end_node:
                        all_paths.append(path_nodes+[v])
                    else:
                        q.append((v, path_nodes+[v]))
        return all_paths
