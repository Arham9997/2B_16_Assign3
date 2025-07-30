class Solution:
    def searchKey(self, n, head, key):
        temp=head
        while(temp):
            if temp.data==key:
                return True
            temp=temp.next
