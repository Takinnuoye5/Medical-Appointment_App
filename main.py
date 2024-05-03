from fastapi import FastAPI, Header
from Routers import appointment, doctor, patient
from fastapi import HTTPException
from fastapi.responses import Response
from typing import Annotated


app = FastAPI()


@app.get("/", status_code=200)
def home():
    return {"message": "hello welcome to the hospital"}


@app.get("/headers")
async def get_header(user_agent: Annotated[str | None, Header()] = None,
                     content_type: Annotated[str | None, Header()] = None,
                     ):
    print(user_agent)
    print(content_type)
    return {"User-Agent": user_agent}

app.include_router(patient.router, prefix="/patient", tags=["patient"])
app.include_router(doctor.router, prefix="/doctor", tags=["doctor"])
app.include_router(appointment.router, prefix="/appointment", tags=["appointment"])



# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         result = 0

#         for i in range(len(s)):
#             if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
#                 result -= roman[s[i]]
#             else:
#                 result += roman[s[i]]

#         return result
# s = Solution()
# print(s.romanToInt("III"))


# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1

#         while left <= right:
#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return left

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l, r = 0, 1
#         maxP = 0

#         while r < len(prices):
#             if prices[l] < prices[r]:
#                 maxP = max(maxP, prices[r] - prices[l])
#             else:
#                 l = r
#             r += 1

#         return maxP

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         prevMap = {}
#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n] = i
#         return []

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         cur = dummy
#         carry = 0
#         while l1 or l2 or carry:
#             v1 = l1.val if l1 else 0
#             v2 = l2.val if l2 else 0
#             val = v1 + v2 + carry
#             carry = val // 10
#             val = val % 10
#             cur.next = ListNode(val)
#             cur = cur.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         return dummy.next

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         one, two = 1, 1

#         for i in range(n - 1):
#             temp = one
#             one = one + two
#             two = temp

#         return one


    
    