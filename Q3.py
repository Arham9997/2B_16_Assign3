def deleteNode(head,data):
    if data==1:
        return head.next
    curr=head
    for i in range(data-2):
        curr=curr.next
    curr.next=curr.next.next
    return head
