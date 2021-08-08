

class Node():
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def next(self):
        return self.next_node

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self.value)


class LinkedList():
    def __init__(self, root):
        self.root = root

    @classmethod
    def create_linked_list(cls, vals):
        li = []
        for val in vals:
            n = Node(val)
            if li:
                li[-1].next_node = n
            li.append(n)
        return cls(li[0])

    def find_mid(self):
        cur = self.root
        i = 0
        memo = {}
        while cur is not None:
            print(cur.value)
            memo[i] = cur
            cur = cur.next()
            i += 1

        print(i, memo)
        return memo[i // 2 if i % 2 != 0 else i//2 - 1]


if __name__ == '__main__':
    inp = range(1, 5)
    linked = LinkedList.create_linked_list(inp)
    print(linked.root.next_node.value)
    mid_node = linked.find_mid()
    print('mid node val:', mid_node.value)
