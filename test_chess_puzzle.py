import pytest
from chess_puzzle import *


def test_location2index1():
    assert location2index("e2") == (5,2)

def test_location2index2():
    assert location2index("z26") == (26,26)

def test_location2index3():
    with pytest.raises(ValueError):
        location2index("ee2")

def test_location2index4():
    with pytest.raises(ValueError):
        location2index("e222")

def test_location2index5():
    with pytest.raises(ValueError):
        location2index("2e")


def test_index2location1():
    assert index2location(5,2) == "e2"

def test_index2location2():
    assert index2location(26,26) == "z26"

def test_index2location3():
    assert index2location(1,1) == "a1"

def test_index2location4():
    assert index2location(10,6) == "j6"

def test_index2location5():
    assert index2location(17,16) == "q16"

wr1 = Rook(3,4,True)
wk1 = King(3,5,True)


br1 = Rook(3,1,False)
bk1 = King(2,3,False)
br2 = Rook(5,5,False)


B1 = (5, [wr1, wk1, br1, bk1, br2])

def test_is_piece_at1():
    assert is_piece_at(2,2, B1) == False

def test_is_piece_at2():
    assert is_piece_at(3,1, B1) == True

def test_is_piece_at3():
    assert is_piece_at(2,3, B1) == True

def test_is_piece_at4():
    assert is_piece_at(3,5, B1) == True

def test_is_piece_at5():
    assert is_piece_at(5,3, B1) == False


def test_piece_at1():
    assert piece_at(3,4, B1) == wr1

def test_piece_at2():
    assert piece_at(3,5, B1) == wk1

def test_piece_at3():
    assert piece_at(3,1, B1) == br1

def test_piece_at4():
    assert piece_at(2,3, B1) == bk1

def test_piece_at5():
    assert piece_at(5,5, B1) == br2


def test_can_reach1():
    assert wr1.can_reach(5,4, B1) == True

def test_can_reach2():
    assert wr1.can_reach(3,5, B1) == False

def test_can_reach3():
    assert wk1.can_reach(3,4, B1) == False

def test_can_reach4():
    assert wk1.can_reach(3,6, B1) == False

def test_can_reach5():
    assert wr1.can_reach(3,1, B1) == True

def test_can_reach6():
    assert br2.can_reach(1,5,B1) == False

def test_can_reach7():
    assert wr1.can_reach(6,4,B1) == False


def test_can_move_to1():
    assert wr1.can_move_to(5,4, B1) == False

def test_can_move_to2():
    assert wr1.can_move_to(3,1,B1) == False

def test_can_move_to3():
    assert wr1.can_move_to(3,5, B1) == False

def test_can_move_to4():
    assert br2.can_move_to(1,5,B1) == False

def test_can_move_to5():
    assert br2.can_move_to(5,1,B1) == True

def test_can_move_to6():
    assert bk1.can_move_to(2,2,B1) == True

wr1a = Rook(3,3, True)

def test_move_to1():
    Actual_B = wr1.move_to(3,3, B1)
    Expected_B = (5, [wr1a, wk1, br1, bk1, br2]) 

    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5

    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found


    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

def test_move_to2():
    Actual_B = wk1.move_to(4,4, B1)
    wk1a = King(4,4,True)
    Expected_B = (5, [wr1, wk1a, br1, bk1, br2]) 

    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5

    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found


    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

def test_move_to3():
    Actual_B = br2.move_to(1,5, B1)
    br2a = Rook(1,5,False)
    Expected_B = (5, [wr1, wk1, br1, bk1, br2a]) 

    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5

    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found


    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

def test_move_to4():
    Actual_B = wr1.move_to(3,1, B1)
    wr1a = Rook(3,1,True)
    Expected_B = (5, [wr1a, wk1, bk1, br2]) 

    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5

    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found


    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

def test_move_to5():
    Actual_B = wr1.move_to(3,1, B1)
    wr1a = Rook(3,1,True)
    Expected_B = (5, [wr1a, wk1, bk1, br2]) 

    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5

    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found


    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

def test_is_check1():
    B2 = (5, [wr1a, wk1, br1, bk1])
    assert is_check(False, B2) == True

def test_is_check2():
    wk1a = King(4,3,True)
    B2 = (5, [wr1, wk1a, br1, bk1])
    assert is_check(True, B2) == False

def test_is_check3():
    B2 = (5, [wr1, wk1, br1, bk1, br2])
    assert is_check(True, B2) == True

def test_is_check4():
    br2a = Rook(5,4,False)
    B2 = (5, [wr1a, wk1, br1, bk1, br2a])
    assert is_check(True, B2) == False

def test_is_check5():
    bk1a = King(2,2,False)
    B2 = (5, [wr1a, wk1, br1, bk1a, br2])
    assert is_check(False, B2) == False


