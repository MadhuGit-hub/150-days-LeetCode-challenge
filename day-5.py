class Solution(object):
 

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_max_val_key(max_element, temp):
            for k,v in temp.items():
                if max_element == v:
                    return k
        temp = {}
        for i in (nums):
            if i not in temp:
                temp[i]= 1
            else:
                temp[i] = temp.get(i) + 1
        max_element  = max(temp.values()) 
        return get_max_val_key(max_element, temp)

