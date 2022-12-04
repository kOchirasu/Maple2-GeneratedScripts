""" trigger/02020310_bf/move_3.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Archeon3', value=1):
            self.set_user_value(triggerId=900009, key='Archeon3', value=0)
            return Archeon_Ready(self.ctx)


class Archeon_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_any_user_additional_effect(boxId=10001, additionalEffectId=73000007, level=1):
            self.move_user_to_pos(pos=[8700,-4800,2750], rot=[0,0,0])
            return Archeon_On(self.ctx)


class Archeon_On(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기(self.ctx)


initial_state = 대기
