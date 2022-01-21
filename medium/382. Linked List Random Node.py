class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.range = []
        while head:
            self.range.append(head.val)
            head = head.next
        

    def getRandom(self) -> int:
        ans = int(random.random() * len(self.range))
        return self.range[ans]
