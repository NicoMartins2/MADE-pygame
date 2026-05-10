import pygame

C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_BLACK = (0, 0, 0)
C_BROWN = (128, 64, 0)

EVENT_TIMEOUT = pygame.USEREVENT + 2
PLAYER_SPEED = {
    'Player1': 3
}

BG_SPEED = {
    'msg1Bg': 0,
    'Level1Bg': 0,
    'msg2Bg': 0,
    'Level2Bg': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'msg3Bg': 0
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

LEVEL2_PLATFORMS = [
    pygame.Rect(0, WIN_HEIGHT - 100, 800, 100),
    pygame.Rect(900, WIN_HEIGHT - 100, 800, 100)
]
LEVEL2_SIGN = [
    pygame.Rect(750, WIN_HEIGHT - 150, 10, 50),
    pygame.Rect(725, WIN_HEIGHT - 140, 50, 20)
]

LEVEL3_PLATFORMS = [
    pygame.Rect(0, 650, 260, 120),   
    pygame.Rect(320, 550, 450, 170), 
    pygame.Rect(860, 500, 200, 220), 
    pygame.Rect(1110, 450, 260, 270),
]
LEVEL3_SIGN = [
    pygame.Rect(750, WIN_HEIGHT - 220, 10, 50),
    pygame.Rect(725, WIN_HEIGHT - 210, 50, 20)
]