# 1464. Maximum Product of Two Elements in an Array

class Solution:
  def maxProduct(self, nums):
    max1 = 0
    max2 = 0

    for num in nums:
      if num > max1:
        max2, max1 = max1, num
      elif num > max2:
        max2 = num

    return (max1 - 1) * (max2 - 1)
