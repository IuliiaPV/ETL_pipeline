import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from src.transform import identify_and_drop_duplicates


class TestIdentifyAndDropDuplicates(unittest.TestCase):

    def test_identify_and_drop_duplicates(self):
        """
        Test that the definition removes duplicates
        """

        d = pd.DataFrame({'col1': [1, 2, 1], 'col2': [3, 4, 3]})

        result = identify_and_drop_duplicates(d)
        expected_result = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        assert_frame_equal(result, expected_result)

    def test_no_duplicates(self):
        """
        Test that the definition removes duplicates
        """

        d = pd.DataFrame({'col1': [1, 2, 2], 'col2': [3, 4, 3]})

        result = identify_and_drop_duplicates(d)

        assert_frame_equal(result, d)


if __name__ == '__main__':
    unittest.main()
