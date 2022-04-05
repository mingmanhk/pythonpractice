class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"
        
        # store data
        self.data = data
        
        # store reference (next item)
        self.next = None
        return
    
    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False

def addTwoNumbers(l1, l2):
    dummy = cur = ListNode()
    carry = 0

    while l1 or l2 or carry:
        res = carry
        print("l1.val" + l1.val)
        print("l2.val" + l2.val)
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        
        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10

        cur.next = ListNode(val)
       
       l1 = l1.next if l1 else None
       l2 = l2.next if l2 else None
       
    return dummy.next

print(addTwoNumbers([2,4,3],[5,6,4]))