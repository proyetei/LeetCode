class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create a hashmap
        myDict = {}
        # target - value = difference
        # difference = 9 -2 = 7, 7 is the number we are looking for
        # we return the difference and value
        for i in range(len(nums)):
            val = nums[i]
            difference = target - val  # 7
            # search through hash map
            if difference in myDict:  # search if difference exists in hash map
                return (i, myDict[difference])
            else:
                myDict[val] = i


input_list = [1, 2, 3, 4, 5]
ob1 = Solution()
print(ob1.twoSum(input_list, 4))
