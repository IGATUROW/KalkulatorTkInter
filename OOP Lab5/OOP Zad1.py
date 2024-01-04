import unittest

WHITE_COLOR = "white"
BLACK_COLOR = "black"
class Pawn:
    def __init__(self, position, color=WHITE_COLOR):
        self.position = position
        self.color = color


    @staticmethod
    def parse_position(position):
        return (ord(position[0]) - ord("a") + 1), int(position[1])
    def can_move(self, position):
        if self.position == position:
            return False
        x_start, y_start = self.parse_position(self.position)
        x_end, y_end = self.parse_position(position)
        if self.color == WHITE_COLOR:
            direction = 1
            y_starting_position = 7
        else:
            pass
        # if x_start != x_end:
        #     return False
        # if y_start + 1 * direction

        return self.position == position


class ChessTest(unittest.TestCase):
    def test_False(self):
        self.assertFalse(False)

    def test_Pawn_have_color(self):
        pawn = Pawn("e4", WHITE_COLOR)
        self.assertEquals

    def test_position_paser_e4_is_54(self):
        pawn = Pawn("a1")
        self.assertEquals((1,1), pawn.parse_position())

    def test_position_a1_is_11(self):
        pawn = Pawn("a")

    def test_position_paser_h8_is_88(self):
        pass

    def test_Pawn_cannot_move_to_same_position(self):
        pawn = Pawn

    def test_white_Pawn_move_one_field(self):
        pawn = Pawn("e2", WHITE_COLOR)
        self.assertTrue(pawn.can_move("e3"))
        self.assertTrue(pawn.can_move("e4"))



def main():
    unittest.main()


if __name__ == "__main__":
    main()