package main

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	var missingIndex int
	var missingExist bool

	var index int
	var value int
	for index, value = range nums {
		missingIndex, missingExist = m[target-value]
		if missingExist {
			awnsear := []int{index, missingIndex}
			return awnsear
		}
		m[value] = index
	}
	awnsear := []int{index, missingIndex}
	return awnsear
}
