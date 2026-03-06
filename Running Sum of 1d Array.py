#Brute Force / Intuition
def runningSum1(self, nums: List[int]) -> List[int]:
	answer = [] #array to keep track of our answer
	for i in range(len(nums)): #iterate through all the elements in nums
		runningSum = 0 #this will keep track of the running sum up to index i
		for j in range(i+1): 
			runningSum += nums[j] #sum all the elements leading up to nums[i]
		answer.append(runningSum) #add the sum to our answer array
	return answer

#Time Optimization (initial sum known, add each prevous running sum to current number)
def runningSum2(self, nums: List[int]) -> List[int]:
	runSum = [nums[0]] #our answer array starts with nums[0], which is the 0th running sum
	for i in range(1,len(nums)):
		runSum.append(runSum[i-1]+nums[i]) #the running sum up to index i is the sum of nums[i] and the running sum up to index i-1
	return runSum

#Space Optimization (destroys original nums array and inputed arguments)
def runningSum3(self, nums: List[int]) -> List[int]:
	for i in range(1,len(nums)):
		nums[i] = nums[i-1] + nums[i]
	return nums
