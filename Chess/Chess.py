import tkinter as tk

window = tk.Tk()
window.title('Chess')
window .geometry('800x750')

# import all need photo and number its(left number means Black or White,right means piece)
img0 = tk.PhotoImage(file = 'chess board.png')
img1_1 = tk.PhotoImage(file = 'kingB.png')
img1_2 = tk.PhotoImage(file = 'queenB.png')
img1_3 = tk.PhotoImage(file = 'bishopB.png')
img1_4 = tk.PhotoImage(file = 'knightB.png')
img1_5 = tk.PhotoImage(file = 'rookB.png')
img1_6 = tk.PhotoImage(file = 'pawnB.png')
img2_1 = tk.PhotoImage(file = 'kingW.png')
img2_2 = tk.PhotoImage(file = 'queenW.png')
img2_3 = tk.PhotoImage(file = 'bishopW.png')
img2_4 = tk.PhotoImage(file = 'knightW.png')
img2_5 = tk.PhotoImage(file = 'rookW.png')
img2_6 = tk.PhotoImage(file = 'pawnW.png')
give_up = tk.PhotoImage(file = 'resign.png')
white = tk.PhotoImage(file = 'WhiteWin.png')
black = tk.PhotoImage(file = 'BlackWin.png')

# BW means current player (set white as default for white first)
# var is the kind of  piece player want to rise (have queen bishop knight rook)
# prom_mes is the prompt message for players (empty as default)
BW = tk.StringVar()
BW.set('White')
var = tk.StringVar()
prom_mes = tk.StringVar()
prom_mes.set('')
Chess_manual_S = ''

