import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def sort_link_remove_duplicate(link_in):
    l = []
    link = copy.deepcopy(link_in)
    for _ in range(link.size()):
        l.append(link.head.value)
        link.head=link.head.next
    
    l = sorted(list(set(l)))
    ret = LinkedList()
    for cell in l:
        ret.append(cell)
    return ret

def union(llist_in_1, llist_in_2):
    llist_1 = sort_link_remove_duplicate(llist_in_1)
    llist_2 = sort_link_remove_duplicate(llist_in_2)

    llist_union = LinkedList()
    while(True):
        if llist_1.head == None and llist_2.head == None:
            break
        elif llist_1.head == None:
            llist_union.append(llist_2.head.value)
            llist_2.head = llist_2.head.next
        elif llist_2.head == None:
            llist_union.append(llist_1.head.value)
            llist_1.head = llist_1.head.next
        elif llist_1.head.value < llist_2.head.value:
            llist_union.append(llist_1.head.value)
            llist_1.head = llist_1.head.next
        elif llist_1.head.value > llist_2.head.value:
            llist_union.append(llist_2.head.value)
            llist_2.head = llist_2.head.next
        else: # llist_1.head.value == llist_2.head.value
            llist_union.append(llist_1.head.value)
            llist_1.head = llist_1.head.next
            llist_2.head = llist_2.head.next
    return llist_union

def intersection(llist_in_1, llist_in_2):
    llist_1 = sort_link_remove_duplicate(llist_in_1)
    llist_2 = sort_link_remove_duplicate(llist_in_2)
    llist_intersection = LinkedList()
    while(True):
        if llist_1.head == None and llist_2.head == None:
            break
        elif llist_1.head == None:
            llist_2.head = llist_2.head.next
        elif llist_2.head == None:
            llist_1.head = llist_1.head.next
        elif llist_1.head.value < llist_2.head.value:
            llist_1.head = llist_1.head.next
        elif llist_1.head.value > llist_2.head.value:
            llist_2.head = llist_2.head.next
        else: # llist_1.head.value == llist_2.head.value
            llist_intersection.append(llist_1.head.value)
            llist_1.head = llist_1.head.next
            llist_2.head = llist_2.head.next
    return llist_intersection

if __name__ == "__main__":
    # Test case 1 -> normal
    """
    test 1
    1 -> 2 -> 3 -> 4 -> 6 -> 9 -> 11 -> 21 -> 32 -> 35 -> 65 -> 
    4 -> 6 -> 21 -> 
    """

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print('test 1')
    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))
    print()

    # Test case 2 -> no interaction
    """
    test 2
    1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 35 -> 65 -> 

    """

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print('test 2')
    print (union(linked_list_3,linked_list_4))
    print (intersection(linked_list_3,linked_list_4))
    print()

    # test case 3 -> completely same
    """
    test 3
    2 -> 3 -> 4 -> 6 -> 23 -> 35 -> 65 -> 
    2 -> 3 -> 4 -> 6 -> 23 -> 35 -> 65 -> 
    """

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [3,2,4,35,6,65,6,4,3,23]
    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print('test 3')
    print (union(linked_list_5,linked_list_6))
    print (intersection(linked_list_5,linked_list_6))
    print()

    # test case 4 -> one is empty
    """
    test 4
    2 -> 3 -> 4 -> 6 -> 23 -> 35 -> 65 -> 

    """
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = []
    for i in element_1:
        linked_list_7.append(i)

    for i in element_2:
        linked_list_8.append(i)

    print('test 4')
    print (union(linked_list_7,linked_list_8))
    print (intersection(linked_list_7,linked_list_8))
    print()