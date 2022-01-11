class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        flag_status=False
        if len(edges)<1:
            if start == end:
                return True
            else:
                return False
    
        adj_list={}
        for e in edges:
            u, v = e[0], e[1]
            if u not in adj_list:
                adj_list[u] = []
            if v not in adj_list:
                adj_list[v]=[]
            adj_list[u].append(v)
            adj_list[v].append(u)
        dist={}
        for k in adj_list.keys():
            dist[k]=sys.maxsize
        dist[start]=0
        q=[start]

        while q:
            u = q.pop(0)
            for v in adj_list[u]:
                if dist[v] == sys.maxsize:
                    dist[v]=dist[u]+1
                    q.append(v)
                    if v == end:
                        flag_status=True
                        q=[]
                        break
        return flag_statuS
