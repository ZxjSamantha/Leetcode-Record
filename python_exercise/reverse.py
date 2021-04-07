class Solution:
    def reverse(self, x:int)->int:

        ans = 0
        original = x
            
        while (x != 0) :
            pop = abs(x) % 10
            #python中取模向下取，负数-53取6，应用绝对值
            #print(pop)

            if ((ans > (2**31) / 10) or (ans == 2**31 and pop > 7)):
                    return 0
            if ((ans < (-2**31) / 10) or (ans == -2**31 and pop < -8)):
                    return 0
                
            ans = ans * 10 + pop
            #print(ans)   
            x = int(x / 10) #condition for loop 
            #...居然默认double
            #print(x)
        if (original >= 0): return ans
        if (original < 0): return -ans
        
        

if __name__=='__main__':
    case = Solution()
    test = case.reverse(x = -123)
    print(test)
