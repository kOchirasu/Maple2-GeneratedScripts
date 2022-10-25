""" trigger/52000014_qd/cube_2300.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2300], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2305], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[12300], visible=False) # Fire Cast Sound

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[92300]):
            return 무너짐01(self.ctx)


class 무너짐01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)
        self.set_effect(triggerIds=[12300], visible=True) # Fire Cast Sound
        self.set_mesh(triggerIds=[2300], visible=False, arg3=0, delay=0, scale=1)
        self.set_mesh(triggerIds=[2305], visible=False, arg3=500, delay=0, scale=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[12300], visible=False) # Fire Cast Sound


initial_state = 대기
