import pygame

pygame.init()
WIDTH, HEIGHT = 900, 900
RED, BLUE, DARK_RED = (244, 5, 21), (58, 148, 236), (194, 16, 13)
LOW, MID, HIGH = 150, 450, 750
LENGTH, OFFSET = 100, 120
pygame.display.set_caption('Tic Tac Toe')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(pygame.font.get_default_font(), 72)
turn = 1
winner = replay = False

def draw_table():
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 900), 2)
    pygame.draw.line(screen, (0, 0, 0), (600, 0), (600, 900), 2)
    pygame.draw.line(screen, (0, 0, 0), (0, 300), (900, 300), 2)
    pygame.draw.line(screen, (0, 0, 0), (0, 600), (900, 600), 2)

def play_again():
    text = font.render('Click to play again', True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, textRect)

def draw_line(p1, p2):
    global winner
    winner = True
    pygame.draw.line(screen, DARK_RED, p1, p2, 30)
    play_again()

def check_win(board):
    if board[0][0] != 0 and board[0][0] == board[0][1] == board[0][2]:
        draw_line((LOW - OFFSET, LOW), (HIGH + OFFSET, LOW))
        return
    if board[1][0] != 0 and board[1][0] == board[1][1] == board[1][2]:
        draw_line((LOW - OFFSET, MID), (HIGH + OFFSET, MID))
        return
    if board[2][0] != 0 and board[2][0] == board[2][1] == board[2][2]:
        draw_line((LOW - OFFSET, HIGH), (HIGH + OFFSET, HIGH))
        return
    if board[0][0] != 0 and board[0][0] == board[1][0] == board[2][0]:
        draw_line((LOW, LOW - OFFSET), (LOW, HIGH + OFFSET))
        return
    if board[0][1] != 0 and board[0][1] == board[1][1] == board[2][1]:
        draw_line((MID, LOW - OFFSET), (MID, HIGH + OFFSET))
        return
    if board[0][2] != 0 and board[0][2] == board[1][2] == board[2][2]:
        draw_line((HIGH, LOW - OFFSET), (HIGH, HIGH + OFFSET))
        return
    if board[0][0] != 0 and board[0][0] == board[1][1] == board[2][2]:
        draw_line((LOW - OFFSET, LOW - OFFSET), (HIGH + OFFSET, HIGH + OFFSET))
        return
    if board[2][0] != 0 and board[2][0] == board[1][1] == board[0][2]:
        draw_line((HIGH + OFFSET, LOW - OFFSET), (LOW - OFFSET, HIGH + OFFSET))

def update_board(board, row, col):
    global turn
    if board[row][col] == 0: 
        board[row][col] = 1 + turn % 2
        turn += 1

def draw_player(cell, row, col):
    y = LOW if row == 0 else MID if row == 1 else HIGH
    x = LOW if col == 0 else MID if col == 1 else HIGH
    if cell == 1:
        pygame.draw.circle(screen, BLUE, (x, y), LENGTH, 10)
    elif cell == 2:
        pygame.draw.line(screen, RED, (x - LENGTH, y - LENGTH), (x + LENGTH, y + LENGTH), 10)
        pygame.draw.line(screen, RED, (x - LENGTH, y + LENGTH), (x + LENGTH, y - LENGTH), 10)
        
def main():
    global replay, winner, turn
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    run = True
    draw_table()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                row = 0 if pos[1] < 300 else 1 if pos[1] < 600 else 2
                col = 0 if pos[0] < 300 else 1 if pos[0] < 600 else 2

                if not winner:
                    update_board(board, row, col)
                    draw_player(board[row][col], row, col)
                    check_win(board)
                else:
                    replay = True

                if turn > 9:
                    play_again()
                    winner = True

            if replay:
                board = [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]
                turn = 1
                winner = replay = False   
                draw_table()            

        pygame.display.update()

if __name__ == "__main__":
    main()