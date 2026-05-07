"""
Prompt:
A frog is hopping around a chessboard, always from the center of one square to the center of another square. Each square has side length 1, but the board itself is not necessarily 8-by-8. Instead, it’s N-by-N, where N is some large whole number.

Every jump the frog makes must be the same distance, which we’ll call L. The frog wants to make four jumps such that:

--Rule 1: After the fourth jump, the frog has returned to its starting square.

--Rule 2: The frog visits a total of four distinct squares along the way, including the square on which it starts (and also stops).

--Rule 3: The path the frog takes is not a square loop.

--Rule 4: The frog is never on a square that is diagonal (i.e., a bishop’s move away) or horizontal/vertical (i.e., a rook’s move away) from the starting square.

What is the smallest jumping distance L for which this is possible?
"""


def check_rule_4_compliance(position):
    if abs(position[0]) == abs(position[1]):
        return False
    elif position[0] == 0:
        return False
    elif position[1] == 0:
        return False
    else:
        return True

print(check_rule_4_compliance((2,-2)))

