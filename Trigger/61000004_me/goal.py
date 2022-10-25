""" trigger/61000004_me/goal.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='gameStart', value=1):
            return 결승점(self.ctx)


class 결승점(common.Trigger):
    def on_enter(self):
        self.end_mini_game_round(winnerBoxId=102, isOnlyWinner=True, expRate=1)
        self.mini_game_give_reward(winnerBoxId=102, contentType='miniGame')
        self.end_mini_game(winnerBoxId=102, isOnlyWinner='true', gameName='escape')
        self.add_buff(boxIds=[102], skillId=70000019, level=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 결승점(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
