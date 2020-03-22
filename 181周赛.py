"""
给你两个整数数组 nums 和 index。你需要按照以下规则创建目标数组：

    目标数组 target 最初为空。
    按从左到右的顺序依次读取 nums[i] 和 index[i]，在 target 数组中的下标 index[i] 处插入值 nums[i] 。
    重复上一步，直到在 nums 和 index 中都没有要读取的元素。

请你返回目标数组。

题目保证数字插入位置总是存在。

示例 1：

输入：nums = [0,1,2,3,4], index = [0,1,2,2,1]
输出：[0,4,1,3,2]
解释：
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]


"""
# 说实话不知道这题考的是什么.可能是参与题目吧


class Solution:

    def createTargetArray(self, nums, index):
        """
        :type nums,index : List[int]
        :rtype: List[int]
        """
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target


"""
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]):
        target = []
        for n, i in zip(nums, index):
            target = target[:i] + [n] + target[i:]
        return target
        zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
        然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
        想法很巧妙,将对应的东西放在对应的位置,运用了+和:两种运算符,高效简洁
"""