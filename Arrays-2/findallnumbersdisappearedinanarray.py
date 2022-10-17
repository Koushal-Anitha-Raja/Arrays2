class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #creating a result variable 
        result=[]
        #iterate through the entire array nums
        for i in range(len(nums)):
            #assigning indexx to find the valuye
            index=abs(nums[i])-1
            
            #if it is already less than zero leave it or else change it 
            if nums[index]>0:
                #then multiply it with -1
                nums[index]*=-1
        
        #then go final one pass to find out the missing element
        for j in range(len(nums)):
            #if the value is greater than zero then append the value to result array
            if nums[j]>0:
                result.append(j+1)
                
        return result