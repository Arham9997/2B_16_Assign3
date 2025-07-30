class Solution:
    def insertAtEnd(self,head,data):
        if not head:
            return Node(data)
        else:
            curr=head
            while curr.next:
                curr=curr.next
            curr.next=Node(data)
        return head
