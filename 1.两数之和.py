#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (47.79%)
# Likes:    7827
# Dislikes: 0
# Total Accepted:    892K
# Total Submissions: 1.9M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]ls
#
#
#

# @lc code=start


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]               
        """
        # 先扫一边,相同的找出来
        # 找出所有的两个的组合 然后用和减去参数一,对比剩下所有不重复的目标
        # 如果相等就村到list
        dct = {} #这个是空的
        for i, n in enumerate(nums):
            if target - n in dct:
                return [dct[target - n], i]
            dct[n] = i  #每次放里一个,这样就不存在比较两遍
# @lc code=end

# 官方推介了三种方法,第一种两次遍历,直接返回i j
# TC:O(n2) SC:O(1)

# 第二种方式使用hashmap, 将数据作为key,将下标作为value.
# 使用map.containsKey(complement) && map.get(complement) != i
# TC:O(n) SC:O(n)

# 第三个方法同样使用hashmap,不过使用了一次遍历就ok了
# 与第二种不同是第二种从一开始就先循环一次做好hashmap,而这个是在每一次循环中插入
# 当map里一个元素时,没有匹配目标.多个元素时可以判断匹配了.当插入与之前有匹配即找出答案
# TC:O(n) SC:O(n)

# python小方法 : 列表.count()
# 列表.index(x,i+1)是从num1后的序列后找num2
# 关于[:i]：这是切片操作，在下标 i 之前的元素都保留,
# 适用于Python中的list(也就是数组)，也适用于numpy科学结构(array等)。
# 因为python有in操作,所以直接遍历一次,有目标直接找出即可
# 但是这样操作属于查询两遍,1查找了2,到2又查找了1,所以每次i查询[:i]即类似之前说的第二种方式
# 之后需要避免查两次行为 引入hashmap即python字典即可解决.
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标
