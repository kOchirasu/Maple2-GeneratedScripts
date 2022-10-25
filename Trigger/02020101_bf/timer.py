""" trigger/02020101_bf/timer.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900002, key='TimerReset', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TimerStart', value=1):
            return 타이머1_시작(self.ctx)


class 타이머1_시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=20, startDelay=1, interval=1, vOffset=-40)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TimerStart', value=9):
            return 종료(self.ctx)
        if self.user_value(key='TimerStart', value=0):
            return 리셋_1(self.ctx)
        if self.time_expired(timerId='1'):
            return 리셋_1(self.ctx)


class 리셋_1(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900002, key='TimerReset', value=1)
        self.reset_timer(timerId='1')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TimerStart', value=9):
            return 종료(self.ctx)
        if self.user_value(key='TimerStart', value=2):
            return 타이머2_시작(self.ctx)


class 타이머2_시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=20, startDelay=1, interval=1, vOffset=-40)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TimerStart', value=9):
            return 종료(self.ctx)
        if self.user_value(key='TimerStart', value=0):
            return 리셋_2(self.ctx)
        if self.time_expired(timerId='2'):
            return 리셋_2(self.ctx)


class 리셋_2(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900002, key='TimerReset', value=2)
        self.reset_timer(timerId='2')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TimerStart', value=9):
            return 종료(self.ctx)
        if self.user_value(key='TimerStart', value=3):
            return 타이머3_시작(self.ctx)


class 타이머3_시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=20, startDelay=1, interval=1, vOffset=-40)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TimerStart', value=9):
            return 종료(self.ctx)
        if self.user_value(key='TimerStart', value=0):
            return 리셋_3(self.ctx)
        if self.time_expired(timerId='3'):
            return 리셋_3(self.ctx)


class 리셋_3(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900002, key='TimerReset', value=3)
        self.reset_timer(timerId='3')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TimerStart', value=9):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='2')
        self.reset_timer(timerId='3')


initial_state = 대기
