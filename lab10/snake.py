import pygame as pg
import random
import time
import psycopg2 as psg

# Pygame кітапханасын бастау
pg.init()

# Терезе өлшемдері, блок өлшемі және FPS
W, H = 800, 800
BS = 50
FPS = 10

# Экранды орнату
screen = pg.display.set_mode((W, H))
pg.display.set_caption("Snake!")
clock = pg.time.Clock()

# Қаріпті орнату
font = pg.font.Font('MICKEY.TTF', 30)

def get_username():
    input_box = pg.Rect(W // 2 - 100, H // 2 - 30, 200, 50)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font_input = pg.font.Font('MICKEY.TTF', 40)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # Toggle input box
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN and text.strip() != '':
                        return text.strip()
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((13, 17, 23))
        prompt = font_input.render("Enter Username:", True, "WHITE")
        screen.blit(prompt, (W // 2 - prompt.get_width() // 2, H // 2 - 100))

        txt_surface = font_input.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)

username = get_username()

conn = psg.connect(host="localhost", dbname="snake", user="postgres", password="Nurik_2006", port=5432)
cur = conn.cursor()

# Create user table
cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
);""")

# Create score table
cur.execute("""CREATE TABLE IF NOT EXISTS user_score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    score INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1
);""")

conn.commit()
# Insert user if not exists
cur.execute("SELECT id FROM users WHERE username = %s", (username,))
row = cur.fetchone()

if row is None:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, 0, 1)", (user_id,))
    conn.commit()  # ← add this here to make sure user is saved

else:
    user_id = row[0]

# Get current score/level
cur.execute("SELECT score, level FROM user_score WHERE user_id = %s", (user_id,))
user_score_row = cur.fetchone()
start_score, start_level = user_score_row[0], user_score_row[1]



def show_menu():
    menu_font = pg.font.Font('MICKEY.TTF', 30)
    text = menu_font.render("Paused - Press Enter to Continue", True, "WHITE")
    text_rect = text.get_rect(center=(W // 2, H // 2))

    # --- NEW: Save score to database on pause ---
    cur.execute("UPDATE user_score SET score = %s WHERE  id = %s", (snake.score, user_id))
    conn.commit()

    while True:
        screen.fill((30, 30, 30))
        screen.blit(text, text_rect)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:  # Continue
                    return


def game_over(score, level):
    font = pg.font.Font('MICKEY.TTF', 50)
    game_over_text = font.render("Game Over!", True, "RED")
    score_text = font.render(f"Score: {score}  Level: {level}", True, "WHITE")
    restart_text = font.render("Press Enter to Restart", True, "WHITE")
    quit_text = font.render("Press ESC to Quit", True, "WHITE")

    # Get the center for all texts
    game_over_rect = game_over_text.get_rect(center=(W // 2, H // 3))
    score_rect = score_text.get_rect(center=(W // 2, H // 2))
    restart_rect = restart_text.get_rect(center=(W // 2, H // 1.5))
    quit_rect = quit_text.get_rect(center=(W // 2, H // 1.3))

    while True:
        screen.fill((13, 17, 23))  # Set background color
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)
        screen.blit(restart_text, restart_rect)
        screen.blit(quit_text, quit_rect)

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:  # Restart the game
                    return True
                elif event.key == pg.K_ESCAPE:  # Quit the game
                    pg.quit()
                    exit()


# Торды салу функциясы
def drawField():
    for i in range(0, W, BS):
        for j in range(0, H, BS):
            rect = pg.Rect(i, j, BS, BS)
            pg.draw.rect(screen, (21, 27, 35), rect, 1)

# Ұпай мен деңгей көрсететін функция
def drawtext(score, level):
    score_text = font.render(f"Score: {score}  Level: {level}", True, "WHITE")
    screen.blit(score_text, (10, 10))

# Жылан класы
class Snake:
    def __init__(self):
        self.x, self.y = BS, BS  # Starting coordinates
        self.xdir, self.ydir = 1, 0  # Starting direction (right)
        self.head = pg.Rect(self.x, self.y, BS, BS)
        self.body = [pg.Rect(self.x - BS, self.y, BS, BS)]  # Body starts with one block
        self.dead = False
        self.score = 0
        self.level = 1
    
    def move(self):
        # If snake goes out of bounds or collides with its body, restart the game
        if self.head.x not in range(0, W) or self.head.y not in range(0, H) or any(self.head.colliderect(i) for i in self.body):
            # Update the score in the database
            cur.execute("UPDATE user_score SET score = %s, level = %s WHERE user_id = %s", (self.score, self.level, user_id))
            conn.commit()

            self.dead = True  # Trigger Game Over
            return  # Stop moving

        
        # Add new head to the body
        self.body.append(self.head.copy())
        self.head.x += self.xdir * BS
        self.head.y += self.ydir * BS
        self.body.pop(0)  # Remove the last segment (unless eating food)



    def draw(self, surf):
        pg.draw.rect(surf, (0, 255, 0), self.head)  # Бас бөлігі
        for part in self.body:
            pg.draw.rect(surf, "green", part)  # Дене бөліктері

# Жеміс класы
class Food:
    def __init__(self):
        self.generate()
    
    def generate(self):
        # Жемістің координаттарын кездейсоқ таңдау
        self.x = random.randint(0, W - BS) // BS * BS
        self.y = random.randint(0, H - BS) // BS * BS
        self.value = random.choice([(5, "red"), (10, "blue"), (15, "yellow")])  # Жемнің ұпайы мен түсі
        self.color = self.value[1]
        self.points = self.value[0]
        self.spawn_time = time.time()  # Шыққан уақыт
    
    def draw(self, surf):
        # Жемісті шеңбер ретінде салу
        pg.draw.circle(surf, self.color, (self.x + BS // 2, self.y + BS // 2), BS // 2)
    
    def expired(self):
        # Егер жем 5 секундтан артық тұрса, жарамсыз деп саналады
        return time.time() - self.spawn_time > 5 

# Ойын нысандарын жасау
snake = Snake()
snake.score = start_score
snake.level = snake.score // 10 + 1  # Restore level from score
food = Food()

# Негізгі цикл
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        # Басқару пернелері
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a and snake.xdir == 0:
                snake.xdir, snake.ydir = -1, 0  # Солға
            elif event.key == pg.K_d and snake.xdir == 0:
                snake.xdir, snake.ydir = 1, 0  # Оңға
            elif event.key == pg.K_w and snake.ydir == 0:
                snake.xdir, snake.ydir = 0, -1  # Жоғары
            elif event.key == pg.K_s and snake.ydir == 0:
                snake.xdir, snake.ydir = 0, 1  # Төмен
            elif event.key == pg.K_ESCAPE:
                show_menu()

    
    # Экранды жаңарту

    snake.move()

    # If snake is dead, show Game Over screen
    if snake.dead:
        if game_over(snake.score, snake.level):  # Restart game if user presses Enter
            snake = Snake()  # Reset the snake object
            food = Food()  # Regenerate food
            continue  # Continue the game loop after resetting

    screen.fill((13, 17, 23))  # Clear the screen
    drawField()
    drawtext(snake.score, snake.level)

    # Handle food and snake collision
    snake.draw(screen)
    food.draw(screen)

    if snake.head.colliderect(pg.Rect(food.x, food.y, BS, BS)):  # If snake eats food
        snake.body.append(pg.Rect(snake.body[-1].x, snake.body[-1].y, BS, BS))
        snake.score += food.points
        snake.level = snake.score // 10 + 1
        food.generate()

    # Егер жем ескі болса, жаңасын шығару
    if food.expired():
        food.generate()
    
    # Экранды жаңарту және жылдамдықты FPS + деңгей бойынша өзгерту
    pg.display.update()
    clock.tick(FPS + snake.level - 1)

# Ойын жабу
pg.quit()
