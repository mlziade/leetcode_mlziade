func maxArea(height []int) int {
    var maxArea int = 0
	var start int = 0
	var end int = len(height) - 1
	for start < end {
		if height[start] == 0 {
			start++
			continue
		}

		if height[end] == 0 {
			end--
			continue
		}

		var aux = calculateArea(height, start, end)
		if aux > maxArea {
			maxArea = aux
		}

		if height[start] < height[end] {
			start++
		} else {
			end--
		}
	}

	return maxArea
}

func calculateArea(height []int, start int, end int) int {
	return (end - start) * min(height[start], height[end])
}