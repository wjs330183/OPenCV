# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#
#
#
#
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
#
#
#  示例 2：
#
#
# 输入：head = [1,2]
# 输出：[2,1]
#
#
#  示例 3：
#
#
# 输入：head = []
# 输出：[]
#
#
#
#
#  提示：
#
#
#  链表中节点的数目范围是 [0, 5000]
#  -5000 <= Node.val <= 5000
#
#
#
#
#  进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
#
#  Related Topics 递归 链表 👍 2632 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, l1: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = None
        p = None
        c = l1
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        return p

    l1: ListNode = {1, 2, 3, 4, 5, 6}
    reverseList(l1)

# leetcode submit region end(Prohibit modification and deletion)

