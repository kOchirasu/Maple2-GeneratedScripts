""" trigger/63000006_cs/shake03.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5070], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5070], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 간격랜덤(self.ctx)


class 간격랜덤(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=25):
            return 초간격4(self.ctx)
        if self.random_condition(rate=25):
            return 초간격5(self.ctx)
        if self.random_condition(rate=25):
            return 초간격6(self.ctx)
        if self.random_condition(rate=25):
            return 초간격7(self.ctx)


class 초간격4(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 초기화(self.ctx)
        if self.user_detected(boxIds=[9002]):
            return 종료(self.ctx)


class 초간격5(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 초기화(self.ctx)
        if self.user_detected(boxIds=[9002]):
            return 종료(self.ctx)


class 초간격6(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=6)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 초기화(self.ctx)
        if self.user_detected(boxIds=[9002]):
            return 종료(self.ctx)


class 초간격7(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=7)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='4'):
            return 초기화(self.ctx)
        if self.user_detected(boxIds=[9002]):
            return 종료(self.ctx)


class 초기화(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5070], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 시작(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5070], visible=False)


initial_state = 대기
