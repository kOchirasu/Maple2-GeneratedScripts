""" trigger/02020027_bf/02020027_timer.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Timer', value=1):
            return 타이머시작(self.ctx)


class 타이머시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='BattleTimer', seconds=300, startDelay=1, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 타이머체크(self.ctx)


class 타이머체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='BattleTimer'):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=1):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='BattleTimer')
        self.set_user_value(triggerId=99990002, key='Timer', value=2)


initial_state = 대기
