from unittest import TestCase, main


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)

class IntegerListTest(TestCase):
    def test_is_initialized_correctly_without_data(self):
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_correctly_with_wrong_type_data(self):
        integer = IntegerList("data", 6.45, 6.66)
        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_correctly_with_integer_data(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)

    def test_get_data(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)

        result = integer.get_data()
        self.assertEqual([5], result)

    def test_add_method_incorrect_data_raises(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)

        with self.assertRaises(ValueError) as ex:
            integer.add("asd")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_correct_data_adds_element(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)

        integer.add(3)
        self.assertEqual([5, 3], integer._IntegerList__data)

    def test_remove_el_removes_the_element(self):
        integer = IntegerList(5)
        integer.remove_index(0)

        self.assertEqual([], integer._IntegerList__data)

    def test_remove_invalid_index_raises(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_returns_element_at_the_removed_index(self):
        integer = IntegerList(5)
        result = integer.remove_index(0)
        self.assertEqual(5, result)

    def test_get_with_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.get(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_valid_index_return_element(self):
        integer = IntegerList(5)
        result = integer.get(0)

        self.assertEqual(5, result)

    def test_insert_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.insert(3, 4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_invalid_data_type_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(ValueError) as ex:
            integer.insert(0, 4.3)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_adds_element(self):
        integer = IntegerList(5)

        integer.insert(0,5)
        self.assertEqual([5, 5], integer._IntegerList__data)

    def test_get_biggest(self):
        integer = IntegerList(5, -2, 1, 100, -8, 4, 61)
        result = integer.get_biggest()
        self.assertEqual(100, result)

    def test_get_index(self):
        integer = IntegerList(5, -2, 1, 100, -8, 4, 61)

        result = integer.get_index(-2)
        self.assertEqual(1, result)

        result = integer.get_index(4)
        self.assertEqual(5, result)


if __name__ == "__main__":
    main()