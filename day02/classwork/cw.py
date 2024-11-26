
import pygame
import random
import sys

# ინიციალიზაცია
pygame.init()

# ეკრანის ზომა
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("მოძრაობის თამაში")

# ფერები
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# პერსონაჟის პარამეტრები
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_velocity = 5

# დაბრკოლებების პარამეტრები
obstacle_width = 50
obstacle_height = 50
obstacle_velocity = 5
obstacles = []

# მთავარი ციკლი
clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, player_width, player_height))

def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

def handle_obstacles(obstacles):
    global player_x, player_y
    for obstacle in obstacles:
        obstacle[1] += obstacle_velocity
        if obstacle[1] > screen_height:
            obstacles.remove(obstacle)
            obstacles.append([random.randint(0, screen_width - obstacle_width), -obstacle_height])
        if player_x < obstacle[0] + obstacle_width and player_x + player_width > obstacle[0]:
            if player_y < obstacle[1] + obstacle_height and player_y + player_height > obstacle[1]:
                return True
    return False

while True:
    screen.fill(WHITE)

    # საგნების მიღება
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # კლავიატურის კონტროლი
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_velocity
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_velocity
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_velocity
    if keys[pygame.K_DOWN] and player_y < screen_height - player_height:
        player_y += player_velocity

    # დაბრკოლებების შექმნა
    if random.random() < 0.02:
        obstacles.append([random.randint(0, screen_width - obstacle_width), -obstacle_height])

    # დაბრკოლებების მოძრაობა და შეჯახება
    if handle_obstacles(obstacles):
        font = pygame.font.SysFont("Arial", 50)
        text = font.render("თამაშის დასასრული!", True, (255, 0, 0))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.wait(2000)  # 2 წამით გაჩერება
        break

    # გადმოწერა
    draw_player(player_x, player_y)
    draw_obstacles(obstacles)

    pygame.display.update()
    clock.tick(60)
    
