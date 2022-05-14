import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Klasa przedstawaiająca pojedynczego obcego we flocie"""
    def __init__(self, ai_settings, screen):
        """Inicjalizacja obcego i zdefiniowanie jego połozenia początkowego"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()  # zdefiniowanie obrazu obcego jako prostokąt
        # umieszczenie nowego obcego w poblizu lewego górnego rogu ekranu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)  # przechowanie dokładnego połozenia obcego


    def blitme(self):
        """Wyswietlanie obcego w jego aktulanym połozeniu"""
        self.screen.blit(self.image, self.rect)