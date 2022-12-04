""" trigger/02020051_bf/103_potion.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Main', value=1):
            return 포션사용_준비(self.ctx)


class 포션사용_준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002131], state=2)
        self.set_user_value(triggerId=101, key='Potion', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=720000):
            return 포션사용(self.ctx)


class 포션사용(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002131], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002131], stateValue=0):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=101, key='Potion', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Main', value=2):
            return 준비(self.ctx)


initial_state = 준비
