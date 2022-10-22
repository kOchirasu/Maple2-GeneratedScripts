""" trigger/61000010_me/goal.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='gameStart', value=1):
            return 결승점()


class 결승점(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=102, isOnlyWinner=True, expRate=1)
        mini_game_give_reward(winnerBoxId=102, contentType='MiniGameType2')
        end_mini_game(winnerBoxId=102, isOnlyWinner='true', gameName='shanghairunner')
        add_buff(boxIds=[102], skillId=70000019, level=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 결승점()


class 종료(state.State):
    pass

