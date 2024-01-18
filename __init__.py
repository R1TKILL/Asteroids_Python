import pygame

from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

widthWindow = 900
heightWindow = 500
window = pygame.display.set_mode((widthWindow, heightWindow))
pygame.display.set_caption("Asteroids")

FPS = pygame.time.Clock()

# anurati,vaoi,AG 10,191,NDS12,Arredamento
textFormatMenu = pygame.font.SysFont('AG 10,191', 35, True, True)
textFormatStart = pygame.font.SysFont('Arredamento', 22, True, True)

textFormat = pygame.font.SysFont('arial', 22, False, True)

textFormat2 = pygame.font.SysFont('arial', 35, True, True)
textFormat3 = pygame.font.SysFont('arial', 18, True, True)

music_menu = pygame.mixer.Sound('../Asteroids_python/musics/main_menu.wav')
music_boss = pygame.mixer.Sound('../Asteroids_python/musics/boss.wav')#Não to usando ainda.
music_back = pygame.mixer.Sound('../Asteroids_python/musics/backmusic.wav')
music_defeats = pygame.mixer.Sound('../Asteroids_python/musics/defeat.wav')
music_points = pygame.mixer.Sound('../Asteroids_python/musics/points.wav')#Muito baixa, trocar.

spaceCraft = pygame.image.load("../Asteroids_python/images/nave4.gif")
spaceCraft = pygame.transform.scale_by(spaceCraft, 0.5)

#Em manuntenção.
def boss():
    pass


def draw_stars(x):
    y_star = randint(0, widthWindow)
    x_star = randint(0, x)
    pygame.draw.circle(window, (255, 255, 255), (x_star, y_star), 5)
    pygame.draw.circle(window, (255, 255, 255), (x_star, y_star), 5)
    y_star += 10
    if y_star >= heightWindow:
        randint(0, 0)
        randint(0, widthWindow)


def defeatCraft():
    defeat = True
    while defeat:
        window.fill((0, 0, 0))
        music_defeats.play()
        music_defeats.set_volume(0.2)
        labelDefeat = "Game Over"
        formatacaoDefeat = textFormat2.render(labelDefeat, True, (255, 0, 0))
        window.blit(formatacaoDefeat, (340, 150))

        labelReset = "Pressione R para continuar..."
        formatacaoReset = textFormat3.render(labelReset, True, (255, 0, 0))
        window.blit(formatacaoReset, (310, 220))

        labelMenu = "Pressione ESC para voltar ao menu principal"
        formatacaomenu = textFormat3.render(labelMenu, True, (255, 0, 0))
        window.blit(formatacaomenu, (250, 250))

        for event in pygame.event.get():
            if event.type == QUIT:
                music_defeats.stop()
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    music_defeats.stop()
                    game()
                if event.key == 27:  # Esc
                    music_defeats.stop()
                    menu(spaceCraft)
        pygame.display.update()


