class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1=set(nums1) 
        set2=set(nums2) 
        list_1=list(set1)
        list_2=list(set2)
        Dict={}
        for i in list_1 : 
            Dict[i]=1 

        for J in set2 : 
            if Dict.get(J,0)==1 :
                list_1.remove(J)
                list_2.remove(J) 
        res=[] 
        res.append(list_1) 
        res.append(list_2) 
        return res 


            
            