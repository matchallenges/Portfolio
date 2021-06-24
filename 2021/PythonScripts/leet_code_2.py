# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):

        str_list1 = [str(i) for i in l1]
        str_list2 = [str(i) for i in l2]

        l1_joined = ''.join(str_list1)
        l2_joined = ''.join(str_list2)

        l1_joined_int = int(l1_joined)
        l2_joined_int = int(l2_joined)

        sum_of_two_lists = l1_joined_int + l2_joined_int

        string_of_final_number = str(sum_of_two_lists)

        string_of_final_number_reversed = string_of_final_number[::-1]

        answer = [int(i) for i in string_of_final_number_reversed]

        return answer


        

solution = Solution()

print(solution.addTwoNumbers([2, 4, 3, 5, 6, 2, 3], [5, 6, 4]))