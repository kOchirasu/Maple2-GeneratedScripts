""" trigger/63000089_cs/trigger_15.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[315], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[115]):
            return 발판15(self.ctx)


class 발판15(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[315], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[115]):
            return 발판15끝(self.ctx)


class 발판15끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='415', seconds=2, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='415'):
            return 대기(self.ctx)


initial_state = 대기
