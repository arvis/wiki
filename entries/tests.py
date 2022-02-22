from django.test import TestCase
from .parsers import parse_string


class ParsingTests(TestCase):

    def test_parse_simple_string(self):
        """
        Most simple test case, parse string with url
        """
        test_str = "Framework [Django] is written in [Python] programming language."

        res  = parse_string(test_str)
        expected = 'Framework <a href="django">Django</a> is written in <a href="python">Python</a> programming language.'
        self.assertIs(expected==res , True)

    def test_parse_multiple_same_links(self):
        """
        Correct parsing if the same link is
        """
        test_str = "Framework [Django] is written in [Python] programming language. Monty Python not a snake [Python]"

        res  = parse_string(test_str)
        print(res)
        expected = 'Framework <a href="django">Django</a> is written in <a href="python">Python</a> programming language. Monty Python not a snake <a href="python">Python</a>'
        self.assertIs(expected==res , True)        

    def test_parse_don_parse_with_spaces(self):
        """
        Not parsing if there is space in link
        """
        test_str = "Framework [Django] is written in [Python] programming language. [Monty Python] not a snake [Python]"

        res  = parse_string(test_str)
        expected = 'Framework <a href="django">Django</a> is written in <a href="python">Python</a> programming language. [Monty Python] not a snake <a href="python">Python</a>'
        self.assertIs(expected==res , True)                