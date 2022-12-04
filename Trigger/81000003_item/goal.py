""" trigger/81000003_item/goal.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='gameStart', value=1):
            return 결승점(self.ctx)


class 결승점(trigger_api.Trigger):
    def on_enter(self):
        self.end_mini_game_round(winnerBoxId=401, isOnlyWinner=True, expRate=1)
        self.mini_game_give_reward(winnerBoxId=401, contentType='UserOpenMiniGameExtraReward', gameName='UserMassive_Crazyrunner') # 1일 5회 추가 보너스
        self.end_mini_game(winnerBoxId=401, isOnlyWinner='true', gameName='UserMassive_Crazyrunner')
        self.add_buff(boxIds=[401], skillId=70000132, level=1)
        self.add_buff(boxIds=[401], skillId=70000019, level=1) # 에레브의 축복

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 결승점(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
