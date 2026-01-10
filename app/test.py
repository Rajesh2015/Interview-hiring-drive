import unittest

class TestSubsequences(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_basic_string(self):
        s = "abc"
        result = self.sol.subsequences(s)
        expected = {"", "a", "b", "c", "ab", "ac", "bc", "abc"}
        self.assertEqual(set(result), expected)

    def test_single_character(self):
        s = "a"
        result = self.sol.subsequences(s)
        expected = {"", "a"}
        self.assertEqual(set(result), expected)

    def test_empty_string(self):
        s = ""
        result = self.sol.subsequences(s)
        expected = {""}
        self.assertEqual(set(result), expected)

    def test_length(self):
        s = "abcd"
        result = self.sol.subsequences(s)
        self.assertEqual(len(result), 2 ** len(s))

    def test_duplicate_characters(self):
        s = "aa"
        result = self.sol.subsequences(s)
        # duplicates are expected in output
        self.assertEqual(len(result), 4)


if __name__ == "__main__":
    unittest.main()
