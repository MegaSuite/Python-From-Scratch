'''
* ==================================================================
* Description: game_status.py
* Copyright (c) Konrad Locas.
* All rights reserved.
* Author: Konrad Locas.
* Date: 2023/03/16 15:30
* ===================================================================
'''
class GameStats():
    '''statics of the game'''
    def __init__(self,ai_settings) -> None:
        
        # initialise

        self.ai_settings=ai_settings
        self.reset_status()

        # inactivation at beginning

        self.game_active = False

        # highest score

        self.high_score=0

    
    def reset_status(self):

        # reset ship nums

        self.ship_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1