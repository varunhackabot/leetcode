# -*- coding: utf-8 -*-
"""Bit_Manipulation-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1chR3jtzMwHIEX9C_sdO5NZVRrJwveWCT
"""

#1342. Number of Steps to Reduce a Number to Zero
#SOLUTION
class Solution:
    def numberOfSteps(self, num: int) -> int:
        a = 0
        while(num!=0):
            if(num%2==0):
                num = num//2
                a+=1
            elif(num%2!=0):
                num-=1
                a+=1
        return(a)

#136. Single Number
#SOLUTION
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = []
        b = 0
        a = Counter(nums)
        for value in a:
            if(a[value]==1):
                b = value
        return(b)
