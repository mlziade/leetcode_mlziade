func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
    var array []int = reverse_int_as_array(x)
	for i := 0; i < len(array)/2; i++ {
		if array[i] != array[len(array)-1-i] {
			return false
		}
	}
	return true
}

func reverse_int_as_array(x int) []int {
	var result []int
	for x != 0 {
		result = append(result, x%10)
		x /= 10
	}
	return result
}