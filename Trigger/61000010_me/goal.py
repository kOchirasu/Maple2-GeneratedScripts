""" trigger/61000010_me/goal.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='gameStart', value=1):
            return 결승점(self.ctx)


class 결승점(trigger_api.Trigger):
    def on_enter(self):
        self.end_mini_game_round(winnerBoxId=102, isOnlyWinner=True, expRate=1)
        self.mini_game_give_reward(winnerBoxId=102, contentType='MiniGameType2')
        self.end_mini_game(winnerBoxId=102, isOnlyWinner='true', gameName='shanghairunner')
        self.add_buff(boxIds=[102], skillId=70000019, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 결승점(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
