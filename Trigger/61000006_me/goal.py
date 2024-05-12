""" trigger/61000006_me/goal.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='gameStart', value=1):
            return 결승점(self.ctx)


class 결승점(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=401, is_only_winner=True, exp_rate=1)
        self.mini_game_give_reward(winner_box_id=401, content_type='miniGame')
        self.end_mini_game(winner_box_id=401, is_only_winner='true', game_name='crazyrunner')
        self.add_buff(box_ids=[401], skill_id=70000019, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 결승점(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