class Chess():
    '''A class to represent each chessman
    have attributes like position,kind,photo and frequency of move
    '''
    # Each default data is build as list first. every piece's data have common index in every list
    pieces = ['King','Queen','Bishop1','Bishop2','Knight1','Knight2','Rook1','Rook2'
              ,'Pawn1','Pawn2','Pawn3','Pawn4','Pawn5','Pawn6','Pawn7','Pawn8']
    init_posi_W_X = ['E','D','C','F','B','G','A','H','A','B','C','D','E','F','G','H']
    init_posi_W_Y = ['1','1','1','1','1','1','1','1','2','2','2','2','2','2','2','2']
    init_posi_B_X = ['E','D','C','F','B','G','A','H','A','B','C','D','E','F','G','H']
    init_posi_B_Y = ['8','8','8','8','8','8','8','8','7','7','7','7','7','7','7','7']
    # use two dictionaries to switch between Chess manual and coordinate 
    X_to_N = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
    N_to_X = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H'}
    Photo_W = [img2_1,img2_2,img2_3,img2_3,img2_4,img2_4,img2_5,img2_5
               ,img2_6,img2_6,img2_6,img2_6,img2_6,img2_6,img2_6,img2_6]
    Photo_B = [img1_1,img1_2,img1_3,img1_3,img1_4,img1_4,img1_5,img1_5
               ,img1_6,img1_6,img1_6,img1_6,img1_6,img1_6,img1_6,img1_6]
    check = True
    count = 0
    former = [None,None,None]
    def __init__(self,S = 'W',piece = 0,posi_x = 0,posi_y = 0,P = 0):
        '''A method to build a new chessman'''
        S = S.upper()
        if S == 'W':
            self.piece = Chess.pieces[piece]
            self.posi_X = Chess.init_posi_W_X[posi_x]
            self.posi_Y = Chess.init_posi_W_Y[posi_y]
            self.color = 'W'
            self.count = Chess.count
            self.photo = Chess.Photo_W[P]
        else:
            self.piece = Chess.pieces[piece]
            self.posi_X = Chess.init_posi_B_X[posi_x]
            self.posi_Y = Chess.init_posi_B_Y[posi_y]
            self.color = 'B'
            self.count = Chess.count
            self.photo = Chess.Photo_B[P]
    def __repr__(self):
        return f'{self.piece} {self.posi_X + self.posi_Y}'
    def move(self,oriX,oriy,posi_x,posi_y,take):
        '''A method to move each chessman
        use attibute of kind to determine which funcion call
        return value means the move is valid
        '''
        if self.piece == 'King':
            if Chess.king_move(self,oriX,oriy,posi_x,posi_y,take) == True:
                return True
            return False
        elif self.piece == 'Queen':
            if Chess.queen_move(self,oriX,oriy,posi_x,posi_y,take) == True:
                return True
            return False
        elif self.piece in ('Bishop1','Bishop2','Bishop'):
            if Chess.bishop_move(self,oriX,oriy,posi_x,posi_y,take) == True:
                return True
            return False
        elif self.piece in ('Knight1','Knight2','Knight'):
            if Chess.knight_move(self,oriX,oriy,posi_x,posi_y,take) == True:
                return True
            return False
        elif self.piece in ('Rook1','Rook2','Rook'):
            if Chess.rook_move(self,oriX,oriy,posi_x,posi_y,take) == True:
                return True
            return False
        else:
            if Chess.pawn_move(self,oriX,oriy,posi_x,posi_y,take) == True:
                return True
            return False
    def king_move(self,orix,oriy,posi_x,posi_y,take):
        '''A method to check and operate the move of king
        six parameter means chessman,original coordinate,new coordinate,take other or not 
        return value means the move of king is valid
        '''
        OX = Chess.X_to_N[orix]
        OY = int(oriy)
        AX = Chess.X_to_N[posi_x]
        AY = int(posi_y)
        if (abs(AY - OY),abs(AX - OX)) in ((0,1),(1,0),(1,1)):
            self.posi_X = posi_x
            self.posi_Y = posi_y
            return True
        # The definition of Castling (consist of four blocks mean long or short Castling for White and Black)
        if AX-OX==2 and abs(AY-OY)==0 and self.count==0 and self.color=='W' and posi_x=='G':
            R = Chess_game.D['H1']
            if R.piece=='Rook2' and R.count==0 and Chess_game.D['G1']==Chess_game.D['F1']==False:
                self.posi_X = posi_x
                self.posi_Y = posi_y
                R.posi_X = 'F'
                R.posi_Y = '1'
                Chess_game.D['F1'] = R
                Chess_game.D['H1'] = False
                return True
        if AX-OX==(-2) and abs(AY-OY)==0 and self.count==0 and self.color=='W' and posi_x=='C':
            R = Chess_game.D['A1']
            if R.piece=='Rook1' and R.count==0 and Chess_game.D['B1']==Chess_game.D['C1']==Chess_game.D['D1']==False:
                self.posi_X = posi_x
                self.posi_Y = posi_y
                R.posi_X = 'D'
                R.posi_Y = '1'
                Chess_game.D['D1'] = R
                Chess_game.D['A1'] = False
                return True
        if AX-OX==2 and abs(AY-OY)==0 and self.count==0 and self.color=='B' and posi_x=='G':
            R = Chess_game.D['H8']
            if R.piece=='Rook2' and R.count==0 and Chess_game.D['G8']==Chess_game.D['F8']==False:
                self.posi_X = posi_x
                self.posi_Y = posi_y
                R.posi_X = 'F'
                R.posi_Y = '8'
                Chess_game.D['F8'] = R
                Chess_game.D['H8'] = False
                return True
        if AX-OX==(-2) and abs(AY-OY)==0 and self.count==0 and self.color=='B' and posi_x=='C':
            R = Chess_game.D['A8']
            if R.piece=='Rook1' and R.count==0 and Chess_game.D['B8']==Chess_game.D['C8']==Chess_game.D['D8']==False:
                self.posi_X = posi_x
                self.posi_Y = posi_y
                R.posi_X = 'D'
                R.posi_Y = '8'
                Chess_game.D['D8'] = R
                Chess_game.D['A8'] = False
                return True
        return False
    def queen_move(self,orix,oriy,posi_x,posi_y,take):
        '''A method to check and operate the move of queen
        six parameter means chessman,original coordinate,new coordinate,take other or not 
        return value means the move of queen is valid
        '''
        # queens move is equal to bishop or rook, so function call directly
        if Chess.bishop_move(self,orix,oriy,posi_x,posi_y,take) == True:
            return True
        if Chess.rook_move(self,orix,oriy,posi_x,posi_y,take) == True:
            return True
        return False
    def bishop_move(self,orix,oriy,posi_x,posi_y,take):
        '''A method to check and operate the move of bishop
        six parameter means chessman,original coordinate,new coordinate,take other or not 
        return value means the move of bishop is valid
        '''
        OX = Chess.X_to_N[orix]
        OY = int(oriy)
        AX = Chess.X_to_N[posi_x]
        AY = int(posi_y)
        if abs(AX - OX) == abs(AY - OY) and abs(AY - OY) != 0 and abs(AX - OX) != 0:
            interval = abs(AX - OX)
            if AX - OX > 0 and AY - OY > 0:
                for i in range(1,interval):
                    if Chess_game.D[Chess.N_to_X[OX + i] + str(OY + i)] != False:
                        return False
            if AX - OX < 0 and AY - OY > 0:
                for i in range(1,interval):
                    if Chess_game.D[Chess.N_to_X[OX - i] + str(OY + i)] != False:
                        return False
            if AX - OX < 0 and AY - OY < 0:
                for i in range(1,interval):
                    if Chess_game.D[Chess.N_to_X[OX - i] + str(OY - i)] != False:
                        return False
            if AX - OX > 0 and AY - OY < 0:
                for i in range(1,interval):
                    if Chess_game.D[Chess.N_to_X[OX + i] + str(OY - i)] != False:
                        return False
            self.posi_X = posi_x
            self.posi_Y = posi_y
            return True
        return False
    def knight_move(self,orix,oriy,posi_x,posi_y,take):
        '''A method to check and operate the move of knight
        six parameter means chessman,original coordinate,new coordinate,take other or not 
        return value means the move of knight is valid
        '''
        OX = Chess.X_to_N[orix]
        OY = int(oriy)
        AX = Chess.X_to_N[posi_x]
        AY = int(posi_y)
        if (abs(AX - OX),abs(AY - OY)) in ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)):
            self.posi_X = posi_x
            self.posi_Y = posi_y
            return True
        return False
    def rook_move(self,orix,oriy,posi_x,posi_y,take):
        '''A method to check and operate the move of rook
        six parameter means chessman,original coordinate,new coordinate,take other or not 
        return value means the move of rook is valid
        '''
        OX = Chess.X_to_N[orix]
        OY = int(oriy)
        AX = Chess.X_to_N[posi_x]
        AY = int(posi_y)
        if OX == AX and OY != AY:
            if AY - OY > 0:
                for i in range(min(AY,OY) + 1,max(AY,OY)):
                    if Chess_game.D[orix + str(i)] != False:
                        return False
            elif AY - OY < 0:
                for i in range(min(AY,OY) + 1,max(AY,OY)):
                    if Chess_game.D[orix + str(i)] != False:
                        return False
            self.posi_X = posi_x
            self.posi_Y = posi_y
            return True
        elif OX != AX and OY == AY:
            if AX - OX > 0:    
                for i in range(min(AX,OX) + 1,max(AX,OX)):
                    if Chess_game.D[Chess.N_to_X[i] + oriy] != False:
                        return False
            elif AX - OX < 0:
                for i in range(min(AX,OX) + 1,max(AX,OX)):
                    if Chess_game.D[Chess.N_to_X[i] + oriy] != False:
                        return False
            self.posi_X = posi_x
            self.posi_Y = posi_y
            return True
        return False
    def pawn_move(self,orix,oriy,posi_x,posi_y,take):
        '''A method to check and operate the move of pawn
        six parameter means chessman,original coordinate,new coordinate,take other or not 
        return value means the move of king is valid
        '''
        OX = Chess.X_to_N[orix]
        OY = int(oriy)
        AX = Chess.X_to_N[posi_x]
        AY = int(posi_y)
        # The normal move (only first can be 2)
        if AX == OX and AY - OY in (2,-2) and self.count == 0 and take == False:
            if Chess_game.D[posi_x + str(int((AY + OY)/2))] == False:
                self.posi_X = posi_x
                self.posi_Y = posi_y
                Chess_game.game_count = 0
                return True
        if AX == OX and AY - OY in (1,-1) and take == False:
            self.posi_X = posi_x
            self.posi_Y = posi_y
            Chess_game.game_count = 0
            # If reach bottom, use rise function call
            if AY in (1,8):
                Chess.rise(self)
            return True
        # En passant
        if abs(AY - OY) == 1 and abs(AX - OX) == 1 and take == False:
            if oriy=='5' and Chess.former[0][:4]=='Pawn' and Chess.former[1]==posi_x+str(AY-1) and self.color=='W':
                self.posi_X = posi_x
                self.posi_Y = posi_y
                Chess.former[1] = False
                Chess.former[2].posi_X = 'X'
                Chess.former[2].posi_Y = 'X'
                Chess_game.game_count = 0
                return True
            if oriy=='4' and Chess.former[0][:4]=='Pawn' and Chess.former[1]==posi_x+str(AY+1) and self.color=='B':
                self.posi_X = posi_x
                self.posi_Y = posi_y
                Chess.former[1] = False
                Chess.former[2].posi_X = 'X'
                Chess.former[2].posi_Y = 'X'
                Chess_game.game_count = 0
                return True
        # normal take   (the take of pawn is different from its normal move, so we need to define it particularly)
        if abs(AY - OY) == 1 and abs(AX - OX) == 1 and take == True:
            if (self.color == 'W' and AY - OY == 1) or (self.color == 'B' and AY - OY == -1):
                self.posi_X = posi_x
                self.posi_Y = posi_y
                Chess_game.game_count = 0
                # If reach bottom, use rise function call
                if AY in (1,8):
                    Chess.rise(self)
                return True
        return False
    def rise(self):
        '''A method to rise pawn to different chessman
        vart is the choice of player
        change the pieces kind,photo 
        '''
        vart = var.get()
        if self.color == 'W':
            self.piece = vart
            if vart == 'Queen':
                self.photo = img2_2
            elif vart == 'Knight':
                self.photo = img2_4
            elif vart == 'Bishop':
                self.photo = img2_3
            else:
                self.photo = img2_5
        if self.color == 'B':
            self.piece = vart
            if vart == 'Queen':
                self.photo = img1_2
            elif vart == 'Knight':
                self.photo = img1_4
            elif vart == 'Bishop':
                self.photo = img1_3
            else:
                self.photo = img1_5
