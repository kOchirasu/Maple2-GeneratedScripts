""" trigger/81000003_item/goal.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='gameStart', value=1):
            return 결승점()


class 결승점(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=401, isOnlyWinner=True, expRate=1)
        mini_game_give_reward(winnerBoxId=401, contentType='UserOpenMiniGameExtraReward', gameName='UserMassive_Crazyrunner') # 1일 5회 추가 보너스
        end_mini_game(winnerBoxId=401, isOnlyWinner='true', gameName='UserMassive_Crazyrunner')
        add_buff(boxIds=[401], skillId=70000132, level=1)
        add_buff(boxIds=[401], skillId=70000019, level=1) # 에레브의 축복

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 결승점()


class 종료(state.State):
    pass


