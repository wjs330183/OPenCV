# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
import random
from typing import List

import numpy as np


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i, hashmap.get(target - num)]
            hashmap[num] = i


def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    step, maxPose, end = 0, 0, 0
    for i in range(n - 1):
        if maxPose >= i:
            maxPose = max(i + nums[i], maxPose)
        if i == end:
            end = maxPose
            step += 1

    return step


def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    days = [0] * len(temperatures)
    stack = []
    for day, temperature in enumerate(temperatures):
        while stack and temperature > temperatures[stack[-1]]:
            prev_index = stack.pop()
            days[prev_index] = day - prev_index
        stack.append(day)
    return days


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    n1 = len(l1) - 1
    n2 = len(l2) - 1
    ans = 0
    i = n1
    while i >= n2:
        for j in range(n2, -1, -1):
            ans += (l1[i] + l2[j]) * np.power(10, n2 - j)
            i -= 1
    while i > -1:
        ans += l1[i] * np.power(10, n1 - i)
        i -= 1
    ans = list(map(int, str(ans)))
    lists = []
    n = len(ans)
    for n in range(len(ans) - 1, -1, -1):
        lists.append(ans[n])
    return lists


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    t = 0
    if x < 0:
        t = 0 - x
    else:
        t = x
    ans = list(map(int, str(t)))
    n = len(ans) - 1
    y = 0
    for n in range(len(ans) - 1, -1, -1):
        y += ans[n] * 10 ** n
    if x < 0:
        t = -y
    else:
        t = y
    if t < (-1 * 2 ** 31) or t > (1 * 2 ** 31 - 1): return 0
    return t


def rev(x):
    digit = x % 10
    x /= 10
    if x < 1 and x > -1:
        return x
    rev(x) * 10 + digit


def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    length = len(flowerbed)
    step = []
    i = 0
    if flowerbed[0] == 0:
        step.append(0)
    while n != 0 and i < length:
        while len(step) < 3 and i < length:
            if flowerbed[i] == 1:
                i += 1
                step = []
                break
            step.append(flowerbed[i])
            i += 1
        if len(step) == 3 or (len(step) == 2 and i == (length)):
            step = step[:1]
            n -= 1

    if n == 0:
        return True
    else:
        return False


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    maxlength, k, smax = 0, -1, {}
    for i, c in enumerate(s):
        if c in smax:
            k = smax[c]
            smax[c] = i
        else:
            smax[c] = i
            maxlength = max(maxlength, i - k)
    return maxlength


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    infinty = 2 ** 40
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    median1, median2 = 0, 0
    while left <= right:
        i = (left + right) // 2
        j = (m + n + 1) // 2 - i
        nums_im1 = (-infinty if i == 0 else nums1[i - 1])
        nums_i = (infinty if i == m else nums1[i])
        nums_jm1 = (-infinty if j == 0 else nums2[j - 1])
        nums_j = (infinty if j == n else nums2[j])
        if nums_im1 <= nums_j:
            median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
            left = i + 1
        else:
            right = i - 1
    return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    n = None
    p = None
    c = head
    while c:
        n = c.next
        c.next = p
        p = c
        c = n
    return p


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Solution.twoSum([3, 2, 4], 6)
    # print_hi('PyCharm')
    # nums = [2, 3, 1, 1, 4]
    # print(jump(nums))
    # temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    # print(dailyTemperatures(temperatures))
    # l1, l2 = [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]
    # l1, l2 = [2, 4, 3], [5, 6, 4]
    # l1, l2 = [2, 4, 3], [5, 6, 4]
    # print(addTwoNumbers(l1, l2))
    # x = random.randint(-1 * math.pow(2, 32), 1 * math.pow(2, 32) - 1)
    # print(x)
    # print(reverse(1534236469))
    # flowerbed, n = [1, 0, 0], 1
    # print(canPlaceFlowers(flowerbed, n))
    # s = 'tmmzuxt'
    # print(lengthOfLongestSubstring(s))
    # l1, l2 = [2, 3, 4], [5, 6, 7]
    # print(findMedianSortedArrays(l1, l2))
    l = [1, 2, 3, 4, 5]
    print(reverseList(l))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
