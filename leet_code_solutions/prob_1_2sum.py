
import pdb

def twosum_hashmap(nums, target):
	'''
	input:
	nums	- list of numbers to calc
	target 	- target value
	output:
	[a,b]	- index of required numbers
	'''

	#pdb.set_trace()
	dataset = {}
	for index in range(len(nums)):
		dataset[(nums[index])] = index

	for value in nums:
		if (target - value) in dataset and \
		(value) in dataset \
		and dataset[(value)] != dataset[(target-value)]:
			return [dataset[(value)], dataset[(target-value)]]
	return []

def twosum_hashmap_onepass(nums,target):

	dataset={}
	for index in range(len(nums)):
		if (target - nums[index]) in dataset:
			return [index, dataset[(target-nums[index])]]
		else:
			dataset[(nums[index])] = index



if __name__ == '__main__':
	a = [230,863,916,585,981,404,316,785,88,12,70,435,384,778,887,755,740,337,86,92,325,422,815,650,920,125,277,336,221,847,168,23,677,61,400,136,874,363,394,199,863,997,794,587,124,321,212,957,764,173,314,422,927,783,930,282,306,506,44,926,691,568,68,730,933,737,531,180,414,751,28,546,60,371,493,370,527,387,43,541,13,457,328,227,652,365,430,803,59,858,538,427,583,368,375,173,809,896,370,789]
	b = twosum_hashmap(a,542)
	print(b)
	print(a[b[0]], a[b[1]])


