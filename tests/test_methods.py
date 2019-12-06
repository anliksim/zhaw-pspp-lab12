import unittest


class ExplainTestSuite(unittest.TestCase):
    """
        Explain results of method calls
    """

    def test_dir_list(self):
        """
            Return all methods of a list
        """
        print('dir([]): ', dir([]))

    def test_dir_dict(self):
        """
            Return all methods of a dict
        """
        print('dir({}): ', dir({}))

    def test_dict_values(self):
        """
            Return list of values of an empty dict
        """
        print('{}.values: ', {}.values)

    def test_dict_values_doc(self):
        """
            Return documentation/description of the method
        """
        print('{}.values.__doc__: ', {}.values.__doc__)


if __name__ == '__main__':
    unittest.main()