def test_is_checkmate1():
    B3 = (5, [wr1a, wk1, br1, bk1, Rook(3,4, True), Rook(3,2,True)])
    assert is_checkmate(False, B3) == True

def test_is_checkmate2():
    wr1 = Rook(5,1,True)
    wk1 = King(3,5,True)

    br3 = Rook(5,4,False)
    br1 = Rook(3,1,False)
    bk1 = King(2,3,False)
    br2 = Rook(5,5,False)


    B1 = (5, [wr1, wk1, br1, bk1, br2, br3])
    assert is_checkmate(True, B1) == True

def test_is_checkmate3():
    wr1 = Rook(5,1,True)
    wk1 = King(3,5,True)

    br3 = Rook(5,4,False)
    br1 = Rook(3,1,False)
    bk1 = King(2,3,False)
    br2 = Rook(5,5,False)


    B1 = (5, [wr1, wk1, br1, bk1, br2, br3])
    assert is_checkmate(False, B1) == False

def test_is_checkmate4():
    wr1 = Rook(5,4,True)
    wk1 = King(3,1,True)
    wr2 = Rook(5,2,True)
    wr3 = Rook(1,3,True)

    bk1 = King(3,3,False)


    B1 = (5, [wr1, wk1, wr2, wr3, bk1])
    assert is_checkmate(False, B1) == True

def test_is_checkmate5():
    wr1 = Rook(5,4,True)
    wk1 = King(3,1,True)
    wr2 = Rook(5,2,True)
    wr3 = Rook(1,3,True)


    br1 = Rook(1,5,False)
    bk1 = King(3,3,False)


    B1 = (5, [wr1, wk1, wr2, wr3, bk1, br1])
    assert is_checkmate(False, B1) == False

def test_is_checkmate6():
    wr1 = Rook(5,4,True)
    wk1 = King(1,5,True)
    wr2 = Rook(4,1,True)


    bk1 = King(3,5,False)


    B1 = (5, [wr1, wk1, wr2, bk1])

    assert is_checkmate(False,B1) == False



def test_is_stalemate1():
    wr1 = Rook(5,4,True)
    wk1 = King(1,5,True)
    wr2 = Rook(4,1,True)


    bk1 = King(3,5,False)


    B1 = (5, [wr1, wk1, wr2, bk1])

    assert is_stalemate(False,B1) == True

def test_is_stalemate2():
    wr1 = Rook(5,4,True)
    wk1 = King(3,1,True)
    wr2 = Rook(5,2,True)
    wr3 = Rook(1,3,True)

    bk1 = King(3,3,False)


    B1 = (5, [wr1, wk1, wr2, wr3, bk1])

    assert is_stalemate(False,B1) == False

def test_is_stalemate3():
    wr1 = Rook(5,4,True)
    wk1 = King(3,1,True)
    wr2 = Rook(5,2,True)
    wr3 = Rook(1,3,True)


    br1 = Rook(1,5,False)
    bk1 = King(3,3,False)


    B1 = (5, [wr1, wk1, wr2, wr3, bk1, br1])
    assert is_stalemate(False, B1) == False


def test_is_stalemate4():
    br1 = Rook(5,4,False)
    bk1 = King(1,5,False)
    br2 = Rook(4,1,False)


    wk1 = King(3,5,True)


    B1 = (5, [wk1, br2, br1, bk1])

    assert is_stalemate(True,B1) == True

def test_is_stalemate5():
    wk1 = King(3,3,True)

    br3 = Rook(5,2,False)
    bk1 = King(1,3,False)
    br2 = Rook(5,4,False)
    br1 = Rook(4,1,False)

    B1 = (5, [wk1, bk1, br2, br3, br1])

    assert is_stalemate(True,B1) == True


def test_read_board1():
    B = read_board("board_examp.txt")
    assert B[0] == 5

    B1 = (5, [King(2,3,False), Rook(5,3,False), King(3,5,True), Rook(4,4, True), Rook(3,1, True)])
    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

    for piece1 in B1[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found


def test_read_board2():
    with pytest.raises(IOError):
        read_board("board_examp2.txt")

def test_read_board3():
    with pytest.raises(IOError):
        read_board("board_examp3.txt")

def test_read_board4():
    with pytest.raises(IOError):
        read_board("board_examp4.txt")

def test_read_board5():
    with pytest.raises(IOError):
        read_board("board_examp5.txt")


def test_read_board6():
    wr1 = Rook(5,1,True)
    wk1 = King(3,5,True)

    br3 = Rook(5,4,False)
    br1 = Rook(3,1,False)
    bk1 = King(2,3,False)
    br2 = Rook(5,5,False)


    B1 = (5, [wr1, wk1, br1, bk1, br2, br3])
    B = read_board("board_examp6.txt")
    assert B[0] == 5
    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

    for piece1 in B1[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

def test_read_board7():
    with pytest.raises(IOError):
        read_board("board_examp7.txt")