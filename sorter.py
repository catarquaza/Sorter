"""
1. sort number array numerically - ascending
2. same as above but descending
3. sort tuple lexographically (both ways)
4. extract numbers from tuple
"""


class Sorter:
    def __init__(self, name):
        self.array = []
        self.name = name
        pass

    def set_array(self, array):
        self.array = array

    def get_ascending(self):
        num_items = len(self.array)
        x = 0
        while True:
            if self.array[x + 1] < self.array[x]:
                index = x + 1
                val = self.array[index]
                self.array.remove(val)
                self.array.insert(x, val)
                x = -1
            x += 1
            if x > num_items - 2:
                break
        return self.array


def main():
    print("start test")

    # test ascending array of numbers
    input = [3, 4, 2, 1]
    sorter = Sorter("list 1")
    sorter.set_array(input)
    assert sorter.get_ascending() == [1, 2, 3, 4]

    # test ascending with duplicaes
    input = [3, 4, 2, 1, 1, 1]
    sorter = Sorter("list 1")
    sorter.set_array(input)
    assert sorter.get_ascending() == [1, 1, 1, 2, 3, 4]

    # test descending array of numbers


main()
