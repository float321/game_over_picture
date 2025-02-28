import pygame
import os
import sys


pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game over')


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class GameOver(pygame.sprite.Sprite):
    image = load_image("gameover.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = GameOver.image
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.rect.y = 0

    def update(self, *args):
        if self.rect.x:
            self.rect.x += 1


if __name__ == '__main__':

    running = True
    all_sprites = pygame.sprite.Group()

    x, y = 10, 10

    GameOver(all_sprites)
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('blue')

        all_sprites.update()
        all_sprites.draw(screen)

        clock.tick(200)
        pygame.display.flip()
    pygame.quit()
