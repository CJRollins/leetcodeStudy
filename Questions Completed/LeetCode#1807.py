class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        lookup = dict(knowledge)
        result = []
        start = None 

        for index, value in enumerate(s):
            if value == '(':
                start = index + 1

            elif value == ')':
                end = index
                extracted = s[start:end]
                replacement = lookup.get(extracted, "?")
                result.append(replacement)

                start = None  # reset parse string

            elif start is None:
                # Copy ordinary text outside brackets.
                result.append(value)

        return "".join(result)