import pygame
import Player
import Card
import os

playerOne = Player.Player()
playerOne.create_player("Player 1")


pygame.init()
pygame.display.init()
bg = pygame.image.load("oGameBoard.jpg")
forest = pygame.image.load("Forest.jpg")
forest = pygame.transform.scale(forest, (75, 100))
forest3rect = pygame.Rect(80, 670, 75, 100)
visionaryrect = pygame.Rect(175, 700, 75, 100)
tuskerrect = pygame.Rect(250, 700, 75, 100)
mystic = pygame.image.load("Mystic.jpg")
visionary = pygame.image.load("visionary.jpg")
visionary = pygame.transform.scale(visionary, (75, 100))
packleader = pygame.image.load("packleader.jpg")
packleader = pygame.transform.scale(packleader, (75, 100))
tusker = pygame.image.load("tusker.jpg")
tusker = pygame.transform.scale(tusker, (75, 100))
mystic = pygame.transform.scale(mystic, (75, 100))
visionary = pygame.transform.scale(visionary, (75, 100))
tusker = pygame.transform.scale(tusker, (75, 100))
packleader = pygame.transform.scale(packleader, (75, 100))
lifeFont = pygame.font.SysFont("comicsansms", 19)
manaFont = pygame.font.SysFont("comicsansms", 14)
lifeTotal = lifeFont.render(str(playerOne.lifePoints), True, (0, 0, 0))
whiteMana = manaFont.render(str(playerOne.mana['White']), True, (255, 255, 255))
blueMana = manaFont.render(str(playerOne.mana['Blue']), True, (255, 255, 255))
blackMana = manaFont.render(str(playerOne.mana['Black']), True, (255, 255, 255))
redMana = manaFont.render(str(playerOne.mana['Red']), True, (255, 255, 255))
greenMana = manaFont.render(str(playerOne.mana['Green']), True, (255, 255, 255))
totalMana = manaFont.render(str(playerOne.mana['Green']), True, (255, 255, 255))


screen = pygame.display.set_mode((689, 800), pygame.RESIZABLE)
done = False
clock = pygame.time.Clock()
angle = 90
tapped = False
tapped2 = False
tapped3 = False
x = 175
y = 700

x1 = 250
y1 = 700

x2 = 1000
y2 = 1000


while not done:

    screen.fill([255, 255, 255])
    screen.blit(bg, (0, 0))
    screen.blit(lifeTotal,
                (622 - lifeTotal.get_width() // 2, 457 - lifeTotal.get_height() // 2))
    screen.blit(whiteMana,
                (545 - lifeTotal.get_width() // 2, 553 - lifeTotal.get_height() // 2))
    screen.blit(blueMana,
                (545 - lifeTotal.get_width() // 2, 567 - lifeTotal.get_height() // 2))
    screen.blit(blackMana,
                (545 - lifeTotal.get_width() // 2, 581 - lifeTotal.get_height() // 2))
    screen.blit(redMana,
                (545 - lifeTotal.get_width() // 2, 595 - lifeTotal.get_height() // 2))
    screen.blit(greenMana,
                (545 - lifeTotal.get_width() // 2, 609 - lifeTotal.get_height() // 2))
    screen.blit(totalMana,
                (545 - lifeTotal.get_width() // 2, 627 - lifeTotal.get_height() // 2))

    screen.blit(forest, (40, 670))
    screen.blit(forest, (60, 670))
    screen.blit(forest, (80, 670))
    screen.blit(mystic, (40, 430))
    screen.blit(visionary, (x, y))
    screen.blit(packleader, (x2, y2))
    screen.blit(tusker, (x1, y1))



    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_coordinates = pygame.mouse.get_pos()
            if forest3rect.collidepoint(mouse_coordinates):
                print('Tap!')
                forest = pygame.transform.rotate(forest, angle)
                if not tapped:
                    playerOne.mana['Green'] += 3
                    tapped = True
                angle = 0
                if angle > 90:
                    angle = 90
                greenMana = manaFont.render(str(playerOne.mana['Green']), True, (255, 255, 255))
                print(playerOne.mana['Green'])
            if visionaryrect.collidepoint(mouse_coordinates):
                if not tapped2:
                    playerOne.mana['Green'] -= 1
                    tapped2 = True
                greenMana = manaFont.render(str(playerOne.mana['Green']), True, (255, 255, 255))
                x = 115
                y = 430
                x2 = 325
                y2 = 700
            if tuskerrect.collidepoint(mouse_coordinates):
                if not tapped3:
                    playerOne.mana['Green'] -= 2
                    tapped3 = True
                greenMana = manaFont.render(str(playerOne.mana['Green']), True, (255, 255, 255))
                x1 = 150
                x2 = 430

        if event.type == pygame.QUIT:
            done = True





    pygame.display.flip()
    clock.tick(60)
