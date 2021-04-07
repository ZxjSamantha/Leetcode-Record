# A search problem
"""
def digitsum(n):
    ans = 0
    while n: 
        ans += n%10
        n //= 10
    return ans 

class Solution:
    def movingCount(self, m: int, n: int, k: int)-> int:
        #i, j = 0
        from queue import Queue
        q = Queue()
        q.put((0,0)) #起点为(0,0)
        s = set()

        while not q.empty():
            x, y = q.get()
            if (x,y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x)+digitsum(y) <= k:
                s.add((x,y))
        #for i in range(0,n):
            #for j in range(0,m):
                for nx, ny in [(x+1, y), (x,y+1)]:
                    q.put((nx,ny))#?
        return len(s)
                
                    
                #else: continue
                # problem: how could robot move one block once？

"""
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if i >= m or j >= n or si + sj > j or (i,j) in visited: return 0
            visited.add((i,j))

            return 


test = Solution()
#case = test.movingCount(m=2, n=2, k=1)
case = test.movingCount(m=3, n=3, k=3)

print(case)