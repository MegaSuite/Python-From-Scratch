'''
* ==================================================================
* Description: alien_invasion.py
* Copyright (c) Konrad Locas.
* All rights reserved.
* Author: Konrad Locas.
* Date: 2023/03/16 15:13
* ===================================================================
'''
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_status import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():

    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Catch Colonel Sanders")
    stats=GameStats(ai_settings)
    play_button=Button(ai_settings,screen,"Play")
    scb=Scoreboard(ai_settings,screen,stats)

    # create the ship

    ship=Ship(ai_settings,screen)

    # create a group

    bullets=Group()
    aliens=Group()

    # create aliens

    gf.create_fleet(ai_settings,screen,ship,aliens)

    # main circulation

    while True:
    
    # check the events

        gf.check_events(ai_settings,screen,stats,scb,play_button,ship,aliens,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,scb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,scb,ship,aliens,bullets)
        
        gf.update_screen(ai_settings,screen,stats,scb,ship,aliens,bullets,play_button)


run_game()
