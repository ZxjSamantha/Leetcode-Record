## 数组与字符串

1. 集合

2. 列表（线性关系，长度可变）

3. 数组（索引）

- 读取 O(1)
- 查找 O(N)
- 插入 
- 删除 O(N)

ex. [寻找数组的中心索引](https://leetcode-cn.com/problems/find-pivot-index/)

将左侧数组之和、数组总和、右侧数组之和抽象为leftSum, total, total-pivot-leftSum. 

```
class Solution:
  def pivotIndex(self, nums):
      total = sum(nums)
      leftSum = 0
      
      for i in range(len(nums)):
          if (2*leftSum + nums[i] == total):
              return i
          leftSum += nums[i]
      
      return -1
```

### 时间复杂度是多少？ O(n)

### 空间复杂度是多少？ O(1) 
