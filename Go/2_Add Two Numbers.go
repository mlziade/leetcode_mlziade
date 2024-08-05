package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	result := new(ListNode)
	result.Val = 0
	result.Next = nil

	auxL1 := l1
	auxL2 := l2
	auxResult := result

	for {
		if auxL1 != nil {
			auxResult.Val += auxL1.Val
			auxL1 = auxL1.Next
		}
		if auxL2 != nil {
			auxResult.Val += auxL2.Val
			auxL2 = auxL2.Next
		}
		if auxResult.Val >= 10 {
			auxResult.Next = new(ListNode)
			auxResult.Val = auxResult.Val - 10
			auxResult.Next.Val = 1
		}
		if (auxL1 != nil || auxL2 != nil) && auxResult.Next == nil {
			auxResult.Next = new(ListNode)
			auxResult.Next.Val = 0
		}
		auxResult = auxResult.Next
		if auxL1 == nil && auxL2 == nil {
			break
		}
	}

	return result
}
