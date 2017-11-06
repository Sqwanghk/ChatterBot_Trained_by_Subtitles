# -*- coding: utf-8 -*-
from chatterbot.comparisons import Comparator


class LevenshteinRatio(Comparator):
    """
    Compare two statements based on the Levenshtein ratio
    of each statement's text.

    """

    def compare(self, statement, other_statement):
        """
        Compare the two input statements.

        :return: The percent of similarity between the text of the statements.
        :rtype: float
        """
        import sys

        # Use python-Levenshtein if available
        from Levenshtein import ratio
            
        # Return 0 if either statement has a falsy text value
        if not statement.text or not other_statement.text:
            return 0

        # Get the lowercase version of both strings
        statement_text = str(statement.text.lower())
        other_statement_text = str(other_statement.text.lower())

        similarity = ratio( statement_text, other_statement_text )

        return similarity

levenshtein_ratio = LevenshteinRatio()