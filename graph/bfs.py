from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.ribs = []


class BSF:
    def __init__(self):
        self.nodes = []
        self.queue = deque()
        self.visited = []

    def add_node(self, nodes=None):
        if nodes is None:
            return
        self.nodes.extend(nodes)

    def add_ribs(self, node, new_ribs):
        if not isinstance(new_ribs, list):
            return
        node.ribs.extend(new_ribs)

    def add_to_queue(self, node):
        if node not in self.nodes:
            return
        for rib in node.ribs:
            self.queue.append(rib)

    def find(self, start_node, goal_node):
        if start_node not in self.nodes:
            return

        self.add_to_queue(start_node)
        while self.queue:
            node = self.queue.popleft()
            if node in self.visited:
                continue
            if node == goal_node:
                return node
            self.visited.append(node)
            self.add_to_queue(node)
        return 'Not found'

        return None

    def reset(self):
        self.queue.clear()
        self.visited.clear()
