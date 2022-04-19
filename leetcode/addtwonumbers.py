def addTwoNumbers(l1, l2):
    dummy = cur = ListNode()
    carry = 0

    #add carry in case last addition has carry number
    while l1 or l2 or carry:
        res = carry
        print("l1.val" + l1.val)
        print("l2.val" + l2.val)
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        #new digit
        val = v1 + v2 + carry
        # get carry number
        carry = val // 10
        # mod 10
        val = val % 10

        cur.next = ListNode(val)

        #update pointer
        cur=cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

print(addTwoNumbers([2,4,3],[5,6,4]))