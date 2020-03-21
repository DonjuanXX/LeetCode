#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (25.91%)
# Likes:    1913
# Dislikes: 0
# Total Accepted:    179.6K
# Total Submissions: 688.8K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#


# @lc code=start
class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 看完感觉听简单的
        # 首先就是排序,之后如果地一个就大于0直接返回,长度小于三直接返回
        # 然后双指针回溯法,当和>0,右侧指针左走,反之亦然\
        # 相同的直接下一个
        # 指针重合,直接下一个
        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    R = R - 1
                else:
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    L = L + 1
        return res


# @lc code=end
