""" trigger/99999925/checkpolymorph.xml """
import trigger_api


class CheckIdle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BuffGo', value=1):
            return Checkpoly(self.ctx)


class Checkpoly(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='BuffStart', value=1, isModify=True)
        self.set_user_value(key='BuffGo', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CheckIdle(self.ctx)


initial_state = CheckIdle