class Chess_game(Chess):
    '''A class to represent a Chess game
    have attribute of the Chess means a player's pieces
    have D means the board state and game_count means the count of move
    '''
    game_count = 0
    D = {'A1':False,'A2':False,'A3':False,'A4':False,'A5':False,'A6':False,'A7':False,'A8':False
         ,'B1':False,'B2':False,'B3':False,'B4':False,'B5':False,'B6':False,'B7':False,'B8':False
         ,'C1':False,'C2':False,'C3':False,'C4':False,'C5':False,'C6':False,'C7':False,'C8':False
         ,'D1':False,'D2':False,'D3':False,'D4':False,'D5':False,'D6':False,'D7':False,'D8':False
         ,'E1':False,'E2':False,'E3':False,'E4':False,'E5':False,'E6':False,'E7':False,'E8':False
         ,'F1':False,'F2':False,'F3':False,'F4':False,'F5':False,'F6':False,'F7':False,'F8':False
         ,'G1':False,'G2':False,'G3':False,'G4':False,'G5':False,'G6':False,'G7':False,'G8':False
         ,'H1':False,'H2':False,'H3':False,'H4':False,'H5':False,'H6':False,'H7':False,'H8':False}
    def __init__(self,BW):
        '''A method to start a new player'''
        self.Chess = []
        for i in range(16):
            T = Chess(BW,i,i,i,i)
            if BW == 'W':
                S1 = Chess.init_posi_W_X[i]
                S2 = Chess.init_posi_W_Y[i]
            else:
                S1 = Chess.init_posi_B_X[i]
                S2 = Chess.init_posi_B_Y[i]
            S = S1 + S2
            Chess_game.D[S] = T
            self.Chess.append(T)
    def __repr__(self):
        for elem in self.Chess:
            print(elem)
    def is_end(self):
        '''A method to check if White or Black is lose'''
        if self.Chess[0].posi_X == 'X' and self.Chess[0].posi_Y == 'X':
            return True
        return False
