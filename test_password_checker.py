
import unittest
from password_checker import analyze_password


class TestPasswordChecker(unittest.TestCase):

    def test_short_password(self):
        score, rating, suggestions = analyze_password("abc")

        self.assertEqual(rating, "Weak")
        self.assertTrue(len(suggestions) > 0)

    def test_moderate_password(self):
        score, rating, suggestions = analyze_password("Abcdef12")

        self.assertEqual(score, 4)
        self.assertEqual(rating, "Moderate")

    def test_strong_password(self):
        score, rating, suggestions = analyze_password(
            "River!Cobalt7Mango"
        )

        self.assertEqual(score, 6)
        self.assertEqual(rating, "Strong")
        self.assertEqual(suggestions, [])

    def test_lowercase_only(self):
        score, rating, suggestions = analyze_password("abcdefgh")

        self.assertEqual(rating, "Weak")
        self.assertIn("Add uppercase letters.", suggestions)

    def test_uppercase_only(self):
        score, rating, suggestions = analyze_password("ABCDEFGH")

        self.assertIn("Add lowercase letters.", suggestions)

    def test_numbers_and_symbols(self):
        score, rating, suggestions = analyze_password("abc12345!")

        self.assertIn("Add uppercase letters.", suggestions)

    def test_empty_password(self):
        score, rating, suggestions = analyze_password("")

        self.assertEqual(score, 0)
        self.assertEqual(rating, "Weak")
        self.assertTrue(len(suggestions) > 0)


if __name__ == "__main__":
    unittest.main()
