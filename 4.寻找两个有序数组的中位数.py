#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (37.07%)
# Likes:    2297
# Dislikes: 0
# Total Accepted:    158.5K
# Total Submissions: 427.2K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
#
#
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
#
#
# @lc code=start
class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
            # 为了拿最小的切
        if n == 0:
            raise ValueError
        imin, imax, half_len = 0, m, (m + n + 1) / 2
        # imax拿得最小数组的长度
        while imin <= imax:
            i = int((imin + imax) / 2)
            # i.j公式体现
            j = int(half_len - i)
            if i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
                # 他的起点是每次调整imin来修正i
                # 每次让起始点或结束点到当前位置,修正幅度较大
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    # 小组最大在b组
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    # 小组最大在a组
                    max_of_left = nums1[i - 1]
                else:
                    # 小组最大在两组最大中最大的
                    max_of_left = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return max_of_left
                if i == m:
                    # 大组最小在b组
                    min_of_right = nums2[j]
                elif j == n:
                    # 大组最大在a组
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2.0


# key 题目要求log 即看到log 基本都是二分法
# 1 看题第一想法 归并后找出中间 其实这是一种对中位数概念比较模糊的做法 TC O(m+n) SC O(m+n)
# 2 第二种方法与第一种类似,就是比较,去掉总长/2小的数,最小的就是我们的目标了.
# 所以就比较,每回比一下,从头开始,a1要是比b1大,就a1和b2比,这样在比完了 TC O(m+n) SC O(1)
# 3 这里有个二分法,当有m+n个数字找中间时,先看前k=m+n/2/2(取余)的,这样比一下,两个都看第k个
# 如果小的就整个砍掉.之后再往后比((m+n)/2-k)/2,之后再比较,直到一个没了,剩下的直接取到中位即可
# 如果二分没了还有两条,就比哪个大,或者是偶数情况就比平均值. TC O(log(m+n)) SC O(1)
# 4 极致 中位数即能把族群分为上下两部分的数 我们研究如何最大跨度的切而不影响结果
# 现定义i/j为m/n的中位数,此时有等式 i+j=m-i+n-j 即j=(m+n)/2-i,当式子和为奇数+1(正好取到要的数)
# 同时偶数时会取余所以可以忽略.即合并为这个公式j=(m+n+1)/2-i.同时为了这个公式不为负数.n要大于等于m
# 假设i是最大的的数字(m-1),n是最小的m那么j=m-m+1=1还是正数,那么我们如何处理呢?
# 就是通过找i来判断j,同时ij还有这样一个关系:1 即A大组最小大等于于B小组最大 A[i-1]>B[j]
# 2 B大组最小大等于于A小组最大 B[j-1]>A[i] 当B[j-1]<A[i]时 我们将i调整,放大i,让整个数变小
# A[i-1]<B[j] 将i缩小,整个数变大. 当到达边界或者符合规定的时候,停止搜索ij
# 使用公式直接求解 max(A[i−1],B[j−1]), 当 m+nm + nm+n 为奇数时
# max(A[i−1],B[j−1])+min(A[i],B[j])/2​, 当 m+nm + nm+n 为偶数时
# TC O(min(m,n))  SC O(1)

# @lc code=end
