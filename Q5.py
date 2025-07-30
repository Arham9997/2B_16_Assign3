class Solution:
    def getKthFromLast(self, head, k):
        c=0
        d=0
        prev=head
        while(head):
           c+=1
           head=head.next
        while(prev):
            d+=1
            if c==k:
                return prev.data
            prev=prev.next
            if d==(c-k):
                return prev.data
        return -1