# Build two player A is the White and B is the Black
A = Chess_game('W')
B = Chess_game('B')

# Two dictionaries represent the photo coordinate in canvas
# X is a position dont appear in the canvas ,so use it to represent dead
X = {'A': 264, 'B': 302, 'C': 340, 'D': 380, 'E': 420, 'F': 460, 'G': 498, 'H': 536, 'X': 9999}
Y = {'1': 336, '2': 296, '3': 256, '4': 218, '5': 178, '6': 140, '7': 101, '8': 63, 'X': 9999}
# Build a Canvas to show the board and pieces
Canvas = tk.Canvas(window,bg = 'white',width = 800,height = 400)
Canvas.place(x = 0,y = 0)

def Graph():
    '''A function to updata the current game'''
    # Each call will clean all old data and create the new object
    Canvas.delete('all')
    board = Canvas.create_image(400,200,anchor = 'center',image = img0)
    
    kingB = Canvas.create_image(X[B.Chess[0].posi_X],Y[B.Chess[0].posi_Y],anchor = 'center',image = B.Chess[0].photo)
    queenB = Canvas.create_image(X[B.Chess[1].posi_X],Y[B.Chess[1].posi_Y],anchor = 'center',image = B.Chess[1].photo)
    bishopB1 = Canvas.create_image(X[B.Chess[2].posi_X],Y[B.Chess[2].posi_Y],anchor = 'center',image = B.Chess[2].photo)
    bishopB2 = Canvas.create_image(X[B.Chess[3].posi_X],Y[B.Chess[3].posi_Y],anchor = 'center',image = B.Chess[3].photo)
    knightB1 = Canvas.create_image(X[B.Chess[4].posi_X],Y[B.Chess[4].posi_Y],anchor = 'center',image = B.Chess[4].photo)
    knightB2 = Canvas.create_image(X[B.Chess[5].posi_X],Y[B.Chess[5].posi_Y],anchor = 'center',image = B.Chess[5].photo)
    rookB1 = Canvas.create_image(X[B.Chess[6].posi_X],Y[B.Chess[6].posi_Y],anchor = 'center',image = B.Chess[6].photo)
    rookB2 = Canvas.create_image(X[B.Chess[7].posi_X],Y[B.Chess[7].posi_Y],anchor = 'center',image = B.Chess[7].photo)
    pawnB1 = Canvas.create_image(X[B.Chess[8].posi_X],Y[B.Chess[8].posi_Y],anchor = 'center',image = B.Chess[8].photo)
    pawnB2 = Canvas.create_image(X[B.Chess[9].posi_X],Y[B.Chess[9].posi_Y],anchor = 'center',image = B.Chess[9].photo)
    pawnB3 = Canvas.create_image(X[B.Chess[10].posi_X],Y[B.Chess[10].posi_Y],anchor = 'center',image = B.Chess[10].photo)
    pawnB4 = Canvas.create_image(X[B.Chess[11].posi_X],Y[B.Chess[11].posi_Y],anchor = 'center',image = B.Chess[11].photo)
    pawnB5 = Canvas.create_image(X[B.Chess[12].posi_X],Y[B.Chess[12].posi_Y],anchor = 'center',image = B.Chess[12].photo)
    pawnB7 = Canvas.create_image(X[B.Chess[13].posi_X],Y[B.Chess[13].posi_Y],anchor = 'center',image = B.Chess[13].photo)
    pawnB8 = Canvas.create_image(X[B.Chess[14].posi_X],Y[B.Chess[14].posi_Y],anchor = 'center',image = B.Chess[14].photo)
    pawnB9 = Canvas.create_image(X[B.Chess[15].posi_X],Y[B.Chess[15].posi_Y],anchor = 'center',image = B.Chess[15].photo)
    
    kingW = Canvas.create_image(X[A.Chess[0].posi_X],Y[A.Chess[0].posi_Y],anchor = 'center',image = A.Chess[0].photo)
    queenW = Canvas.create_image(X[A.Chess[1].posi_X],Y[A.Chess[1].posi_Y],anchor = 'center',image = A.Chess[1].photo)
    bishopW1 = Canvas.create_image(X[A.Chess[2].posi_X],Y[A.Chess[2].posi_Y],anchor = 'center',image = A.Chess[2].photo)
    bishopW2 = Canvas.create_image(X[A.Chess[3].posi_X],Y[A.Chess[3].posi_Y],anchor = 'center',image = A.Chess[3].photo)
    knightW1 = Canvas.create_image(X[A.Chess[4].posi_X],Y[A.Chess[4].posi_Y],anchor = 'center',image = A.Chess[4].photo)
    knightW2 = Canvas.create_image(X[A.Chess[5].posi_X],Y[A.Chess[5].posi_Y],anchor = 'center',image = A.Chess[5].photo)
    rookW1 = Canvas.create_image(X[A.Chess[6].posi_X],Y[A.Chess[6].posi_Y],anchor = 'center',image = A.Chess[6].photo)
    rookW2 = Canvas.create_image(X[A.Chess[7].posi_X],Y[A.Chess[7].posi_Y],anchor = 'center',image = A.Chess[7].photo)
    pawnW1 = Canvas.create_image(X[A.Chess[8].posi_X],Y[A.Chess[8].posi_Y],anchor = 'center',image = A.Chess[8].photo)
    pawnW2 = Canvas.create_image(X[A.Chess[9].posi_X],Y[A.Chess[9].posi_Y],anchor = 'center',image = A.Chess[9].photo)
    pawnW3 = Canvas.create_image(X[A.Chess[10].posi_X],Y[A.Chess[10].posi_Y],anchor = 'center',image = A.Chess[10].photo)
    pawnW4 = Canvas.create_image(X[A.Chess[11].posi_X],Y[A.Chess[11].posi_Y],anchor = 'center',image = A.Chess[11].photo)
    pawnW5 = Canvas.create_image(X[A.Chess[12].posi_X],Y[A.Chess[12].posi_Y],anchor = 'center',image = A.Chess[12].photo)
    pawnW6 = Canvas.create_image(X[A.Chess[13].posi_X],Y[A.Chess[13].posi_Y],anchor = 'center',image = A.Chess[13].photo)
    pawnW7 = Canvas.create_image(X[A.Chess[14].posi_X],Y[A.Chess[14].posi_Y],anchor = 'center',image = A.Chess[14].photo)
    pawnW8 = Canvas.create_image(X[A.Chess[15].posi_X],Y[A.Chess[15].posi_Y],anchor = 'center',image = A.Chess[15].photo)
