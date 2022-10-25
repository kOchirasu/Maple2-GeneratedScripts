""" trigger/02100001_bf/3003_falldown.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3003], visible=True, arg3=0, delay=0, scale=0) # 투명 발판

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9003]):
            return RemoveMesh(self.ctx)


class RemoveMesh(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3003], visible=False, arg3=0, delay=0, scale=0) # 투명 발판

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[9003]):
            return Wait(self.ctx)


initial_state = Wait
