import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Reakcja na naciśniecie klawisza"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Reakcja na zwolnienie klawisza"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Reakcja na zdarzenia generwoane przez klawiature i mysz"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Uaktulanienie obrazów na ekranie i przejscie do nowego ekranu"""
    screen.fill(ai_settings.bg_color)  # odswiezanie ekranu w trakcie kazdej iteracji petli
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)  # drow wysiwetla za pomocą pygam kazdy eleent grupy
    pygame.display.flip()  # Wyswietlanie ostatnio zmodyfikowanego ekranu


def fire_bullet(ai_settings, screen, ship, bullets):
    """Wystrzelenie pocisku jesli limit nie jest przekroczony"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)  # Utworzenie nowego pocisku i dodanie go do grupy pocisków
        bullets.add(new_bullet)


def update_bullets(bullets):
    """Uaktulanienie połozenia pocisków i usunięcie tych niewidocznych na ekranie"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(ai_settings, screen, aliens):
    """Utworzenie pełnej floty obcych."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    # utworzenie pierwszgo rzędu obcych
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
