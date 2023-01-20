class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.i = 0
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.list_of_list[self.i][self.j]
            if self.j < len(self.list_of_list[self.i]) - 1:
                self.j += 1
            elif self.i <= len(self.list_of_list) - 1:
                self.i += 1
                self.j = 0
            return item
        except:
            raise StopIteration

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        print(flat_iterator_item, check_item)

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
