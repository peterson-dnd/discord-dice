class DiceComplexityException(Exception):
    """
    Custom exception raised when the combination of dice and sides
    is too large and could exceed system limits.
    """
    def __init__(self, complexity, complexity_limit, message=None):
        self.complexity = complexity
        self.complexity_limit = complexity_limit

        if message is None:
            # Default error message
            self.message = f"The complexity '{complexity}' of this roll is greater than the limit '{complexity_limit}'"
        else:
            self.message = message

        super().__init__(self.message)

    def __str__(self):
        """
        String representation of the exception.
        """
        return self.message