def Resign():
    '''A function to operate the surrender'''
    # Build a new Canvas to cover whole game and show the winner
    Canvas_R = tk.Canvas(window,bg = 'white',width = 800,height = 400)
    Canvas_R.place(x = 0,y = 0)
    Resign = Canvas_R.create_image(400,198,anchor = 'center',image = give_up)
    var = BW.get()
    done.destroy()
    resign.destroy()
    if var == 'White':
        Winner = tk.Label(window,text = 'The Black win!!!',font = ('ARial',20),bg = 'yellow').place(x = 310,y = 5)
    else:
        Winner = tk.Label(window,text = 'The White win!!!',font = ('ARial',20),bg = 'yellow').place(x = 310,y = 5)
    Record()
def Draw():
    if Chess_game.game_count >= 50:
        Canvas_D = tk.Canvas(window,bg = 'white',width = 800,height = 400)
        Canvas_R.place(x = 0,y = 0)
        d = tk.Label(window,text = 'Draw',font = ('ARial',20),bg = 'yellow').place(x = 310,y = 5)
        return True
    return False
def MOVE_W():
    '''A function to operate the move of White piece'''
    global B
    global Chess_manual_S
    Chess.check = True
    var1 = piece_input.get()
    var2 = move_input.get()
    var = var1 + '-->' +  var2
    Ox = var1[0]
    Oy = var1[1]
    Tx = var2[0]
    Ty = var2[1]
    koma = Chess_game.D[var1]
    koma_taken = Chess_game.D[var2]
    # Normal move
    if koma_taken == False and koma.color == 'W':
        Tem = Chess.move(koma,Ox,Oy,Tx,Ty,False)
        if Tem == True:
            Chess_game.D[var1] = False
            Chess_game.D[var2] = koma
            Graph()
            chess_manual.insert('end',var)
            Chess_manual_S += ('W ' + koma.piece + ' ' + var + '\n')
            prom_mes.set('')
            BW.set('Black')
            koma.count += 1
            Chess.former[0] = koma.piece
            Chess.former[1] = var2
            Chess.former[2] = koma
            Chess_game.game_count += 1
            Draw()
        else:
            prom_mes.set('Invalid move')
    # Move with take
    elif koma_taken != False and koma.color == 'W' and koma_taken.color == 'B':
        Tem = Chess.move(koma,Ox,Oy,Tx,Ty,True)
        if Tem == True:
            koma_taken.posi_X = 'X'
            koma_taken.posi_Y = 'X'
            Chess_game.D[var1] = False
            Chess_game.D[var2] = koma
            Graph()
            chess_manual.insert('end',var)
            Chess_manual_S += ('W ' + koma.piece + ' ' + var + '\n')
            prom_mes.set('')
            BW.set('Black')
            koma.count += 1
            Chess_game.game_count = 0
        else:
            prom_mes.set('Invalid move')
    # Take the piece with common color
    elif koma_taken != False and koma.color == 'W' and koma_taken.color == 'W':
        prom_mes.set('Dont take the White piece')
    # Move the opponents piece
    else:
        prom_mes.set('Dont move the Black piece')
    # Check if Black is lose
    if Chess_game.is_end(B):
        Canvas_W = tk.Canvas(window,bg = 'white',width = 800,height = 400)
        Canvas_W.place(x = 0,y = 0)
        White_win = Canvas_W.create_image(400,398,anchor = 'center',image = white)
        Winner = tk.Label(window,text = 'The White win!!!',font = ('ARial',20),bg = 'yellow').place(x = 310,y = 5)
        Record()
