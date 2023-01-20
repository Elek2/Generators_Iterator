class FlatIterator:

    def __init__(self, list_of_list):

        def flat(nestedlist):
            res = []
            for e in nestedlist:
                if type(e) is not list:
                    res.append(e)
                else:
                    res.extend(flat(e))
            return res

        self.list_of_list = flat(list_of_list)


    def __iter__(self):
        return self

    def __next__(self):
        if self.list_of_list:
            return self.list_of_list.pop(0)
        else:
            raise StopIteration


def test_1():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_1()
