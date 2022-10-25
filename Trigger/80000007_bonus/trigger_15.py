""" trigger/80000007_bonus/trigger_15.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[302]):
            return 막힘(self.ctx)


class 막힘(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[410,411,412,413,414,415,416,417,418], visible=False)


initial_state = 대기
