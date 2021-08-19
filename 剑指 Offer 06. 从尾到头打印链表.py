class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return a[::-1] #从末尾提取元素