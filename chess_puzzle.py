import re
from copy import deepcopy
from random import choice

def location2index(loc: str) -> tuple[int, int]:
    '''converts chess location to corresponding x and y coordinates'''
    
    #check if the string is in the right format
    if re.fullmatch(r"[a-z]\d{1,2}", loc):
        match = re.match(r"([a-z])(\d{1,2})",loc)
    else:
        raise ValueError
    
    # convert the location of the column to number and return the tuple

    letters = list("abcdefghijklmnopqrstuvwxyz")

    return (letters.index(match.group(1)) +1, int(match.group(2)))
    
	
def index2location(x: int, y: int) -> str:
    '''converts  pair of coordinates to corresponding location'''

    letters = list("abcdefghijklmnopqrstuvwxyz")
    return str(letters[x-1]+str(y))

class Piece:
    pos_x : int	
    pos_y : int
    side : bool #True for White and False for Black
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values'''
        self.pos_x = pos_X
        self.pos_y = pos_Y
        self.side = side_


Board = tuple[int, list[Piece]]


def is_piece_at(pos_X : int, pos_Y : int, B: Board) -> bool:
    '''checks if there is piece at coordinates pox_X, pos_Y of board B''' 
    #run through every position and match its position
    for piece in B[1]:
        if piece.pos_x == pos_X and piece.pos_y == pos_Y:
            return True
    return False

def piece_at(pos_X : int, pos_Y : int, B: Board) -> Piece:
    '''
    returns the piece at coordinates pox_X, pos_Y of board B 
    assumes some piece at coordinates pox_X, pos_Y of board B is present
    '''
    for piece in B[1]:
        if piece.pos_x == pos_X and piece.pos_y == pos_Y:
            return piece

class Rook(Piece):
    
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X,pos_Y,side_) #inherit from the class Piece

    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''
        checks if this Rook can move to coordinates pos_X, pos_Y
        on board B according to rule [Rule1] and [Rule3] (see section Intro)
        Hint: use is_piece_at
        '''

        # checks if the target position is the same as current position
        if self.pos_x == pos_X and self.pos_y == pos_Y:
            return False
        if pos_X < 1 or pos_X > B[0] or pos_Y < 1 or pos_Y > B[0]:
            return False

        #checks if the target position is reachable by the rook according to chess rules
        if self.pos_x == pos_X or self.pos_y == pos_Y:
            #check if any pieces are in the way to the target position by storing the list of positions 
            #in between and checking for pieces in those positions
            pos_inbetw = []
            if abs(self.pos_x-pos_X) != 0:
                for i in range(min(self.pos_x,pos_X)+1,max(self.pos_x,pos_X)):
                    pos_inbetw.append((i,self.pos_y))
            else:
                for i in range(min(self.pos_y,pos_Y)+1,max(self.pos_y,pos_Y)):
                    pos_inbetw.append((self.pos_x,i))

            for pos in pos_inbetw:
                if is_piece_at(pos[0],pos[1],B):
                    return False
            if is_piece_at(pos_X,pos_Y,B):

                #checks if the target position has the same side piece
                if piece_at(pos_X,pos_Y,B).side == self.side:
                    return False
                else:
                    return True
            return True
        else:
            return False


    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''
        checks if this Rook can move to coordinates pos_X, pos_Y
        on board B according to all chess rules
        
        Hints:
        - firstly, check [Rule1] and [Rule3] using can_reach
        - secondly, check if result of move is capture using is_piece_at
        - if yes, find the piece captured using piece_at
        - thirdly, construct new board resulting from move
        - finally, to check [Rule4], use is_check on new board
        '''
        B1 = deepcopy(B)
        piece = piece_at(self.pos_x,self.pos_y,B1)
        if piece.can_reach(pos_X,pos_Y,B1):

        #check if there is a piece at target position and remove that piece            
            if is_piece_at(pos_X,pos_Y,B1):
                B1[1].remove(piece_at(pos_X,pos_Y,B1))
        
        #move the piece to its target position
            piece.pos_x = pos_X
            piece.pos_y = pos_Y
            if is_check(piece.side,B1):
                return False
            return True
        return False


    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this rook to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''
        #If there is a piece at target position remove that piece
        if is_piece_at(pos_X,pos_Y,B):
            B[1].remove(piece_at(pos_X,pos_Y,B))
        
        #change the position of the piece
        self.pos_x = pos_X
        self.pos_y = pos_Y
        return B
   
    def unicode(self) -> str:
        '''
        returns the unicode of the piece
        '''
        if self.side == True:
            return "\u2656\u2001"
        if self.side == False:
            return "\u265C\u2001"

    def string(self) -> str:
        '''
        returns the string in Piece column row format
        '''
        Rcr = "R" + index2location(self.pos_x,self.pos_y)
        return Rcr
    
class King(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X,pos_Y,side_)

    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule2] and [Rule3]'''

        # checks if the target position is the same as current position
        if self.pos_x == pos_X and self.pos_y == pos_Y:
            return False

        if pos_X < 1 or pos_X > B[0] or pos_Y < 1 or pos_Y > B[0]:
            return False

        #checks if the target position is reachable by the King
        if (
            abs(pos_X-self.pos_x) == 1 and abs(pos_Y-self.pos_y) == 1
            ) or (
            abs(pos_X-self.pos_x) == 1 and abs(pos_Y-self.pos_y) == 0
            ) or (
            abs(pos_X-self.pos_x) == 0 and abs(pos_Y-self.pos_y) == 1
            ):
            if is_piece_at(pos_X,pos_Y,B):
                #checks if the target position has the same side piece
                if piece_at(pos_X,pos_Y,B).side == self.side:
                    return False
                else:
                    return True
            return True
        else:
            return False

    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
        #check if there is a piece at target position and remove that piece
        B1 = deepcopy(B)
        piece = piece_at(self.pos_x,self.pos_y,B1)
        if piece.can_reach(pos_X,pos_Y,B1):

        #check if there is a piece at target position and remove that piece            
            if is_piece_at(pos_X,pos_Y,B1):
                B1[1].remove(piece_at(pos_X,pos_Y,B1))
        
        #move the piece to its target position
            piece.pos_x = pos_X
            piece.pos_y = pos_Y

        #check if the new configuration results in a check
            if is_check(piece.side,B1):
                return False
            return True
        return False

    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''
        if is_piece_at(pos_X,pos_Y,B):
            B[1].remove(piece_at(pos_X,pos_Y,B))
        self.pos_x = pos_X
        self.pos_y = pos_Y

        return B

    def unicode(self):
        '''
        returns the unicode of the piece
        '''
        if self.side == True:
            return "\u2654\u2001"
        if self.side == False:
            return "\u265A\u2001"

    def string(self):
        '''
        returns the string in Piece column row format
        '''
        Kcr = "K" + index2location(self.pos_x,self.pos_y)
        return Kcr

