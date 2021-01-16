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
        self.record = [None] * (len(val_list) + 1)
        self.removed_cups = []
        self.head = None
        prev_node = None
        for val in val_list:
            new_node = Node(val)
            self.record[val] = new_node
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

    def remove_n_nodes_after_head(self, n):
        removed_nodes = []
        for _ in range(n):
            removed_nodes.append(self.remove_node_after(self.head))
        return removed_nodes

    def get_node_by_value(self, value):
        current_node = self.head
        while True:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
            if current_node is self.head:
                break

    # def get_highest_value(self):
    #     max_val = -1
    #     current_node = self.head
    #     while True:
    #         if current_node.value > max_val:
    #             max_val = current_node.value
    #         current_node = current_node.next
    #         if current_node is self.head:
    #             break
    #     return max_val

    # def get_highest_available_cup(self, val):
    #     for i in range(4):
    #         if val < -1:
    #             val = len(self.record) - 1
    #         if val in self.removed_cups:
    #             val -= 1
    #         else:
    #             return self.record(val)
    #     raise Exception

    def get_destination_cup(self):
        destination_cup_value = self.head.value
        for i in range(4):
            destination_cup_value -= 1

            if destination_cup_value < 1:
                destination_cup_value = len(self.record) - 1

            candidate = self.record[destination_cup_value]
            if candidate in self.removed_cups:
                continue
            else:
                return candidate
        raise Exception

    def play(self):
        self.removed_cups = self.remove_n_nodes_after_head(3)
        destination_cup = self.get_destination_cup()
        insert_after = destination_cup
        for cup in self.removed_cups:
            self.insert_node_after(insert_after, cup)
            insert_after = cup
        self.removed_cups = []
        self.head = self.head.next

    def play_n_times(self, n):
        for _ in range(n):
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
    data_copy = data[:]
    for i in range(max(data_copy) + 1, 1000000 + 1):
        data_copy.append(i)
    cups = LinkedList(data_copy)
    cups.play_n_times(10000000)
    cup_1 = cups.record[1]
    return cup_1.next.value * cup_1.next.next.value


if __name__ == '__main__':
    DAY = 23
    input_data = get_input(DAY, False)
    print(part1(input_data))
    print(part2(input_data))
