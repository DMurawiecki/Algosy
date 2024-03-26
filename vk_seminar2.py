def task1():
    def hasCycle(head):
        if head is None or head.next is None:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            
        return True

    # Пример для проверки
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    # Создаем связанный список, содержащий петлю
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2 

    result = hasCycle(node1)
    print(result)

# task1()


def task2():    
    def reverseLinkedList(head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head = prev
        return head

    # Пример для проверки
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    # Создаем связанный список для тестирования
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    # Выводим изначальный список
    current = node1
    while current is not None:
        print(current.data)
        current = current.next

    reversed_head = reverseLinkedList(node1)

    # Выводим обратно перевернутый список
    current = reversed_head
    while current is not None:
        print(current.data)
        current = current.next

# task2()

def task3():
    def middleNode(head):
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Пример для проверки
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    # Создаем связанный список для тестирования
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    result = middleNode(node1)
    print(result.data)

# task3()

def task4():
    class ListNode:
        def __init__(self, val):
            self.val = val
            self.next = None

    def removeElements(head, val):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        while cur is not None:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next

    # Пример для проверки
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(6)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(5)
    node7 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    new_head = removeElements(node1, 6)

    # Выводим новый список без элементов со значением 6
    current = new_head
    while current is not None:
        print(current.val)
        current = current.next

# task4()

# HOME TASK
 
def home_task():
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def mergeSortedLists(list1, list2):
        dummy = ListNode()
        current = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        current.next = list1 if list1 is not None else list2
        return dummy.next

    # Пример для проверки
    node1 = ListNode(3)
    node2 = ListNode(6)
    node3 = ListNode(8)

    node4 = ListNode(4)
    node5 = ListNode(7)
    node6 = ListNode(9)
    node7 = ListNode(11)

    node1.next = node2
    node2.next = node3

    node4.next = node5
    node5.next = node6
    node6.next = node7

    new_head = mergeSortedLists(node1, node4)

    # Выводим новый отсортированный список
    current = new_head
    while current is not None:
        print(current.val)
        current = current.next

# home_task()