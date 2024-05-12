""" trigger/52000051_qd/03_removelight.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='ResetInnerLight', value=0)
        self.set_user_value(key='RemoveInnerLight', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetInnerLight', value=1):
            return Play(self.ctx)


class Play(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='ResetInnerLight', value=0)
        self.set_user_value(key='RemoveInnerLight', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RemoveInnerLight', value=1):
            return RemoveLight01(self.ctx)


class RemoveLight01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[9001], skillId=70000103, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
