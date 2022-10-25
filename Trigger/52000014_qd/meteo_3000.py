""" trigger/52000014_qd/meteo_3000.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 낙하01(self.ctx)


class 낙하01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)
        self.set_mesh(triggerIds=[3000], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 초기화(self.ctx)


class 초기화(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 낙하01(self.ctx)


initial_state = 대기
