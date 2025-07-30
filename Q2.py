class Solution:
    def insertInMiddle(self,head,data):
        if not head:
            return Node(data)
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        node=Node(data)
        node.next=slow.next
        slow.next=node
        return head
