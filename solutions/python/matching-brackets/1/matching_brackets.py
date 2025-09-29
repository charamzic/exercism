def is_paired(input_string):
    stack = []
    matching_brackets = {")": "(", "]": "[", "}": "{"}
    for char in input_string:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != matching_brackets[char]:
                return False
    return not stack


# Given a string containing brackets `[]`, braces `{}`, parentheses `()`, or any combination thereof, verify that any and all pairs are matched and nested correctly.
# Any other characters should be ignored.
# For example, `"{what is (42)}?"` is balanced and `"[text}"` is not.
