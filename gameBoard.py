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
mystic = pygame.image.load("Mystic.jpg")
mystic = pygame.transform.scale(mystic, (75, 100))
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

    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_coordinates = pygame.mouse.get_pos()
            if forest3rect.collidepoint(mouse_coordinates):
                print('Tap!')
                forest = pygame.transform.rotate(forest, angle)
                angle = 270
                if angle >= 360:
                    angle = 90
                screen.blit(forest, (75, 100))
                playerOne.mana['Green'] += 3

        if event.type == pygame.QUIT:
            done = True





    pygame.display.flip()
    clock.tick(60)
