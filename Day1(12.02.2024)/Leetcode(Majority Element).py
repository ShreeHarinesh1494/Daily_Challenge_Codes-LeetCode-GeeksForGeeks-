Majority Element :
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Solution :(Python)

from collections import Counter 
class Solution(object):
    def majorityElement(self, nums):
        c = Counter(nums).most_common()
        return c[0][0]

        

 
