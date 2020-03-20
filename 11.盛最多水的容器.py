#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#
# https://leetcode-cn.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (61.85%)
# Likes:    1210
# Dislikes: 0
# Total Accepted:    158.4K
# Total Submissions: 255K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
#
#
#
#
#
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#
#
# 示例：
#
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
#
#


# @lc code=start
class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 目前我只想到了暴力算法,找出所有来计算.所有排列组合,用组合中短者乘下标差
        """
        TC O(n^2)   SC O(1)
        Time Limit Exceeded
        45/50 cases passed (N/A)
        max = 0
        for i in range(len(height)):
            j = i + 1
            while j < len(height):
                storage = min(height[i], height[j]) * (j - i)
                j += 1
                max = storage if storage > max else max
        return max
        """
        # 显然还需要更快的方式,因为只要做到当前的最好选择即可.
        # 所谓的最好选择,就是缩小桶的边,也就是比较两边下一个移动位的高度,相对高的作为边.
        # 但是我这个却错了,我只考虑了对下一个边进行比较,却完全忽略了对当前边的判断
        # 过于追求速度而导致了错误
        """
        TC O(n)   SC O(1)
        Wrong Answer  example:[1,2,4,3]
        17/50 cases passed (N/A)
        start, end, max = 0, len(height) - 1, 0
        while start != end:
            storage = min(height[start], height[end]) * (end - start)
            max = storage if storage > max else max
            if height[start + 1] > height[end - 1]:
                start += 1
            elif height[start + 1] == height[end - 1]:
                if height[start] <= height[end]:
                    start += 1
                else:
                    end -= 1
            else:
                end -= 1
        return max
        """
        # 我考虑的有点多了,实际上我们来想一下,每次移动的话,要想保住当前的最大面积,需要移动的是什么呢?
        # 当移动长边时,内里肯定变小,因为容量由短边决定.
        # 当移动短边时,如果两个都是长边,内里容积就会变大
        # 如果两边一样的话,如何移动呢?
        # 其实这种情况可以忽略,如果内里有两根超长的壁,那么两边一样的只是形成了短边被淘汰掉而不会错过
        # 如果没有两根超长的壁,那么不会出现更大的结果,即可忽略
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res
        # 这个解法巧妙运用了max来减少了几个三元表达判断,也巧妙运用短边判断来计算容积


# @lc code=end