def MOVE_B():
    '''A function to operate the move of Black piece'''
    global A
    global Chess_manual_S
    Chess.check = True
    var1 = piece_input.get()
    var2 = move_input.get()
    var = var1 + '-->' +  var2
    Ox = var1[0]
    Oy = var1[1]
    Tx = var2[0]
    Ty = var2[1]
    koma = Chess_game.D[var1]
    koma_taken = Chess_game.D[var2]
    # Normal move
    if koma_taken == False and koma.color == 'B':
        Tem = Chess.move(koma,Ox,Oy,Tx,Ty,False)
        if Tem == True:
            Chess_game.D[var1] = False
            Chess_game.D[var2] = koma
            Graph()
            chess_manual.insert('end',var)
            Chess_manual_S += ('B ' + koma.piece + ' ' + var + '\n')
            prom_mes.set('')
            BW.set('White')
            koma.count += 1
            Chess.former[0] = koma.piece
            Chess.former[1] = var2
            Chess.former[2] = koma
            Chess_game.game_count += 1
            Draw()
        else:
            prom_mes.set('Invalid move')
    # Move with take
    elif koma_taken != False and koma.color == 'B' and koma_taken.color == 'W':
        Tem = Chess.move(koma,Ox,Oy,Tx,Ty,True)
        if Tem == True:
            koma_taken.posi_X = 'X'
            koma_taken.posi_Y = 'X'
            Chess_game.D[var1] = False
            Chess_game.D[var2] = koma
            Graph()
            chess_manual.insert('end',var)
            Chess_manual_S += ('B ' + koma.piece + ' ' + var + '\n')
            prom_mes.set('')
            BW.set('White')
            koma.count += 1
            Chess_game.game_count = 0
        else:
            prom_mes.set('Invalid move')
    # Take the piece with common color
    elif koma_taken != False and koma.color == 'B' and koma_taken.color == 'B':
        prom_mes.set('Dont take the Black piece')
    # Move the opponents piece
    else:
        prom_mes.set('Dont move the White piece')
    # Check if White is lose
    if Chess_game.is_end(A):
        Canvas_B = tk.Canvas(window,bg = 'white',width = 800,height = 400)
        Canvas_B.place(x = 0,y = 0)
        Black_win = Canvas_B.create_image(400,198,anchor = 'center',image = black)
        Winner = tk.Label(window,text = 'The Black win!!!',font = ('ARial',20),bg = 'yellow').place(x = 310,y = 5)
        Record()
