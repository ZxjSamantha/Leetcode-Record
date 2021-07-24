## 数组与字符串

1. 集合

2. 列表（线性关系，长度可变）

3. 数组（索引）

- 读取 O(1)
- 查找 O(N)
- 插入 
- 删除 O(N)

---

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

---

[搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)

排序数组中找插入位置：在一个有序数组中找第一个大于等于target下标。 

二分查找：
左右边界怎么找？
终止条件是什么：left > right 

### 时间复杂度是多少？ O(logn)
### 空间复杂度是多少？ O(1)

---

[合并区间](https://leetcode-cn.com/problems/merge-intervals/)

```
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        merged = []
        
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
            # 如果结果集最后一个元素的右边界比新加入区间的左边界小，直接加入结果集
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
            # 如果有重合，更新区间右边界
        return merged
        
```

类似题目：

[重叠区间，合并区间，插入区间](https://mp.weixin.qq.com/s/ioUlNa4ZToCrun3qb4y4Ow)


怎么比较一个列表中任意两个元素？

### 要比较，先排序！！！

按照左区间排序？右区间排序？

---

字符串的操作对象是**字符串整体和它的字串**，常用操作有**比较**和**连接**。 