def game():
    x_craft = 190
    y_craft = 380

    x_gun = widthWindow - 10
    y_gun = heightWindow
    dispatch_gun = False

    postionY1 = 0
    postionY2 = 0
    postionY3 = 0
    postionX1 = randint(0, 470)
    postionX2 = randint(0, 470)
    postionX3 = randint(0, 470)
    postionX4 = randint(0, 470)
    postionX5 = randint(0, 470)
    postionX6 = randint(0, 470)

    postionXhealth = randint(0, 470)
    postionYhealth = -8000


    points = 0
    distance = 0

    music_back.play(-1)
    music_defeats.set_volume(0.2)

    # Para a barra de vida.
    color_bar = (0, 255, 0)
    increment_bar = 300
    width_health = 300

    while True:
        distance += 1
        FPS.tick(60)
        window.fill((0, 0, 0))

        labelPontos = f"Pontos: {points}"
        format = textFormat.render(labelPontos, True, (255, 255, 255))
        labelDistance = f"Distância: {distance}"
        formatDistance = textFormat.render(labelDistance, True, (255, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            # Desnhando o tiro na tela.
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    dispatch_gun = True
                    x_gun = x_craft + 59
                    y_gun = y_craft + 50
                    pygame.draw.rect(window, (255, 0, 0), (x_gun, y_gun, 10, 30))

        if width_health != increment_bar:
            width_health += 1
        else:
            width_health = width_health

        if increment_bar != width_health:
            increment_bar -= 1
        else:
            increment_bar = increment_bar

        # Barras de vida do Player.
        # Serve só para o suporte das outras.
        pygame.draw.rect(window, (255, 255, 255), (540, 30, 308, 25), 4)
        # Barra que muda de cor para verde quando ganha life e para amarelo quando perde life.
        pygame.draw.rect(window, color_bar, (544, 34, increment_bar, 17))
        # Sobe aconpando a de cima e desce rapidamente fazendo a de cima a aconpanha-lá.
        pygame.draw.rect(window, (255, 0, 0), (544, 34, width_health, 17))

        # Controlando para não passar dos limites do suporte
        if width_health >= 300:
            width_health = 300
        elif increment_bar >= 300:
            increment_bar = 300
        elif width_health <= 0:
            width_health = 0
        elif increment_bar <= 0:
            increment_bar = 0

        # Elementos da tela.
        # Nave e tiro.
        objectCraft = pygame.draw.rect(window, (0, 0, 0), (x_craft + 44, y_craft + 30, 40, 70))
        gun = pygame.draw.rect(window, (255, 255, 0), (x_gun, y_gun, 10, 30))

        # Méteoros e vida talvez um boss
        asteroid1 = pygame.draw.rect(window, (255, 0, 0), (postionX1, postionY1, 30, 30))
        asteroid2 = pygame.draw.rect(window, (255, 0, 0), (postionX2, postionY2, 30, 30))
        asteroid3 = pygame.draw.rect(window, (255, 0, 0), (postionX3, postionY3, 30, 30))
        asteroid4 = pygame.draw.rect(window, (255, 0, 0), (postionX4, postionY1, 30, 30))
        asteroid5 = pygame.draw.rect(window, (255, 0, 0), (postionX5, postionY2, 30, 30))
        asteroid6 = pygame.draw.rect(window, (255, 0, 0), (postionX6, postionY3, 30, 30))

        up_health = pygame.draw.rect(window, (0, 255, 0), (postionXhealth, postionYhealth, 30, 30))

        postionY1 += 3
        postionY2 += 2
        postionY3 += 4
        postionYhealth += 4
        # Para ficar no loop.
        if postionY1 >= heightWindow:
            postionY1 = 0
            postionX1 = randint(0, 470)
            postionX4 = randint(0, 470)
        if postionY2 >= heightWindow:
            postionY2 = 0
            postionX2 = randint(0, 470)
            postionX5 = randint(0, 470)
        if postionY3 >= heightWindow:
            postionY3 = 0
            postionX3 = randint(0, 470)
            postionX6 = randint(0, 470)
        if postionYhealth >= heightWindow:
            postionYhealth = -8000
            postionXhealth = randint(0, 470)

        # Fundo estelar.
        draw_stars(500)

        # Para o tiro subir.
        if dispatch_gun:
            y_gun -= 50
        if y_gun <= -30:
            dispatch_gun = False
            y_gun = heightWindow

        # Verificando se a colisão entre tiro e asteroids e nave.
        #Tiros
        if gun.colliderect(asteroid1):
            points += 1
            postionX1 = widthWindow
        if gun.colliderect(asteroid2):
            points += 1
            postionX2 = widthWindow
        if gun.colliderect(asteroid3):
            points += 1
            postionX3 = widthWindow
        if gun.colliderect(asteroid4):
            points += 1
            postionX4 = widthWindow
        if gun.colliderect(asteroid5):
            points += 1
            postionX5 = widthWindow
        if gun.colliderect(asteroid6):
            points += 1
            postionX6 = widthWindow
        #asteroids
        if asteroid1.colliderect(objectCraft):
            if width_health > 0:
                width_health -= 5
                color_bar = (255, 255, 0)
            else:
                music_back.stop()
                defeatCraft()
        if asteroid2.colliderect(objectCraft):
            if width_health > 0:
                width_health -= 5
                color_bar = (255, 255, 0)
            else:
                music_back.stop()
                defeatCraft()
        if asteroid3.colliderect(objectCraft):
            if width_health > 0:
                width_health -= 5
                color_bar = (255, 255, 0)
            else:
                music_back.stop()
                defeatCraft()
        if asteroid4.colliderect(objectCraft):
            if width_health > 0:
                width_health -= 5
                color_bar = (255, 255, 0)
            else:
                music_back.stop()
                defeatCraft()
        if asteroid5.colliderect(objectCraft):
            if width_health > 0:
                width_health -= 5
                color_bar = (255, 255, 0)
            else:
                music_back.stop()
                defeatCraft()
        if asteroid6.colliderect(objectCraft):
            if width_health > 0:
                width_health -= 5
                color_bar = (255, 255, 0)
            else:
                music_back.stop()
                defeatCraft()
        if up_health.colliderect(objectCraft):
            if width_health < 300:
                increment_bar += 5
                color_bar = (0, 255, 0)
            else:
                width_health = 300
                increment_bar = 300

        #Chamando o boss
        if distance == 15000:
            if points >= 300:
                print("Chefão.")
            else:
                defeatCraft()

        # Movimentação do player.
        if x_craft < -40:
            x_craft = -40
        if x_craft >= 410:
            x_craft = 410

        if pygame.key.get_pressed()[K_a]:
            x_craft = x_craft - 5
        if pygame.key.get_pressed()[K_d]:
            x_craft = x_craft + 5

        #Separa o menu.
        pygame.draw.line(window, (255, 255, 0), (500, 0), (500, 600), 7)

        window.blit(format, (530, 80))
        window.blit(formatDistance, (720,80))
        window.blit(spaceCraft, (x_craft, y_craft))
        pygame.display.update()


def menu(spaceCraft):
    spaceCraft = pygame.transform.scale_by(spaceCraft, 1.9)
    while True:
        window.fill((0, 0, 0))
        music_menu.play()
        music_menu.set_volume(0.5)

        labelMainMenu = "ASTEROIDS"
        formatacaoMainMenu = textFormatMenu.render(labelMainMenu, True, (255, 0, 0))
        labelStart = "Pressione Enter para iniciar o jogo"
        formatacaoStart = textFormatStart.render(labelStart, True, (255, 0, 0))

        draw_stars(widthWindow)

        for event in pygame.event.get():
            if event.type == QUIT:
                music_defeats.stop()
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == 13:  # Enter
                    music_menu.stop()
                    game()

        window.blit(spaceCraft, (330, 120))
        window.blit(formatacaoMainMenu, (270, 60))
        window.blit(formatacaoStart, (225, 410))
        pygame.display.update()


menu(spaceCraft)