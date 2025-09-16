class Solution:
    def detectLoop(self, head):
        _set = set()
        detect = False
        while head:
            if head not in _set:
                _set.add(head)
                head = head.next
            else:
                detect = True
                break
        return detect
