#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (36.86%)
# Likes:    4038
# Dislikes: 0
# Total Accepted:    356.1K
# Total Submissions: 965.6K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = xx
#         self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a, b, p, carry = l1, l2, None, 0
        while a or b:
            val = (a.val if a else 0) + (b.val if b else 0) + carry
            carry, val = val / 10 if val >= 10 else 0, val % 10
            p, p.val = a if a else b, val
            a, b = a.next if a else None, b.next if b else None
            p.next = a if a else b
        if carry:
            p.next = ListNode(carry)
        return l1
        # 这题挺简单的,就和计算机加法器类似
        # 但是难点在于ListNode如何运用.就是一个链表
        # 好久没用next什么了 这个里面 每次赋值之前的if/else判断值得学习
        # while a or b 也很有 oj 感觉
        # 最后一个if 是为了防止进位的 三位数进位到四位数的意思
        #


# @lc code=end