def BW_check():
    '''A function to seperate White and Black move'''
    var = BW.get()
    if var == 'White':
        MOVE_W()
    if var == 'Black':
        MOVE_B()
def Record():
    global Chess_manual_S
    file = open('Chess.txt','w')
    file.write(Chess_manual_S)
    file.close()
# The coordinate prompt
AG = tk.Label(window,text = 'A',font = ('ARial',20),bg = 'white').place(x = 252,y = 5)
BG = tk.Label(window,text = 'B',font = ('ARial',20),bg = 'white').place(x = 291,y = 5)
CG = tk.Label(window,text = 'C',font = ('ARial',20),bg = 'white').place(x = 330,y = 5)
DG = tk.Label(window,text = 'D',font = ('ARial',20),bg = 'white').place(x = 368,y = 5)
EG = tk.Label(window,text = 'E',font = ('ARial',20),bg = 'white').place(x = 407,y = 5)
FG = tk.Label(window,text = 'F',font = ('ARial',20),bg = 'white').place(x = 450,y = 5)
GG = tk.Label(window,text = 'G',font = ('ARial',20),bg = 'white').place(x = 484,y = 5)
HG = tk.Label(window,text = 'H',font = ('ARial',20),bg = 'white').place(x = 524,y = 5)
number8 = tk.Label(window,text = '8',font = ('ARial',20),bg = 'white').place(x = 212,y = 45)
number7 = tk.Label(window,text = '7',font = ('ARial',20),bg = 'white').place(x = 212,y = 85)
number6 = tk.Label(window,text = '6',font = ('ARial',20),bg = 'white').place(x = 212,y = 125)
number5 = tk.Label(window,text = '5',font = ('ARial',20),bg = 'white').place(x = 212,y = 165)
number4 = tk.Label(window,text = '4',font = ('ARial',20),bg = 'white').place(x = 212,y = 205)
number3 = tk.Label(window,text = '3',font = ('ARial',20),bg = 'white').place(x = 212,y = 245)
number2 = tk.Label(window,text = '2',font = ('ARial',20),bg = 'white').place(x = 212,y = 280)
number1 = tk.Label(window,text = '1',font = ('ARial',20),bg = 'white').place(x = 212,y = 318)

