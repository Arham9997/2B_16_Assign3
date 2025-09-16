class Solution:
    def removeLoop(self, head):
        _set = set()
        _removed = False
        prev = head
        while head:
            if head not in _set:
                _set.add(head)
                prev = head
                head = head.next
            else:
                prev.next = None
                _removed = True
                break
        return _removed