def is_check(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is check for side
    Hint: use can_reach
    '''
    #get the king of the side
    for piece in B[1]:
        if piece.side == side and type(piece) == King:
            king = piece

    #check if the opposite side can reach the king
    for piece in B[1]:
        if piece.side != side and piece.can_reach(king.pos_x,king.pos_y,B):
            return True

    return False

def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints: 
    - use is_check
    - use can_move_to
    '''
    #check if there is any possible move available for the side that does not result in check
    if is_check(side,B):
        for piece in B[1]:
            if piece.side == side:
                for i in range(1,B[0]+1):
                    for j in range(1,B[0]+1):
                        if piece.can_move_to(i,j,B):
                            return False
        return True
    return False

def is_stalemate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is stalemate for side

    Hints: 
    - use is_check
    - use can_move_to 
    '''
    if is_check(side,B):
        return False
    else:
        for piece in B[1]:
            if piece.side == side:
                for i in range(1,B[0]+1):
                    for j in range(1,B[0]+1):
                        if piece.can_move_to(i,j,B):
                            return False
        return True

def read_board(filename: str) -> Board:
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''
    
    B = ()
    #read lines from the file
    try:
        with open(filename) as f:
            lines = f.readlines()
    except:
        raise IOError
    #check if the size of the board is in correct format
    if re.fullmatch(r"\d{1,2}",lines[0].replace('\n',"")):
        board_size = int(lines[0].replace('\n',""))
    else:
        raise IOError

    #check if the size of the board is in the range 3-26
    if board_size < 3 or board_size > 26:
        raise IOError

    #store the size of the board
    B += (board_size,)


    pieces = []

    #process the white pieces
    whites = re.findall(r"[RK][a-z]\d{1,2}",lines[1])
    no_of_king = 0
    for white in whites:
        if white[0] == "K":
            no_of_king += 1
            location = re.search(r"[a-z]\d{1,2}",white).group(0)
            position = location2index(location)
            if position[0] < 1 or position[0] > board_size or position[1] < 1 or position[1] > board_size:
                raise IOError
            pieces.append(King(position[0],position[1],True))
        if white[0] == "R":
            location = re.search(r"[a-z]\d{1,2}",white).group(0)
            position = location2index(location)
            if position[0] < 1 or position[0] > board_size or position[1] < 1 or position[1] > board_size:
                raise IOError
            pieces.append(Rook(position[0],position[1],True))

    #check if only one king is present for white
    if no_of_king != 1:
        raise IOError


    #process the black pieces
    blacks = re.findall(r"[RK][a-z]\d{1,2}",lines[2])
    no_of_king = 0
    for black in blacks:
        if black[0] == "K":
            no_of_king += 1
            location = re.search(r"[a-z]\d{1,2}",black).group(0)
            position = location2index(location)
            if position[0] < 1 or position[0] > board_size or position[1] < 1 or position[1] > board_size:
                raise IOError
            pieces.append(King(position[0],position[1],False))
        if black[0] == "R":
            location = re.search(r"[a-z]\d{1,2}",black).group(0)
            position = location2index(location)
            if position[0] < 1 or position[0] > board_size or position[1] < 1 or position[1] > board_size:
                raise IOError
            pieces.append(Rook(position[0],position[1],False))


    #check if only one king is present for black
    if no_of_king != 1:
        raise IOError

    B += (pieces,)

    return B

def save_board(filename: str, B: Board) -> None:
    '''saves board configuration into file in current directory in plain format'''
    with open(filename, "w") as fp:
        fp.write(f"{B[0]}\n") #write the board size
        for piece in B[1]:
            if piece.side == True:
                fp.write(f"{piece.string()}, ") #write the white pieces
        fp.write("\n")
        for piece in B[1]:
            if piece.side == False:
                fp.write(f"{piece.string()}, ") #write the black pieces



def find_black_move(B: Board) -> tuple[Piece, int, int]:
    '''
    returns (P, x, y) where a Black piece P can move on B to coordinates x,y according to chess rules 
    assumes there is at least one black piece that can move somewhere

    Hints: 
    - use methods of random library
    - use can_move_to
    '''
    #create a list of all available moves for black pieces
    available_moves = []
    
    for i in range(1,B[0]+1):
        for j in range(1,B[0]+1):
            for piece in B[1]:
                if piece.side == False:
                    if piece.can_move_to(i,j,B):
                        available_moves.append((piece, i, j))
    
    #choose a move by random choice
    move = choice(available_moves)

    return move

    

def conf2unicode(B: Board) -> str: 
    '''converts board cofiguration B to unicode format string (see section Unicode board configurations)'''
    conf = []

    letters = list("abcdefghijklmnopqrstuvwxyz")
    #create a list of columns to show it in the string
    columns = ["\u2001\u2001"]
    for i in range(0,B[0]):
        columns.append(letters[i]+"\u2001")
    conf.append(columns)

    #fill the config with white spaces and later replace it with pieces
    for i in range(1,B[0]+1):
        conf.append([])
        conf[i].append(str(i)+"\u2001")
        for j in range(0,B[0]):
            conf[i].append("\u2001\u2001")
        conf[i].append("\n")
    
    #place the pieces in their positions
    for piece in B[1]:
        conf[piece.pos_y][piece.pos_x] = piece.unicode()

    conf.reverse()

    #convert the list into string
    unicode = str("")
    for i in conf:
        for j in i:
            unicode += j
    return unicode
    

def whitemove(B):
    '''
    Processes the white turns
    '''
    #check the current configuration for checkmate and stalemate for white
    if is_checkmate(True, B):
        print("Game over. Black wins.")
        exit()
    if is_stalemate(True, B):
        print("Game over. Stalemate.")
        exit()

    next_move = input("Next move of White: ")
    if next_move =="QUIT":
        filename = input("File name to store the configuration: ")
        save_board(filename,B)
        print("The game configuration saved.")
        exit()

    #check if the input is in the correct format
    if re.fullmatch(r"[a-z]\d{1,2}[a-z]\d{1,2}",next_move):
        positions = re.findall(r"[a-z]\d{1,2}",next_move)
        curr_pos = location2index(positions[0])
        targ_pos = location2index(positions[1])

        #check if there is a piece at current position
        if is_piece_at(curr_pos[0],curr_pos[1],B):
            piece = piece_at(curr_pos[0],curr_pos[1],B)

            #check the side of the piece and if its a valid move
            if piece.side == True and piece.can_move_to(targ_pos[0],targ_pos[1],B):
                new_B = piece.move_to(targ_pos[0],targ_pos[1],B)
                #print the new configuration
                print("The configuration after White's move is:\n")
                print(conf2unicode(new_B))
                #proceed to black turn
                blackmove(new_B)

    #if its not a valid move repeat the process again
    print("This is not a valid move. ")
    whitemove(B)

def blackmove(B):
    '''
    Processes the black turns
    '''
    #check if the current configuration is checkmate or stalemate for black
    if is_checkmate(False,B):
        print("Game over. White wins.")
        exit()
    if is_stalemate(False, B):
        print("Game over. Stalemate.")
        exit()

    move = find_black_move(B)
    curr_loc = index2location(move[0].pos_x,move[0].pos_y)
    targ_loc = index2location(move[1],move[2])
    new_B = move[0].move_to(move[1],move[2],B)

    #print the black move
    print(f"Next move of Black is {curr_loc}{targ_loc}. The configuration after Black's move is:\n")
    print(conf2unicode(new_B))

    #proceed to white move
    whitemove(new_B)


def main() -> None:
    '''
    runs the play

    Hint: implementation of this could start as follows:
    filename = input("File name for initial configuration: ")
    ...
    '''    
    filename = input("File name for initial configuration: ")

    if filename == "QUIT":
        exit()

    #Function to start the game

    def start(filename):
        try:
            B = read_board(filename)
            print("The initial configuration is:\n")
            print(conf2unicode(B))
            whitemove(B)
        except OSError: #catch the errors
            filename = input("This is not a valid file. File name for initial configuration: ")
            if filename == "QUIT":
                exit()
            start(filename)

    
    start(filename)
    


if __name__ == '__main__': #keep this in
   main()
