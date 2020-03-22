#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (43.29%)
# Likes:    383
# Dislikes: 0
# Total Accepted:    84.1K
# Total Submissions: 193.7K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#
#
#


# @lc code=start
class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 这你吗不跟刚才那题一样了吗
        """
        Your runtime beats 13.79 % of python submissions
        Your memory usage beats 5.73 % of python submissions (12.7 MB)
        min = 100000
        nums.sort()
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
            if len(nums) == 3:
                return nums[0] + nums[1] + nums[2]
            while (left < right):
                now = nums[i] + nums[left] + nums[right] - target
                min = now if abs(now) < abs(min) else min
                # print(
                #     str(min) + " : " + str(i) + " " + str(nums[i]) + " " +
                #     str(left) + " " + str(nums[left]) + " " + str(right) +
                #     str(nums[right]))
                if now < 0:
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                else:
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
        return min + target
        """
        # 尽管这是一道和之前类似的题,我却错了两次,第一次是因为考虑失当
        # 当相减出现负数的时候的距离判断并不好,加入了abs后才解决
        # 第二次是自己逻辑出现问题,因为计算距离所以now不需要再去和target求距离了
        # 然后还手滑一直与min比较 最后是要记得数组最大下标是了你len-1
        nums = sorted(nums)
        length = len(nums)
        if length < 3:
            return None
        least_delta = nums[0] + nums[1] + nums[2] - target
        for i in range(length - 2):
            delta = nums[i] + nums[i + 1] + nums[i + 2] - target
            if delta > 0:
                if abs(delta) < abs(least_delta):
                    least_delta = delta
                continue
            delta = nums[i] + nums[length - 2] + nums[length - 1] - target
            if delta < 0:
                if abs(delta) < abs(least_delta):
                    least_delta = delta
                continue
            forward, backward = i + 1, length - 1
            delta = nums[i] + nums[forward] + nums[backward] - target
            while backward > forward:
                if delta == 0:
                    return target
                elif delta > 0:
                    backward -= 1
                else:
                    forward += 1
                if abs(delta) < abs(least_delta):
                    least_delta = delta
                delta = nums[i] + nums[forward] + nums[backward] - target
        return (target + least_delta)
        # 他比我好在有一个==0的情况,当相等时这就是最接近的数字了,不用多余比较了
        # 他比我少一个循环,他在最后一次即-1 -2 -3这个相加在前方判断了,不需要执行循环,可能时间会好一点.
        # 他把第一次的0 1 2三个数字加起来作为标准,这样比我给一个最小数好很多


# @lc code=end
