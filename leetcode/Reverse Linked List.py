

def reverseList(head: [ListNode]):
    def rec(prev, cur):
        if not cur:
            return prev
        tail = rec(cur, cur.next)
        cur.next = prev
        return tail
    return rec(None, head)

print(reverseList([1,2]))