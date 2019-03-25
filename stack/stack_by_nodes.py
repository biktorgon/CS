class EmptyStackError(Exception):

    def __init__(self, text):
        self.text = text


class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, x):
        self.length += 1
        new_node = Node(x, None)
        if self.head is None:
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.length == 0:
            raise EmptyStackError('stack is empty')
        self.length -= 1
        current_node = self.head
        self.head = current_node.next

        return current_node.value

    def peek(self):
        if self.length == 0:
            raise EmptyStackError('stack is empty')

        return self.head.value

    def __str__(self):
        if self.head is None:
            return 'Stack []'

        stack_list = list()
        current_node = self.head
        stack_list.append(current_node.value)

        while current_node.next is not None:
            current_node = current_node.next
            stack_list.append(current_node.value)

        return 'Stack {}'.format(stack_list)
