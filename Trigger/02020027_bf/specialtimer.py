""" trigger/02020027_bf/specialtimer.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SpecialTimer', value=1):
            return 타이머시작(self.ctx)


class 타이머시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='SpecialTimer', seconds=180, startDelay=1, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 타이머체크(self.ctx)


class 타이머체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='SpecialTimer'):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990002, key='SpecialTimer', value=0)
        self.reset_timer(timerId='SpecialTimer')


initial_state = 대기
