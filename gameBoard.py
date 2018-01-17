import pygame
import Player
import Card


import os

playerOne = Player.create_player("Player 1")


pygame.init()
pygame.display.init()
bg = pygame.image.load("C:/Users/Thomas/PycharmProjects/Magic/Images/oGameBoard.jpg")
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


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill([255, 255, 255])
    screen.blit(bg, (0,0))
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





    pygame.display.flip()
    clock.tick(60)