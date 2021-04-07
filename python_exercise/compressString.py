class Solution:
    def compressString(self, S:str) -> str: 
        if len(S) == 0: return S

        ans = ''
        count = 0
        ch = S[0]

        for c in S:
            if c == ch:
                count += 1
            else: 
                ans += ch + str(count)
                ch = c
                count = 1
        ans += ch + str(count)

        return ans if len(ans) < len(S) else S

case = Solution()

test = case.compressString("asdhklzxcbmaaaaaaaahhhhhssssssssllllllll")
print(test)

