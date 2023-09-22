class Solution:
    def is_valid_coordinate(s):
        if s[0] != '(' or s[-1] != ')':
            return False

        s = s[1:-1]
        parts = s.split(',')

        if len(parts) != 2:
            return False

        x_str, y_str = parts[0], parts[1]

        if x_str[0] == ' ' or y_str[0] == ' ' or x_str[-1] == ' ' or y_str[-1] == ' ':
            return False

        if x_str[0] == '+' or x_str[0] == '-':
            x_str = x_str[1:]

        if y_str[0] == '+' or y_str[0] == '-':
            y_str = y_str[1:]

        if x_str == "" or y_str == "":
            return False

        if x_str[-1] == '.' or y_str[-1] == '.':
            return False

        if x_str != '0' and x_str[0] == '0' and x_str[1] != '.':
            return False

        if y_str != '0' and y_str[0] == '0' and y_str[1] != '.':
            return False

        if not x_str.replace('.', '', 1).isdigit() or not y_str.replace('.', '', 1).isdigit():
            return False

        x = float(parts[0])
        y = float(parts[1])

        if -90 <= x <= 90 and -180 <= y <= 180:
            return True
        else:
            return False

    def funcValidPairs(inputStr):
        res = []
        for coordinate in inputStr:
            is_valid = Solution.is_valid_coordinate(coordinate)
            if is_valid:
                res.append("Valid")
            else:
                res.append("Invalid")
        return res

coordinates = [
    "(90,180)",
    "(+90,+180)",
    "(90.,180)",
    "(90.0,180.1)",
    "(85S,95W)",
    "(+0,180)",
    "(090,180)",
    "(9.0,180)",
    "(+9.0,180)",
    "(0+9.0,+0)",
    "(0.0,+0)",
    "(+90,+180)",
    "(+90,+180)",
    "(20,280)",
    "(90,180)",
    "(90,180)"
]

print(Solution.funcValidPairs(coordinates))