import os.path


def get_input(day, bTest=False):
    filename = str(day) + ('test' if bTest else '') + '.txt'
    input_path = os.path.join('inputs', filename)
    with open(input_path) as f:
        return [int(x) for x in f.read().splitlines()[0]]


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self, val_list):
        self.head = None
        prev_node = None
        for val in val_list:
            new_node = Node(val)
            if not self.head:
                self.head = new_node
            if prev_node:
                prev_node.next = new_node
            prev_node = new_node
        prev_node.next = self.head

    def insert_node_after(self, node, node_to_insert):
        next_node = node.next
        node.next = node_to_insert
        node.next.next = next_node

    def remove_node_after(self, node):
        node_to_remove = node.next
        node.next = node.next.next
        return node_to_remove

    def get_node_by_value(self, value):
        current_node = self.head
        while True:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
            if current_node is self.head:
                break
        return None

    def remove_n_nodes_after_head(self, n):
        removed_nodes = []
        for _ in range(n):
            removed_nodes.append(self.remove_node_after(self.head))
        return removed_nodes

    def get_highest_value(self):
        max_val = -1
        current_node = self.head
        while True:
            if current_node.value > max_val:
                max_val = current_node.value
            current_node = current_node.next
            if current_node is self.head:
                break
        return max_val

    def get_destination_cup(self):
        destination_cup_value = self.head.value
        destination_cup_node = None
        while not destination_cup_node:
            destination_cup_value -= 1
            if destination_cup_value < 1:
                destination_cup_value = self.get_highest_value()
            destination_cup_node = self.get_node_by_value(destination_cup_value)
        return destination_cup_node

    def play(self, p2=False):
        removed_cups = self.remove_n_nodes_after_head(3)
        destination_cup = self.get_destination_cup()
        insert_after = destination_cup
        for cup in removed_cups:
            self.insert_node_after(insert_after, cup)
            insert_after = cup
        self.head = self.head.next

    def play_n_times(self, n):
        for i in range(n):
            self.play()

    def get_values(self):
        current_node = self.head
        out = []
        while True:
            out.append(current_node.value)
            current_node = current_node.next
            if current_node is self.head:
                break
        return out

    def get_result(self):
        while self.head.value is not 1:
            self.head = self.head.next
        lst = self.get_values()[1:]
        return ''.join([str(x) for x in lst])


def part1(data):
    cups = LinkedList(data)
    cups.play_n_times(100)
    return cups.get_result()


def part2(data):
    # after the first few rounds, when we get the max +1, the destination cup will never be ahead. (at least not for 1 million rounds)
    # in fact, it will always add the 3 cups right after the last 3 cups, because the new destination cup will always be the 3rd cup of last time
    # so I think the two nodes after 1 will not change at all until 1 million is reached.
    # maybe we could just keep an index of where the insertions began, a count, and a current max/
    # what happens when we go over after 1 mil ?
    # well hmm
    # [2,1,X,3] => {[1,X4,X5]}, [2, X, 3] -> [2, X, 1, X4, X5, 3]
    # as soon as we reach the X, the 3 nodes will be put after the biggest available X that is already out, similar to the first one.
    #  
    # what about a magic node
    # when we call remove_n_nodes_after_head on it it would create a new node
    # when next is called on it it just increments its internal range, only give back the head after the mil.
    
    pass


if __name__ == '__main__':
    DAY = 23
    input_data = get_input(DAY, False)
    print(part1(input_data))
    print(part2(input_data))
