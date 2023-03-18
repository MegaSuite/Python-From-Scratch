'''
* ==================================================================
* Description: game_functions.py
* Copyright (c) Konrad Locas.
* All rights reserved.
* Author: Konrad Locas.
* Date: 2023/03/16 15:13
* ===================================================================
'''
import sys
import pygame

from bullet import Bullet
from alien import Alien
from time import sleep

def get_number_aliens_x(ai_settings,alien_width):
    available_space_x=ai_settings.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(3*alien_width))
    return number_aliens_x


def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y=(ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows=int(available_space_y/(2.5*alien_height))
    return number_rows


def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=10+alien_width+3*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)


def create_fleet(ai_settings,screen,ship,aliens):

    '''create aliens'''
    
    alien=Alien(ai_settings,screen)
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    # create the rows of aliens
    
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)


def check_keydown_events(event,ai_settings,screen,ship,bullets):

    if event.key==pygame.K_RIGHT:
        ship.move_right=True
    elif event.key==pygame.K_LEFT:
        ship.move_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)
    elif event.key==pygame.K_LALT:
        sys.exit()


def fire_bullets(ai_settings,screen,ship,bullets):
        
        # create a bullet and add it to the group

        if len(bullets)<ai_settings.bullet_allowed:
            new_bullet=Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)


def check_keyup_events(event,ship):

    if event.key==pygame.K_RIGHT:
        ship.move_right=False
    elif event.key==pygame.K_LEFT:
        ship.move_left=False
        

def check_events(ai_settings,screen,stats,scb,play_button,ship,aliens,bullets):

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,scb,play_button,ship,aliens,bullets,mouse_x,mouse_y)


def check_play_button(ai_settings,screen,stats,scb,play_button,ship,aliens,bullets,mouse_x,mouse_y):

    '''on tapping the play button , start the  game'''

    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)

    if button_clicked and not stats.game_active:

        # reset the settings

        ai_settings.initialise_dynamic_settings()

        # hide the cursor
        pygame.mouse.set_visible(False)

        stats.reset_status()
        stats.game_active=True

        # reset the scoreboard

        scb.prep_high_score()
        scb.prep_score()
        scb.prep_level()
        scb.prep_ships()

        # clean the list of aliens and bullets

        aliens.empty()
        bullets.empty()

        # create a new fleet of aliens and place a ship on the bottom of the screen

        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()



def update_screen(ai_settings,screen,stats,scb,ship,aliens,bullets,play_button):

    '''redraw the screen in each circulation'''
     
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # show the score
    
    scb.show_score()

    # if it's inactive ,draw the button

    if not stats.game_active:
        play_button.draw_button()

    # display the drawn screen

    pygame.display.flip()


def update_bullets(ai_settings,screen,stats,scb,ship,aliens,bullets):
    
    bullets.update()
    
    # delete the bullets outside the screen

    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(ai_settings,screen,stats,scb,ship,aliens,bullets)


def check_bullet_alien_collisions(ai_settings,screen,stats,scb,ship,aliens,bullets):

    # delete the bullets and ships came across

    collisons=pygame.sprite.groupcollide(bullets,aliens,True,True)

    if collisons:
        for aliens in collisons.values():
            stats.score += ai_settings.alien_points*len(aliens)
            scb.prep_score()
        check_high_score(stats,scb)

    # create new alien fleets

    if len(aliens)==0:
        bullets.empty()
        ai_settings.increase_speed()

        # upgrade 

        stats.level += 1
        scb.prep_level()

        create_fleet(ai_settings,screen,ship,aliens)


def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break




def change_fleet_direction(ai_settings,aliens):
    '''downward and change direction'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *=-1


def ship_hit(ai_settings,stats,scb,screen,ship,aliens,bullets):
    
    '''renew the ship hit'''

    # change the activation according to the No. of ships left

    if stats.ship_left > 0:

        stats.ship_left -= 1

        # update the scoreboard

        scb.prep_ships()

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    # clean the list of aliens and bullets

    aliens.empty()
    bullets.empty()

    # create a new fleet of aliens and place a ship on the bottom of the screen

    create_fleet(ai_settings,screen,ship,aliens)
    ship.center_ship()

    # pause

    sleep(0.5)


def check_alien_bottom(ai_settings,stats,scb,screen,ship,aliens,bullets):

    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:

            # deal it like the collision of the ship and aliens

            ship_hit(ai_settings,stats,screen,scb,ship,aliens,bullets)
            break


def update_aliens(ai_settings,screen,stats,scb,ship,aliens,bullets):

    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    # collisions on aliens and ship

    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,scb,screen,ship,aliens,bullets)

    # check the aliens arriving the bottom

    check_alien_bottom(ai_settings,stats,scb,screen,ship,aliens,bullets)


def check_high_score(stats,scb):

    # check if there's new highest

    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scb.prep_high_score()