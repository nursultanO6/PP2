import pygame as pg
import random
import time

pg.init()

W, H = 800, 800
BS = 50
FPS = 10

screen = pg.display.set_mode((W, H))
pg.display.set_caption("Snake!")
clock = pg.time.Clock()

font = pg.font.Font('MICKEY.TTF', 30)

def drawField():
    for i in range(0, W, BS):
        for j in range(0, H, BS):
            rect = pg.Rect(i, j, BS, BS)
            pg.draw.rect(screen, (21, 27, 35), rect, 1)

def drawtext(score, level):
    score_text = font.render(f"Score: {score}  Level: {level}", True, "WHITE")
    screen.blit(score_text, (10, 10))

class Snake:
    def __init__(self):
        self.x, self.y = BS, BS
        self.xdir, self.ydir = 1, 0
        self.head = pg.Rect(self.x, self.y, BS, BS)
        self.body = [pg.Rect(self.x - BS, self.y, BS, BS)]
        self.dead = False
        self.score = 0
        self.level = 1
    
    def move(self):
        if self.head.x not in range(0, W) or self.head.y not in range(0, H) or any(self.head.colliderect(i) for i in self.body):
            self.__init__()  
        
        self.body.append(self.head.copy())
        self.head.x += self.xdir * BS
        self.head.y += self.ydir * BS
        self.body.pop(0)
    
    def draw(self, surf):
        pg.draw.rect(surf, (0, 255, 0), self.head)
        for part in self.body:
            pg.draw.rect(surf, "green", part)

class Food:
    def __init__(self):
        self.generate()
    
    def generate(self):
        self.x = random.randint(0, W - BS) // BS * BS
        self.y = random.randint(0, H - BS) // BS * BS
        self.value = random.choice([(5, "red"), (10, "blue"), (15, "yellow")])  
        self.color = self.value[1]
        self.points = self.value[0]
        self.spawn_time = time.time()
    
    def draw(self, surf):
        pg.draw.circle(surf, self.color, (self.x + BS // 2, self.y + BS // 2), BS // 2)
    
    def expired(self):
        return time.time() - self.spawn_time > 5 

snake = Snake()
food = Food()
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a and snake.xdir == 0:
                snake.xdir, snake.ydir = -1, 0
            elif event.key == pg.K_d and snake.xdir == 0:
                snake.xdir, snake.ydir = 1, 0
            elif event.key == pg.K_w and snake.ydir == 0:
                snake.xdir, snake.ydir = 0, -1
            elif event.key == pg.K_s and snake.ydir == 0:
                snake.xdir, snake.ydir = 0, 1
    
    screen.fill((13, 17, 23))
    drawField()
    drawtext(snake.score, snake.level)
    
    snake.move()
    snake.draw(screen)
    food.draw(screen)
    
    if snake.head.x == food.x and snake.head.y == food.y:
        snake.body.append(pg.Rect(snake.body[-1].x, snake.body[-1].y, BS, BS))
        snake.score += food.points
        snake.level = snake.score // 10 + 1 
        food.generate()
    
    if food.expired():
        food.generate()
    
    pg.display.update()
    clock.tick(FPS + snake.level - 1)
pg.quit()