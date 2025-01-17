class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_every_k_elements(head, k):

    if k <= 1 or head is None:
        return head

    curr, prev = head, None

    while True:
        prev_last = prev
        curr_last = curr

        i = 0
        while curr and i < k:
            curr.next, prev, curr = prev, curr, curr.next
            i += 1

        if prev_last:
            prev_last.next = prev
        else:
            head = prev

        curr_last.next = curr

        if curr is None:
            break
        prev = curr_last

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()


main()
