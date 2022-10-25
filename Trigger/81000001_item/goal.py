""" trigger/81000001_item/goal.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='gameStart', value=1):
            return 결승점(self.ctx)


class 결승점(common.Trigger):
    def on_enter(self):
        self.end_mini_game_round(winnerBoxId=102, isOnlyWinner=True, expRate=1)
        self.mini_game_give_reward(winnerBoxId=102, contentType='UserOpenMiniGameExtraReward', gameName='UserMassive_Escape') # 1일 5회 추가 보너스
        self.end_mini_game(winnerBoxId=102, isOnlyWinner='true', gameName='UserMassive_Escape')
        self.add_buff(boxIds=[102], skillId=70000132, level=1)
        self.add_buff(boxIds=[102], skillId=70000019, level=1) # 에레브의 축복 버프 걸어줌

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 결승점(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
