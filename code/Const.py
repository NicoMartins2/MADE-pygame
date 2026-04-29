import pygame

C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_BLACK = (0, 0, 0)

EVENT_TIMEOUT = pygame.USEREVENT + 2
PLAYER_SPEED = {
    'Player1': 3
}

BG_SPEED = {
    'msg1Bg': 0,
    'Level1Bg': 0,
    'msg2Bg': 0,
    'Level2Bg': 0
}

MENU_OPTION = ('Aperte ENTER para começar','')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}

SPAWN_TIME = 4000

WIN_WIDTH = 1280
WIN_HEIGHT = 720