import pygame
import os

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
bg = pygame.image.load("pitbull.png")

# Ensure correct path
songs = [os.path.join("C:/Users/Nursultan/Desktop/projects/PP2/lab7/music/", song) for song in 
         ['GiveMeEverything.mp3', 'HeyBaby.mp3', 'IKnowYouWantMe.mp3', 'MmmYeah.mp3', 'OnTheFloor.mp3']]

queue = 0
currently_playing_song = False

def play():
    global currently_playing_song
    if queue < 0 or queue >= len(songs):
        return

    if not os.path.exists(songs[queue]):
        return

    pygame.mixer.music.load(songs[queue])
    pygame.mixer.music.play()
    currently_playing_song = True
    print(f"Playing: {songs[queue]}")

def stop():
    global currently_playing_song
    pygame.mixer.music.stop()
    currently_playing_song = False

def playnext():
    global queue
    queue = (queue + 1) % len(songs)
    play()

def playprev():
    global queue
    queue = (queue - 1) % len(songs) 
    play()

play()  

run = True
while run:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playprev()
            elif event.key == pygame.K_RIGHT:
                playnext()
            elif event.key == pygame.K_SPACE:
                if currently_playing_song:
                    pygame.mixer.music.pause()
                    currently_playing_song = False
                else:
                    pygame.mixer.music.unpause()
                    currently_playing_song = True
            elif event.key == pygame.K_q:
                stop()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
