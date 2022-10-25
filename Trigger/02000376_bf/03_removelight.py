""" trigger/02000376_bf/03_removelight.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='ResetInnerLight', value=0)
        self.set_user_value(key='RemoveInnerLight', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetInnerLight', value=1):
            return Play(self.ctx)


class Play(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='ResetInnerLight', value=0)
        self.set_user_value(key='RemoveInnerLight', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RemoveInnerLight', value=1):
            return RemoveLight01(self.ctx)


class RemoveLight01(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9001], skillId=70000103, level=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
