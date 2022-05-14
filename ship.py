import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')  # Wczytanie obrazu statku i pobranie jego prostokąta
        self.rect = self.image.get_rect()  # dostęp do atrybutu powierzchni
        self.screen_rect = screen.get_rect()  # umieszczmy wymiary ekranu w atrybusie self.screen_rect
        self.ai_settings = ai_settings

        # Każdy nowy statek kosmiczny pojawia się na dole ekranu
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False  # opcja wskazująca na poruszanie sie statku
        self.moving_left = False
        self.center = float(self.rect.centerx)

    def update(self):
        """Uaktulanienie połozenia statku na podstawie opcji wskazującej na jego ruch"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Wyswietlanie statku w jego aktulanym połozeniu"""
        self.screen.blit(self.image, self.rect)