# The prompt message of input data 
piece = tk.Label(window,text = 'Piece :',font = ('ARial',20)).place(x = 50,y = 480)
move = tk.Label(window,text = 'Move :',font = ('ARial',20)).place(x = 50,y = 520)
# The prompt message of current player and warning
leading = tk.Label(window,textvariable = BW,font = ('ARial',20),bg = 'light blue').place(x = 50,y = 420)
prompt = tk.Label(window,textvariable = prom_mes,width = 20,font = ('ARial',10)).place(x = 150,y = 420)
# The listbox to represent all move from game start
chess_manual = tk.Listbox(window,width = 40,height = 15)
chess_manual.place(x = 350,y = 420)
# The entry
piece_input = tk.Entry(window,font = ('ARial',18),width = 10)
piece_input.place(x = 150,y = 485)
move_input = tk.Entry(window,font = ('ARial',18),width = 10)
move_input.place(x = 150,y = 525)

Graph()
# Each button means done and resign
done = tk.Button(window,text = 'Done',font = ('ARial',20),width = 8,height = 1,bg = 'light blue'
                 ,command = BW_check)
done.place(x = 50,y = 580)
resign = tk.Button(window,text = 'Resign',font = ('ARial',20),width = 8,height = 1,bg = 'gray'
                 ,command = Resign)
resign.place(x = 50,y = 650)

# Four radiobuttons for user to choose when rise
R_queen = tk.Radiobutton(window,text = 'Queen',font = (('ARial'),10),variable = var,value = 'Queen'
                         ,width = 6,height = 1,bg = 'white').place(x = 360,y = 670)
R_knight = tk.Radiobutton(window,text = 'Knight',font = (('ARial'),10),variable = var,value = 'Knight'
                          ,width = 6,height = 1,bg = 'white').place(x = 450,y = 670)
R_bishop = tk.Radiobutton(window,text = 'Bishop',font = (('ARial'),10),variable = var,value = 'Bishop'
                          ,width = 6,height = 1,bg = 'white').place(x = 540,y = 670)
R_rook = tk.Radiobutton(window,text = 'Rook',font = (('ARial'),10),variable = var,value = 'Rook'
                        ,width = 6,height = 1,bg = 'white').place(x = 630,y = 670)

window.mainloop()